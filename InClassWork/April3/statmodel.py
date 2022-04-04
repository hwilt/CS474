import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind
from numpy.random import normal

control_times = normal(60, 10, 100) # [61, 49, ...]
test_times = normal(15, 90, 100) # [61, 49, ...]

t, p = ttest_ind(control_times, test_times)

print(f't-score: {t}')
print(f'p-value: {p}')