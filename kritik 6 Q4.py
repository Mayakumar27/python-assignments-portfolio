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

def expected_uniform(a, b):
    return (a + b) / 2

def expected_exponential(lambda_):
    return 1 / lambda_

def expected_dosage(mean, variance):
    E_X2 = variance + mean**2
    return 2.38 * E_X2

mu = 171  # Mean height in cm
sigma_squared = 7.1 ** 2  # Variance
a, b = 0, 1
lambda_ = 1 / 50

E_uniform = expected_uniform(a, b)
E_exponential = expected_exponential(lambda_)
E_dosage = expected_dosage(mu, sigma_squared)

print(f"Expected value for Uniform Distribution U({a}, {b}): {E_uniform}")
print(f"Expected value for Exponential Distribution Exp({lambda_}): {E_exponential}")
print(f"Expected Dosage Calculation: {E_dosage:.4f}")
