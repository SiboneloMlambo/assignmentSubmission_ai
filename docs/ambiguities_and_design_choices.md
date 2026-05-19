# Ambiguities and Design Choices

## 1. Unspecified beta parameter
The assignment brief explicitly notes that the original paper does not specify the value of beta used in the experiments. This project treats beta as an experimental variable and evaluates several values: `0.1, 0.25, 0.5, 1, 2, 5, 10`.

## 2. Planner choice
The paper uses classical planners as black-box subroutines. Fast Downward is recommended by the assignment, but the code also contains deterministic built-in planners so the repository remains runnable on a normal student machine without external planner installation.

## 3. Observation generation
Observation sequences are sampled as prefixes/partial traces from a hidden goal plan. Observation percentages are varied at `25%, 50%, 75%, 100%`.

## 4. Statistical rigour
Each condition is repeated with fixed random seeds. The summary files report mean accuracy, standard deviation, and 95% confidence intervals.

## 5. Noise extension
Noise is not required for a solo project, but is useful for stronger analysis. The implemented modes are missing, corrupt, spurious, and mixed observations.
