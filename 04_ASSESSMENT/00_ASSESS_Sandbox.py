import numpy as np
import matplotlib.pyplot as plt
import random


def linear_generator(gradient, y_intercept):

    x_linear = np.linspace(-15, 15, 40)
    y_linear = gradient * x_linear + y_intercept

    # plotting the points
    plt.plot(x_linear,y_linear, linewidth=3, label='Linear')

    plt.ylim(-25, 20)
    plt.xlim(-20, 20)

    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('Linear Graph')

    plt.legend()

    # function to show the plot
    plt.show()

gradient = int(input("Enter Gradient: "))
y_intercept = int(input("Enter y-int: "))

linear_generator(gradient, y_intercept)
