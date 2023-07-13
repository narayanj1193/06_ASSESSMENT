import random
import threading

import sympy as sp
import fractions
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean


# Function for choice checking. Compares users answer to items in valid_list.
def user_choice(question, valid_list):
    # Error code in case of user inputting something that is not in the valid_list.
    error = "Please choose a valid input."

    while True:
        user_answer = input(question).lower()

        for item in valid_list:
            if user_answer == item[0] or user_answer == item:
                # If user_answer is the first letter of item,
                # or is item, returns item.
                return item

        # If it is not in valid_list it prints error
        print(f"{error}\n")


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


def graph_generator(difficulty, mode):
    graph_formula = 0
    y_graph = 0
    x_graph = np.linspace(-20, 20, 10000)

    if mode == 'parabola':
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

    elif mode == "linear":
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


# Function that checks if an input is valid. If int_only is false it works well for equations, as it allows all sorts
# of inputs including floats and strings
def num_check(question, int_only=True, graph_close=False):
    global user_answer
    error = "Please enter a valid number or 'xxx' to exit."

    while True:
        user_answer = input(question)

        if user_answer == "xxx":
            return "end_game"

        elif user_answer == "":
            if int_only:
                # If an empty string is entered and only integers are allowed, return the empty string
                return
            else:
                print(error)
                continue

        elif user_answer != "":
            if not int_only:
                # If non-integer values are allowed, check for special cases and evaluate the user_answer
                if user_answer.lower() == 'x' or ('x' in user_answer.lower() and '+' in user_answer or '-' in user_answer):
                    # If the user_answer contains 'x' with '+' or '-', return the user_answer
                    return

                if '^' in user_answer and '2' in user_answer:
                    # If the user_answer contains '^' and '2', return the user_answer
                    return

                try:
                    number = eval(user_answer)
                    if isinstance(number, float) or isinstance(number, int) or isinstance(number, fractions.Fraction):
                        # If the evaluated user_answer is a float, integer, or fraction, return the number
                        user_answer = number
                    else:
                        print(error)
                        continue

                # error handling (errors happen alot 🥲)
                except (NameError, ZeroDivisionError, SyntaxError, TypeError, SyntaxWarning):
                    print(error)
                    continue

            else:
                try:
                    user_answer = int(user_answer)
                    if user_answer < 1:
                        # If the user_answer is an integer less than 1, print an error message
                        print(error)
                        continue

                except ValueError:
                    print(error)
                    continue

            if graph_close:
                plt.close()

            return


# Function that simplifies two equations and compares them to see if they are the same
def answer_checker(eq1, eq2):
    # Replace characters within the equations to valid alternatives, to ensure there are no errors.
    if '^' in eq1:
        eq1 = eq1.replace('^', '**').replace(' ', '')

    if '^' in eq2:
        eq2 = eq2.replace('^', '**').replace(' ', '')

    elif '- -' in eq1:
        eq1 = eq1.replace('- -', '+')

    elif '(' in eq2:
        eq2 = eq2.replace('(', '* (')

    # symbol x for symbol calculations
    x = sp.Symbol('x')

    try:
        # substitutes all numbers from -20, 20 into each equation.
        for i in range(-20, 21):
            x_val = i
            y1 = sp.sympify(eq1).subs(x, x_val)
            y2 = sp.sympify(eq2).subs(x, x_val)

            if y1 != y2:
                return False

            else:
                return True

    # error handling
    except sp.SympifyError:
        print("Invalid equation. Please try again.")
        return 'try again'


def find_random_coordinate(graph_formula):
    x = random.randint(-5, 5)  # Assuming x ranges from -100 to 100
    x_val = sp.symbols('x')
    y = sp.sympify(graph_formula).subs(x_val, x)  # Evaluate the equation with the random x value
    y = round(y, 1)
    return x, y


