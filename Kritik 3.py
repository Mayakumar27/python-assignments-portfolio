import numpy as np

def central_difference_derivative(f, x, dx=1e-8):
    
    return (f(x + dx) - f(x - dx)) / (2 * dx)

def linear_approximation(f, c, x, derivative_at_c):

    return f(c) + derivative_at_c * (x - c)

def find_points_with_error(f, c, E, dx=1e-8, tolerance=1e-8, max_iter=1000):

    derivative_at_c = central_difference_derivative(f, c, dx)
    f_c = f(c)

    def L(x):
        return linear_approximation(f, c, x, derivative_at_c)
    x1, x2 = c - dx, c + dx
    iter_count_x1, iter_count_x2 = 0, 0

    while iter_count_x1 < max_iter:
        error_x1 = abs(f(x1) - L(x1))
        if abs(error_x1 - E) < tolerance:
            break
        x1 -= dx
        iter_count_x1 += 1
    else:
        x1 = None

    while iter_count_x2 < max_iter:
        error_x2 = abs(f(x2) - L(x2))
        if abs(error_x2 - E) < tolerance:
            break
        x2 += dx
        iter_count_x2 += 1
    else:
        x2 = None

    if x1 is not None and x2 is not None:
        return x1, x2
    else:
        return "No such x1 and x2 found within specified range or iterations."

# (i)
print("(i): f(x) = x^2")
f1 = lambda x: x ** 2
result = find_points_with_error(f1, c=1, E=0.1)
if isinstance(result, tuple):
    x1, x2 = result
    print(f"x1 = {x1}, x2 = {x2}\n")
else:
    print(result)

# (ii)
print("(ii): f(x) = sin(x)")
f2 = lambda x: np.sin(x)
result = find_points_with_error(f2, c=np.pi / 4, E=0.05)
if isinstance(result, tuple):
    x1, x2 = result
    print(f"x1 = {x1}, x2 = {x2}\n")
else:
    print(result)

# (iii)
print("(iii): f(x) = e^x")
f3 = lambda x: np.exp(x)
result = find_points_with_error(f3, c=0, E=0.01)
if isinstance(result, tuple):
    x1, x2 = result
    print(f"x1 = {x1}, x2 = {x2}")
else:
    print(result)

