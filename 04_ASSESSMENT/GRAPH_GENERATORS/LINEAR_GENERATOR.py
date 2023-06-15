import numpy as np
import matplotlib.pyplot as plt
import random

def linear_generator(x, y):

    if x > 10:
        x_points = [x, x-15]
    else:
        x_points = [x, x+15]

    if y > 10:
        y_points = [y, y-15]
    else:
        y_points = [y, y+15]

    # plotting the points
    plt.plot(x_points, y_points, linewidth=3, label='Linear')

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

linear_generator(random.randint(-15, 15), random.randint(-15, 15))