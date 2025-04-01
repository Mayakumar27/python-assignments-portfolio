import numpy as np
def roots(f, a, b, tol=1e-10, max_iter=1000):
    # Check if the initial interval is valid (i.e., f(a) and f(b) have opposite signs)
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) should have opposite signs.")
        return None

    # Initialize variables
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        # Find midpoint
        c = (a + b) / 2
        # Check if midpoint is a root or if interval is sufficiently small
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        # Update the interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2

def f1(x):
    return np.exp(x) + np.log(x)


def f2(x):
    return np.arctan(x) - x ** 2


def f3(x):
    return np.sin(x) / np.log(x)


def f4(x):
    return np.log(np.cos(x))

print("Root of f(x) = e^x + ln(x) on [0, 1]:", roots(f1, 0.5, 1))
print("Root of f(x) = arctan(x) - x^2 on [0, 2]:", roots(f2, 0, 2))
print("Root of f(x) = sin(x) / ln(x) on [3, 4]:", roots(f3, 3, 4))
print("Root of f(x) = ln(cos(x)) on [5, 7]:", roots(f4, 5, 7))

