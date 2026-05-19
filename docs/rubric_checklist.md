# Rubric Checklist

## Understanding: 20 marks
- State precise, testable claims in `report/report.tex`.
- Explain the method: compliant vs non-compliant planning costs, cost difference, Boltzmann likelihood, Bayes posterior.

## Methodology & Implementation: 24 marks
- Describe implemented Python pipeline, PDDL/domain inputs, planners, scoring layer, repeated trials, beta sensitivity, and noise settings.
- Document ambiguities, especially the unspecified beta parameter.
- Specify domains, parameters, metrics, seeds, and computational environment.

## Results & Analysis: 28 marks
- Present results for at least two domains. This repo includes three.
- Compare accuracy across observation percentages and beta values.
- Report mean, standard deviation, and 95% confidence intervals.
- Discuss discrepancies and reproducibility limitations.

## Report Quality: 12 marks
- Use the report template sections required by the assignment.
- Use labelled tables and figures from `results/*/plots`.

## Code & Repository: 8 marks
- Keep this one-project folder structure.
- Include setup, run instructions, dependencies, and outputs.

## Video: 8 marks
- Use `video/five_minute_video_script.md`.
- Show a short demo of `python full_pipeline.py --mode single --beta 1.0`.
