import random
import numpy as np
import matplotlib.pyplot as plt
import threading

# Global variable to store the user's response
user_response = None


def display_graph(x, y, graph_type):
    # Plots graph
    plt.plot(x, y, linewidth=3, label='Linear')

    # Limits y axis
    plt.ylim(-25, 20)
    # Limits x axis
    plt.xlim(-20, 20)

    # Details on graph
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    if graph_type == "Linear":
        plt.title('Linear Graph')

    else:
        plt.title('Parabola Graph')

    # horizontal axis line at y = 0
    plt.axhline(color='black')
    # vertical axis line at x = 0
    plt.axvline(color='black')

    plt.legend()
    plt.grid()

    # shows graph
    plt.show()


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
    return x_linear, y_linear, linear_formula, "linear"


def ask_equation():
    global user_response
    user_response = input("What is the equation of the graph? ")
    plt.close()


# Main routine
x_linear, y_linear, linear_formula, graph_type = generate_linear("hard")

# Create and start a thread to ask the equation
equation_thread = threading.Thread(target=ask_equation)
equation_thread.start()

# Display the graph
display_linear(x_linear, y_linear, graph_type)

# Wait for the equation thread to complete
equation_thread.join()

# Access the user's response
print("User's response:", user_response)
