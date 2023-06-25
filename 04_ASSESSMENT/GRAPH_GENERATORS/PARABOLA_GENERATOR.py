import numpy as np
import matplotlib.pyplot as plt
import random


def plot_parabola(x_intercepts_equation, vertex_equation):
    x_parabola = np.linspace(-20, 20, 10000)

    k = random.randint(1, 2)
    if x_intercepts_equation:
        x_1, x_2 = x_intercepts
        y_parabola = k * (x_parabola - x_1) * (x_parabola - x_2)

    else:
        b, c = vertex_equation
        y_parabola = k * (x_parabola - b) ** 2 + c

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


x_intercepts = [random.randint(-15, 15), random.randint(-15, 15)]
vertex = [random.randint(-5, 10), random.randint(-5, 10)]

use_vertex = random.choice([True, False])

print(use_vertex)
if not use_vertex:
    print(x_intercepts)
    plot_parabola(x_intercepts, False)

else:
    print(vertex)
    plot_parabola(False, vertex)
