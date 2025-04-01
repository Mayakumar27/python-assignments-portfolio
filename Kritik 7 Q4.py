import numpy as np
from scipy.stats import t

data = [92.64, 79.00, 84.79, 97.41, 93.68, 65.23, 84.50, 73.49, 73.97, 79.11]
mu_0 = 75
n = len(data)

x_bar = np.mean(data)

s = np.sqrt(sum((xi - x_bar) ** 2 for xi in data) / (n - 1))

t_0 = (x_bar - mu_0) / (s / np.sqrt(n))

alpha = 0.05
t_star = t.ppf(1 - alpha / 2, df=n-1)

if abs(t_0) <= t_star:
    conclusion = "Accept the null hypothesis: No significant difference."
else:
    conclusion = "Reject the null hypothesis: Significant difference detected."

print(f"Sample Mean (x̄): {x_bar:.2f}")
print(f"Sample Standard Deviation (s): {s:.2f}")
print(f"t_0 (Test Statistic): {t_0:.3f}")
print(f"t_* (Critical Value at 95% confidence): {t_star:.3f}")
print(f"Conclusion: {conclusion}")
