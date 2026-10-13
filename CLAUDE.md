# CLAUDE.md

**Read `AGENTS.md` first** — it is the full working contract (startup, invariants,
verification, definition of done, submission contract). This file adds the working rules.

## Working rules

- **Autonomous to the deadline.** Do not ask for step-by-step approval; make progress, record
  evidence, surface blockers. The gated exceptions are explicit: **creating/altering the GitHub
  repo, environment setup changes, using >4 GPUs, and any portal upload** — those need the owner's OK.
- **Agonism is the prize; binding is only the gate.** Never let a strong binding prediction stand in
  for activation. Score agonism against the **6X18 active state**, binding against the inactive `24–432`
  construct model, and keep them separate. No in-silico score proves agonism.
- **Queue heavy GPU work into idle windows.** Verify idle GPUs with `nvidia-smi`, one process per GPU,
  cap CPU threads, never clobber a foreign job. Default 4 GPUs; burst to 8 only when idle.
- **Adopt the latest SOTA** where it adds an orthogonal signal or real gain, after verifying availability
  + license (ODC-BY-clean for submitted designs). **Never claim a tool ran unless it actually ran.**
- **Devil's-advocate, then revise** every design and every metric before spending compute.
- **uv only** for environment work; heavy tools in isolated `envs/` venvs (`configs/tools.yaml`).
- **Re-validate the exact final sequence** end-to-end (submit == folded == scored); natural AAs, linear/disulfide.
- **Commit and push at each checkpoint** with a descriptive message and **no AI attribution**. Stage only
  source/docs/configs/harness; `results/ runs/ envs/ third_party/ weights/ data/raw/` stay gitignored.
