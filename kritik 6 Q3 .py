import numpy as np
import scipy.integrate as integrate

def normal_density(mean, variance, x):
    sigma = np.sqrt(variance)  # Standard deviation
    coef = 1 / (np.sqrt(2 * np.pi * variance))
    exponent = np.exp(-((x - mean) ** 2) / (2 * variance))
    return coef * exponent

def integration(mean, variance, a, b):
    result, _ = integrate.quad(lambda x: normal_density(mean, variance, x), a, b)
    return result

mu = 171
sigma_squared = 7.1 ** 2  # Variance

probability = integration(mu, sigma_squared, 162, 190)

print(f"Probability of height between 162 cm and 190 cm: {probability:.4f}")

