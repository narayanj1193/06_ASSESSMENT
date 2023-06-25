import numpy as np
import matplotlib.pyplot as plt
import random


def linear_generator(gradient, y_intercept):
    x_linear = np.linspace(-15, 15, 40)
    y_linear = gradient * x_linear + y_intercept

    # plotting the points
    plt.plot(x_linear, y_linear, linewidth=3, label='Linear')

    plt.ylim(-25, 20)
    plt.xlim(-20, 20)

    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('Linear Graph')

    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

    plt.grid()

    # function to show the plot
    plt.show()


# gradient = float(input("Enter Gradient: "))
# y_intercept = float(input("Enter y-int: "))
end_game = ""
while end_game != "xxx":

    difficulty = input("Difficulty? ")

    if difficulty == "hard":
        gradient = round(random.uniform(0.5, 5), 1)
        y_intercept = random.randint(-15, 15)

    elif difficulty == "medium":
        gradient = random.randint(1, 20) * 0.5
        y_intercept = random.randint(-30, 30) * 0.5

    else:
        print("Easy Mode.\n")
        gradient = random.randint(1,8)
        y_intercept = random.randint(-15, 15)

    print(gradient, y_intercept)

    linear_generator(gradient, y_intercept)
