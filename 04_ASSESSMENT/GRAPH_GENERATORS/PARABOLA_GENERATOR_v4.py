import random
import numpy as np
import matplotlib.pyplot as plt
import threading


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


def generate_parabola(difficulty):
    x_parabola = np.linspace(-20, 20, 10000)

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
        y_parabola = k * (x_parabola - x_1) * (x_parabola - x_2)
        parabola_formula = f"y = {k} * (x - {x_1}) * (x - {x_2})"

    else:
        b, c = vertex
        y_parabola = k * (x_parabola - b) ** 2 + c
        parabola_formula = f"y = {k} (x - {b})^2 + {c}"

    # returns the equation of the graph
    return x_parabola, y_parabola, parabola_formula, "parabola"


def ask_equation(question):
    global user_response

    user_response = input(question)
    plt.close()


def main():
    # Main routine
    x_linear, y_linear, linear_formula, graph_type = generate_parabola("hard")

    # Create and start a thread to ask the equation
    equation_thread = threading.Thread(target=ask_equation, args=("What is the equation of the graph? ",))
    equation_thread.start()

    # Display the graph
    display_graph(x_linear, y_linear, graph_type)

    # Wait for the equation thread to complete
    equation_thread.join()

    # Access the user's response
    print("User's response:", user_response)


# Call the main function
main()
