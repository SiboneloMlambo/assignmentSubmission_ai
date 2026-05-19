# Experiment Protocol

## Claims tested

1. Increasing the observation percentage improves top-1 goal recognition accuracy.
2. The posterior probability of the true goal increases as more observations are available.
3. The beta parameter affects confidence and robustness.
4. Observation noise reduces recognition accuracy.
5. The method is reproducible on small domains, but exact numerical reproduction is limited by underspecified original settings.

## Metrics

- Top-1 accuracy
- True-goal posterior probability
- True-goal rank
- Mean, standard deviation, and 95% confidence interval across runs

## Domains

- Blocksworld / Block Words
- Logistics
- Campus navigation

## Reproducibility command

```bash
python run_all_experiments.py --quick
python run_all_experiments.py
```
