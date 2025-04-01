import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y = sp.symbols('x y')

j = sp.sin(x**2 + y**2)

j_func = sp.lambdify((x, y), j, 'numpy')

x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)

Z = j_func(X, Y)

plt.contourf(X, Y, Z, levels=50, cmap='plasma')
plt.colorbar()
plt.title(r'Contour plot of $j(x, y) = \sin(x^2 + y^2)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