def statement_generator(statement, decoration, above_below, has_emoji=False):
    sides = decoration * 3
    statement = f"{sides} {statement} {sides}"

    if has_emoji:
        top_bottom_length = len(statement) + (len(sides) * 2) + 2
    else:
        top_bottom_length = len(statement)

    top_bottom = above_below * top_bottom_length

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def instructions():
    print("*** How to Play ***")
    print()
    print("These are the rules:")
    print()
    return ""


def main():

    questions_attempted = 0
    questions_correct = 0
    questions_wrong = 0
    users_result = 0
    yes_no_list = ['yes', 'no']
    difficulty_list = ['easy', 'medium', 'hard']
    modes_list = ['linear', 'parabola', 'mixed']
    game_summary = []
    guess_array = []

    statement_generator('WELCOME TO GRAPHS QUIZ', '📈', '*', True)

    played_before = user_choice('Have you done this quiz before? ', yes_no_list)

    if played_before == "no":
        instructions()

    questions = num_check("How many questions would you like to attempt? <enter> for continuous mode: ", True)
    if questions == "end_game":
        print("Thanks for playing! ")
        exit()

    mode = user_choice("What mode would you like to play? (linear, parabola, or mixed): ", modes_list)

    difficulty = user_choice("What difficulty would you like to play at? (easy, medium, or hard): ", difficulty_list)

    end_game = False
    while end_game is not True:
        next_question = False
        amount_attempts = 0

        if end_game is True:
            break

        if questions != "" and questions_attempted == questions:
            end_game = True

        questions_attempted += 1
        print()
        if questions == "":
            heading = f"Continuous Mode: Question {questions_attempted}"
        else:
            heading = f"Question: {questions_attempted} of {questions}"
        print(heading)

        # Generates details of the graph.
        x, y, graph_formula, graph_type = graph_generator(difficulty, mode)

        while next_question is not True and end_game is not True:
            hint_given = False

            if amount_attempts <= 2:
                amount_attempts += 1
                print(f"\nGuess {amount_attempts} of 3")

                if amount_attempts == 3:
                    print("This is your last attempt! ")

                if '.0' in graph_formula:
                    graph_formula = graph_formula.replace(".0", "")

                user_answer_thread = threading.Thread(target=num_check, args=("\nWhat is the equation of the graph? ",
                                                                                False, True,))
                if user_answer == "end_game":
                    end_game = True
                    break

                try:
                    users_result = answer_checker(graph_formula, user_answer)
                except TypeError:
                    continue

                if users_result == 'try again':
                    amount_attempts -= 1
                    continue

                if users_result is False:
                    print("Incorrect ❌")

                    if hint_given is not True:
                        give_hint = user_choice('Would you like a hint? ', yes_no_list)

                        if give_hint == "yes":
                            random_coordinate = find_random_coordinate(graph_formula)
                            print(f"The graph passes through: {random_coordinate}")

                else:
                    print(f"The equation of the graph is: {graph_formula}")
                    print(f"Your equation is: {user_answer}")
                    print()
                    print("Your answer is correct ✅✅")
                    questions_correct += 1
                    next_question = True

            elif amount_attempts == 3:
                print(f"You have unfortunately run out of attempts.\nThe equation of the graph was {graph_formula}. ")
                questions_wrong += 1
                next_question = True

            # outcome variable for game summary
            if users_result is True:
                outcome = f"Question {questions_attempted}: Correct in {amount_attempts} guesses!"
            else:
                outcome = f"Question{questions_attempted}: You ran out of guesses 🥲."
            game_summary.append(outcome)
            guess_array.append(amount_attempts)

    if not True and questions_attempted > 0:
        # Calculate quiz stats
        average_attempts = mean(guess_array)

        print()
        statement_generator("Quiz Stats", '*', '')
        print()
        print(f"Your average amount of guesses were: {average_attempts}")
        print()
        for game in game_summary:
            print(game)

if __name__ == '__main__':
    main()