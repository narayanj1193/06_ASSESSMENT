import numpy as np
import matplotlib.pyplot as plt
import random


def plot_parabola(difficulty):
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

    # plotting the points
    plt.plot(x_parabola, y_parabola, linewidth=3, label='Parabola')

    plt.ylim(-25, 20)
    plt.xlim(-20, 20)

    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('Parabola Graph')

    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

    plt.grid()

    # function to show the plot
    plt.show()

    return parabola_formula


def user_choice(question, valid_list):
    # error code
    error = "Please choose a valid input."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


# Main routine
valid_difficulty = ["easy", "medium", "hard", "xxx"]

end_game = ""
while end_game != "xxx":
    # ask user for choice, check if its valid
    difficulty_parabola = user_choice("Choose your difficulty (Easy, Medium, or Hard): ", valid_difficulty)

    print(difficulty_parabola)
    formula = plot_parabola(difficulty_parabola)
    print(formula)

