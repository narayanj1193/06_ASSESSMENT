import random

# Functions at the top
def statement_generator(statement, decoration, above_below):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = above_below * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Parabola generator
def plot_parabola(x_intercepts_equation, vertex_equation, scale_factor):
    x_parabola = np.linspace(-20, 20, 10000)

    k = scale_factor

    if x_intercepts_equation:
        x_1, x_2 = x_intercepts
        y_parabola = k * (x_parabola - x_1) * (x_parabola - x_2)
        parabola_formula = f"y = {k} * (x - {x_1}) * (x - {x_2})"
    else:
        b, c = vertex_equation
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

# User Choice Checker
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


# Main Routine

questions_answered = 0
questions_attempted = 0
questions_incorrect = 0

amount_guesses = 0
guess = 0

question_summary = []

# creates a decorative statement, adds aesthetic to program, welcomes users

statement_generator("Welcome to Graphs Quiz", "!", "*")

# ask user if they have played before, if not, display instructions
played_before = yes_no_checker("Have you tried this quiz before? ")
if played_before == "no":
    instructions()

# asks user if they would like to do a quiz on types of graphs
mode = choice_checker("Would you like to be quizzed on Linear graphs, Parabola graphs, or a mix? ")

# asks for rounds
rounds = num_check("How many questions would you like to answer? <enter> "
                   "for continuous mode: ")

if rounds == "":
    rounds_mode = "continuous"

end_game = "no"
while end_game == "no":
