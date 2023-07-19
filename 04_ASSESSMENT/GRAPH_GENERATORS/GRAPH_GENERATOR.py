import random
import numpy as np
import matplotlib.pyplot as plt
import threading


def display_graph(x, y, graph_type):
    # Plots graph
    plt.plot(x, y, linewidth=3)

    # Limits y axis
    plt.ylim(-25, 20)
    # Limits x axis
    plt.xlim(-20, 20)

    # Details on graph
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    if graph_type == "linear":
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


def graph_generator(difficulty, mode):
    graph_formula = 0
    y_graph = 0
    x_graph = np.linspace(-20, 20, 10000)
    types_of_graphs = ['parabola', 'linear']
    type_graph = mode

    if mode == 'mixed':
        type_graph = random.choice(types_of_graphs)

    if type_graph == 'parabola':
        if difficulty == "easy":
            x_1 = random.randint(1, 10)
            x_2 = random.randint((x_1 - 2), (x_1 + 2))

            k = random.randint(1, 2)

            vertex = [random.randint(0, 5), random.randint(0, 5)]

        elif difficulty == "medium":
            x_1 = random.randint(-20, 20) * 0.5
            x_2 = round(random.uniform(x_1 - 5.5, x_1 + 5.5))

            k = random.randint(1, 5)

            vertex = [random.randint(-20, 20) * 0.5, random.randint(-20, 20) * 0.5]

        else:
            x_1 = round(random.uniform(-10, 10), 1)
            x_2 = round(random.uniform(x_1 - 5, x_1 + 5), 1)

            k = 0
            while k == 0:
                k = random.randint(-5, 5)

            vertex = [round(random.uniform(-10, 10), 1), round(random.randint(-10, 10), 1)]

        x_intercepts = [x_1, x_2]

        use_vertex = random.choice([True, False])

        if not use_vertex:
            x_1, x_2 = x_intercepts
            y_graph = k * (x_graph - x_1) * (x_graph - x_2)
            graph_formula = f"y = {k} * (x - {x_1}) * (x - {x_2})"

        else:
            b, c = vertex
            y_graph = k * (x_graph - b) ** 2 + c
            graph_formula = f"y = {k} (x - {b})^2 + {c}"

    elif type_graph == "linear":
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
        else:
            # (easy mode) generates features that are integers
            gradient = random.randint(1, 8)
            y_intercept = random.randint(-15, 15)

        # Placement of y coordinate according to the x points
        y_graph = gradient * x_graph + y_intercept

        # Formula of the graph
        graph_formula = f'{gradient} * x + {y_intercept}'


    # returns the equation of the graph
    return x_graph, y_graph, graph_formula, mode


def ask_equation(question):
    global user_response

    user_response = input(question)
    plt.close()


def main():
    # Main routine
    difficulty = input('what difficulty? ')
    mode = input('what mode? ')
    while True:
        print_new = False
        while print_new is False:
            x, y, graph_formula, graph_type = graph_generator(difficulty, mode)

            # Create and start a thread to ask the equation
            equation_thread = threading.Thread(target=ask_equation, args=("New graph? ",))
            equation_thread.start()

            # Display the graph
            display_graph(x, y, graph_type)

            # Wait for the equation thread to complete
            equation_thread.join()

            # Access the user's response
            if user_response == 'yes':
                print_new = True


# Call the main function
main()