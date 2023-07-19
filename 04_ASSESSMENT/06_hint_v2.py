import random
import sympy as sp


def find_random_coordinate(graph_formula):

    # if iterations reach max_iterations it continues to the next loop.
    # makes sure it does not run infinitely
    for i in range(1, 100):
        x = random.randint(-5, 5)  # Assuming x ranges from -5 to 5
        x_val = sp.symbols('x')  # Create a symbolic variable 'x' for substitution

        try:
            y = sp.sympify(graph_formula).subs(x_val, x)  # Evaluate the equation with the random x value
            if y == round(y, 0):
                return x, y  # Return the coordinates (x, y)
        except TypeError:
            pass

    # If no integer value is found within the maximum iterations, search for a y value with one decimal place
    while True:
        x = random.randint(-5, 5)  # Generate another random x value
        x_val = sp.symbols('x')  # Create a symbolic variable 'x' for substitution

        try:
            y = sp.sympify(graph_formula).subs(x_val, x)  # Evaluate the equation with the random x value
            y = round(y, 1)  # Round the y value to one decimal place
            return x, y  # Return the coordinates (x, y)

        # error handling
        except TypeError:
            pass


# Example usage:

equation = "x**2 + 2*x - 3"  # Replace with your desired quadratic equation
random_coordinate = find_random_coordinate(equation)
print(f"The graph passes through: {random_coordinate}")
