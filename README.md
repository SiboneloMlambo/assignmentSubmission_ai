# Probabilistic Plan Recognition Reproducibility Study

Solo reproducibility project for Ramírez and Geffner, **“Probabilistic Plan Recognition Using Off-the-Shelf Classical Planners” (AAAI 2010)**.

This repository is organised as one submission-ready project. It contains three domain experiments so the individual requirement of **at least two planning domains** is covered with an extra domain for stronger evidence:

- `blocksworld`
- `logistics`
- `campus`

The implementation follows the assignment brief: compile/score candidate goals, compute Bayesian posterior probabilities, run repeated trials over observation percentages, investigate the unspecified `beta` parameter, and report variance through standard deviations and 95% confidence intervals.

## Project structure

```text
prob_plan_recognition_reproducibility_solo/
├── README.md
├── requirements.txt
├── run_all_experiments.py
├── scripts/
│   └── clean_outputs.py
├── domains/
│   ├── blocksworld/
│   ├── logistics/
│   └── campus/
├── results/
│   ├── blocksworld/
│   ├── logistics/
│   └── campus/
├── report/
│   └── report.tex
├── docs/
│   ├── rubric_checklist.md
│   ├── ambiguities_and_design_choices.md
│   └── experiment_protocol.md
```

Each domain folder is runnable on its own and has its own `full_pipeline.py`, PDDL files, planner/scorer code, tests, and outputs.

## Installation

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Run all domains

For a quick reproducibility check:

```bash
python run_all_experiments.py --quick
```

For the full repeated experiment:

```bash
python run_all_experiments.py
```

## Run one domain manually

```bash
cd domains/blocksworld
python full_pipeline.py --mode single --beta 1.0
python full_pipeline.py --mode publication --runs 50
```

Repeat with `domains/logistics` and `domains/campus`.

## Outputs

Main outputs are written inside each domain under `outputs/` and copied into the top-level `results/` folder:

```text
publication_raw_candidates.csv  # candidate-goal rows
publication_trials.csv          # trial-level rows
publication_summary.csv         # grouped mean, std, CI results
plots/*.png                     # report-ready figures
```

