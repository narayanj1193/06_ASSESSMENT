import random
import sympy

def find_random_coordinate(graph_formula):
    x = random.randint(-5, 5)  # Assuming x ranges from -100 to 100
    x_val = sympy.symbols('x')
    y = sympy.sympify(graph_formula).subs(x_val, x)  # Evaluate the equation with the random x value
    return x, y

# Example usage:
equation = "x**2 + 2*x - 3"  # Replace with your desired quadratic equation
random_coordinate = find_random_coordinate(equation)
print(f"The graph passes through: {random_coordinate}")
