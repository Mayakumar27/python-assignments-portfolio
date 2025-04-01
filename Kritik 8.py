import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Gradient Descent Function
def gradient_descent(x0, y0, f, grad_f, alpha, num_iterations):
    """
    Performs gradient descent to find a local minimum.

    Parameters:
    x0, y0 : Initial coordinates for descent.
    f : Function of two variables (x, y).
    grad_f : Function that computes the gradient of f.
    alpha : Learning rate.
    num_iterations : Number of iterations to perform.

    Returns:
    x, y : Coordinates of the final point after gradient descent.
    """
    x, y = x0, y0

    for i in range(num_iterations):
        grad_x, grad_y = grad_f(x, y)
        x -= alpha * grad_x
        y -= alpha * grad_y

    return x, y

def fun_1(x, y):
    return x**2 + y**2

def grad_f_1(x, y):
    grad_x = 2*x
    grad_y = 2*y
    return grad_x, grad_y

x1, y1 = gradient_descent(0.1, 0.1, fun_1, grad_f_1, 0.1, 10)
x2, y2 = gradient_descent(-1, 1, fun_1, grad_f_1, 0.01, 100)

print("Final point for f1 with (0.1, 0.1), alpha=0.1, iterations=10:", (x1, y1))
print("Final point for f1 with (-1,1), alpha=0.01, iterations=100:", (x2, y2))

def fun_2(x, y):
    return 1 - np.exp(-x**2 - (y - 2)**2) - 2 * np.exp(-x**2 - (y + 2)**2)

def grad_f_2(x, y):
    grad_x = 2*x * np.exp(-x**2 - (y - 2)**2) + 4*x * np.exp(-x**2 - (y + 2)**2)
    grad_y = 2*(y-2) * np.exp(-x**2 - (y - 2)**2) + 4*(y+2) * np.exp(-x**2 - (y + 2)**2)
    return grad_x, grad_y

x3, y3 = gradient_descent(0, 1, fun_2, grad_f_2, 0.01, 10000)
x4, y4 = gradient_descent(0, -1, fun_2, grad_f_2, 0.01, 10000)

print("Final point for f2 with (0,1), alpha=0.01, iterations=10000:", (x3, y3))
print("Final point for f2 with (0,-1), alpha=0.01, iterations=10000:", (x4, y4))

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = fun_2(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f2(X,Y)')
ax.set_title('3D Plot of f2(X, Y)')

plt.show()
