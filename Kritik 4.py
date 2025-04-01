import matplotlib.pyplot as plt
import numpy as np

def gradient_descent(f, learning_rate, initial_point, max_steps=10000, tolerance=1e-10):
    def deriv(f, base_point):
        dx = 1e-10
        return (f(base_point + dx) - f(base_point - dx)) / (2 * dx)

    # Initialize variables
    x_coords = [initial_point]
    y_coords = [f(initial_point)]
    x_current = initial_point

    for step in range(max_steps):
        gradient = deriv(f, x_current)
        if abs(gradient) < tolerance:  # Stopping condition: derivative close to 0
            break
        x_next = x_current - learning_rate * gradient
        x_coords.append(x_next)
        y_coords.append(f(x_next))
        x_current = x_next

    # Plot the function and the steps of gradient descent
    plot_range = np.linspace(min(x_coords) - 0.5, max(x_coords) + 0.5, 1000)
    function_range = [f(i) for i in plot_range]
    plt.figure(figsize=(10, 6))
    plt.plot(plot_range, function_range, label="f(x)", color="blue")
    plt.scatter(x_coords, y_coords, color="red", label="Steps")
    plt.title("Gradient Descent")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Return the last x and y values
    return round(x_coords[-1], 3), round(y_coords[-1], 3)
# Example 1: f(x) = x^2
f1 = lambda x: x**2
min_x1, min_y1 = gradient_descent(f1, learning_rate=0.1, initial_point=5)
print(f"Local minimum for f(x) = x^2: x = {min_x1}, f(x) = {min_y1}")

# Example 2: f(x) = x^4 - 2x^2
f2 = lambda x: x**4 - 2*x**2
min_x2, min_y2 = gradient_descent(f2, learning_rate=0.05, initial_point=2)
print(f"Local minimum for f(x) = x^4 - 2x^2: x = {min_x2}, f(x) = {min_y2}")
