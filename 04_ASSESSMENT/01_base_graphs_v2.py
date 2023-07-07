import random
import numpy as np
import matplotlib.pyplot as plt


def display_linear(x_linear, y_linear):

    # Plots graph
    plt.plot(x_linear, y_linear, linewidth=3, label='Linear')

    # Limits y axis
    plt.ylim(-25, 20)
    # Limits x axis
    plt.xlim(-20, 20)

    # Details on graph
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Linear Graph')

    # horizontal axis line at y = 0
    plt.axhline(color='black')
    # vertical axis line at x = 0
    plt.axvline(color='black')

    plt.legend()
    plt.grid()

    # shows graph
    plt.show()


# Function to generate a linear graph based on the specified difficulty level
def generate_linear(difficulty):

    if difficulty == "hard":
        # If difficulty is hard the gradient will be any random decimal between 0.5 and 5.
        gradient = round(random.uniform(0.5, 5), 1)

        # If difficulty is hard the y_intercept will be any random decimal between -15 and 15
        y_intercept = round(random.uniform(-15, 15), 1)

    elif difficulty == "medium":
        # If difficulty is medium the gradient will be a multiple of 0.5 between 0.5 and 10
        gradient = random.randint(1, 20) * 0.5

        # If difficulty is medium the y_intercept will be a multiple of 0.5 between -15, and 15
        y_intercept = random.randint(-30, 30) * 0.5

    # (easy mode) generates features that are integers
    else:
        gradient = random.randint(1, 8)
        y_intercept = random.randint(-15, 15)

    # Array of x points that is used for calculating the y points.
    x_linear = np.linspace(-15, 15, 40)

    # Placement of y coordinate according to the x points
    y_linear = gradient * x_linear + y_intercept

    # Formula of the graph
    linear_formula = f'{gradient} * x + {y_intercept}'

    # returns the equation of the graph
    return x_linear, y_linear, linear_formula


# Main routine
x_linear, y_linear, linear_formula = generate_linear("hard")
display_linear(x_linear, y_linear)
