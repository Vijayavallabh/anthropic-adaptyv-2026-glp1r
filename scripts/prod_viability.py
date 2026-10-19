#!/usr/bin/env python3
"""Production-viability scorecard for a GLP1R Track-3 submission.

NECESSARY-CONDITION developability only (expression / solubility / proteolysis / message
availability in the REAL Adaptyv construct). This is NOT an agonism score and never ranks
agonism -- it flags designs that cannot physically express/survive/present, which are wasted
shots-on-goal regardless of design intent. Firewall-safe.

Construct (organizer-clarified): (f)Met (added when missing) + design + flexible tail
  tail = GGSGG + GFP11(RDHMVLHEYVNAAGIT) + GGSGG + Twin-Strep(WSHPQFEK..WSHPQFEK)
GFP11 is a split-GFP reporter => expression level is what the assay reads out, so
solubility/aggregation of the fusion is a first-order viability axis.
"""
import csv, sys

TAIL = "GGSGGRDHMVLHEYVNAAGITGGSGGWSHPQFEKGGGSGGGSGGSAWSHPQFEK"

# Kyte-Doolittle hydropathy
KD = {'I':4.5,'V':4.2,'L':3.8,'F':2.8,'C':2.5,'M':1.9,'A':1.8,'G':-0.4,'T':-0.7,
      'S':-0.8,'W':-0.9,'Y':-1.3,'P':-1.6,'H':-3.2,'E':-3.5,'Q':-3.5,'D':-3.5,
      'N':-3.5,'K':-3.9,'R':-4.5}
# Eisenberg consensus hydrophobicity (for hydrophobic moment)
EIS = {'I':1.38,'F':1.19,'V':1.08,'L':1.06,'W':0.81,'M':0.64,'A':0.62,'C':0.29,
       'G':0.48,'Y':0.26,'T':-0.05,'S':-0.18,'H':-0.40,'Q':-0.85,'K':-1.50,
       'N':-0.78,'E':-0.74,'D':-0.90,'R':-2.53,'P':0.12}
PKA = {'D':3.65,'E':4.25,'H':6.0,'C':8.3,'Y':10.07,'K':10.53,'R':12.48}
HPHOB = set("FILVWMYAC")  # aggregation-prone residues

def net_charge(seq, pH=7.4):
    q = 0.0
    q += 1.0/(1+10**(pH-8.0))          # N-term
    q += -1.0/(1+10**(3.1-pH))         # C-term
    for a in seq:
        if a in ('K','R','H'):
            q += 1.0/(1+10**(pH-PKA[a]))
        elif a in ('D','E','C','Y'):
            q += -1.0/(1+10**(PKA[a]-pH))
    return q

def gravy(seq):
    return sum(KD.get(a,0) for a in seq)/len(seq)

def max_hphob_window(seq, w=5):
    if len(seq) < w: return gravy(seq)
    return max(sum(KD.get(a,0) for a in seq[i:i+w])/w for i in range(len(seq)-w+1))

def longest_hphob_run(seq):
    best=cur=0
    for a in seq:
        cur = cur+1 if a in HPHOB else 0
        best=max(best,cur)
    return best

def ch_margin(seq):
    """Uversky charge-hydrophobicity boundary: R_b = 2.785*H - 1.151 (H = KD scaled 0..1,
    R = |net charge|/len). margin>0 = soluble/disordered side; <0 = compact/aggregation-prone."""
    H = sum((KD.get(a,0)+4.5)/9.0 for a in seq)/len(seq)
    R = abs(net_charge(seq))/len(seq)
    return R - (2.785*H - 1.151)

def protease_sites(seq):
    """Trypsin (after K/R not before P) + chymotrypsin (after F/Y/W/L/M not before P)."""
    n=0
    for i,a in enumerate(seq[:-1]):
        nxt=seq[i+1]
        if nxt=='P': continue
        if a in ('K','R') or a in ('F','Y','W','L','M'): n+=1
    return n

def construct(seq):
    return (seq if seq[0]=='M' else 'M'+seq) + TAIL

def row(name, seq):
    c = construct(seq)
    return {
        'name':name,'len':len(seq),'seq':seq,
        'net_charge':round(net_charge(seq),2),
        'gravy':round(gravy(seq),2),
        'max_hphob_w5':round(max_hphob_window(seq),2),
        'long_hphob_run':longest_hphob_run(seq),
        'ch_margin':round(ch_margin(seq),3),
        'prot_sites':protease_sites(seq),
        'prot_density':round(protease_sites(seq)/len(seq),3),
        # fusion context (M+design+tail): does the whole expressed thing stay soluble?
        'constr_len':len(c),
        'constr_charge':round(net_charge(c),2),
        'constr_gravy':round(gravy(c),2),
        'constr_ch_margin':round(ch_margin(c),3),
    }

def main(path):
    with open(path, newline='') as f:
        r=list(csv.DictReader(f))
    rows=[row(d['name'], d['sequence']) for d in r]
    cols=['name','len','net_charge','gravy','max_hphob_w5','long_hphob_run','ch_margin',
          'prot_sites','prot_density','constr_charge','constr_ch_margin']
    w=max(len(x['name']) for x in rows)
    print(f"{'name':<{w}} {'len':>3} {'netQ':>5} {'gravy':>6} {'hphobW5':>7} {'run':>3} "
          f"{'chMarg':>7} {'protN':>5} {'protD':>6} {'cQ':>6} {'cChM':>7}")
    for x in rows:
        print(f"{x['name']:<{w}} {x['len']:>3} {x['net_charge']:>5} {x['gravy']:>6} "
              f"{x['max_hphob_w5']:>7} {x['long_hphob_run']:>3} {x['ch_margin']:>7} "
              f"{x['prot_sites']:>5} {x['prot_density']:>6} {x['constr_charge']:>6} "
              f"{x['constr_ch_margin']:>7}")
    # Outlier flags (portfolio-relative, necessary-condition only)
    def flag(x):
        f=[]
        if x['ch_margin'] < -0.15: f.append('AGG(ch_margin<<0)')
        if x['max_hphob_w5'] > 2.0: f.append('HYDROPHOBIC_PATCH')
        if x['long_hphob_run'] >= 6: f.append('HPHOB_RUN>=6')
        if abs(x['net_charge']) < 1.0: f.append('NEAR_NEUTRAL(low soln)')
        if x['prot_density'] > 0.45: f.append('PROTEASE_DENSE')
        if x['constr_ch_margin'] < -0.05: f.append('FUSION_AGG')
        return f
    print("\n=== viability flags (necessary-condition; NOT agonism) ===")
    any_flag=False
    for x in rows:
        fl=flag(x)
        if fl:
            any_flag=True
            print(f"  {x['name']:<14} {x['seq']:<46} -> {', '.join(fl)}")
    if not any_flag:
        print("  none — all designs pass the production-viability floor")
    # write csv
    out=path.replace('.csv','_viability.csv')
    with open(out,'w',newline='') as f:
        wr=csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator='\n')
        wr.writeheader(); wr.writerows(rows)
    print(f"\nwrote {out}")

if __name__=='__main__':
    main(sys.argv[1])
