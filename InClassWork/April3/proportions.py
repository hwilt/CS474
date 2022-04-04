import numpy as np
from statsmodels.stats.proportion import proportions_ztest


trials = np.array([50, 25])
successes = np.array([5, 20])

z, p = proportions_ztest(successes, trials, alternative='two-sided')

print(f'z-score: {z}')
print(f'p-value: {p}')


