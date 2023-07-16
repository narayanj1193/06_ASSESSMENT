import random
import threading

import sympy as sp
import fractions
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean


user_equation_answer = ""  # Define user_equation_answer variable


# Function for choice checking. Compares users answer to items in valid_list.
def user_choice(question, valid_list):
    # Error code in case of user inputting something that is not in the valid_list.
    error = "Please choose a valid input."

    while True:
        user_response = input(question).lower()

        for item in valid_list:
            if user_response == item[0] or user_response == item:
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
    x_graph = np.linspace(-20, 20, 10000)
    y_graph = ''

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
            graph_formula = f"{k} * (x - {x_1}) * (x - {x_2})"

        else:
            b, c = vertex
            y_graph = k * (x_graph - b) ** 2 + c
            graph_formula = f"{k} (x - {b})^2 + {c}"

    if mode == "linear":

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

    graph_formula = str(graph_formula)
    type_graph = mode
    # returns the equation of the graph
    return x_graph, y_graph, graph_formula, type_graph


# Function that checks if an input is valid. If int_only is false it works well for equations, as it allows all sorts
# of inputs including floats and strings
def num_check(question, int_only=True):
    error = "Please enter a valid number or 'xxx' to exit."

    while True:
        response = input(question)

        if response == "xxx":
            return "end_game"

        elif response == "":
            if int_only:
                # If an empty string is entered and only integers are allowed, return the empty string
                return response
            else:
                print(error)
                continue

        elif response != "":
            if not int_only:
                response = str(response)

                # If non-integer values are allowed, check for special cases and evaluate the response
                if response.lower() == 'x' or ('x' in response.lower() and '+' in response or '-' in response):
                    # If the response contains 'x' with '+' or '-', return the response
                    return response

                if '^' in response and '2' in response:
                    # If the response contains '^' and '2', return the response
                    return response

                try:
                    number = eval(response)
                    if isinstance(number, float) or isinstance(number, int) or isinstance(number, fractions.Fraction):
                        # If the evaluated response is a float, integer, or fraction, return the number
                        return number
                    else:
                        print(error)
                        continue

                # error handling (errors happen alot 🥲)
                except (NameError, ZeroDivisionError, SyntaxError, TypeError, SyntaxWarning):
                    print(error)
                    continue

            else:
                try:
                    response = int(response)
                    if response < 1:
                        # If the response is an integer less than 1, print an error message
                        print(error)
                        continue

                except ValueError:
                    print(error)
                    continue
            return response


# Function that simplifies two equations and compares them to see if they are the same
def answer_checker(eq1, eq2):
    eq1 = str(eq1)
    eq2 = str(eq2)

    # Replace characters within the equations to valid alternatives, to ensure there are no errors.
    if '^' in eq1:
        eq1 = eq1.replace('^', '**').replace(' ', '')

    if '^' in eq2:
        eq2 = eq2.replace('^', '**').replace(' ', '')

    eq1 = eq1.replace('x', '120')
    eq2 = eq2.replace('x', '120')

    try:
        eq1_calculated = eval(eq1)
        eq2_calculated = eval(eq2)

        if eq1_calculated != eq2_calculated:
            return False  # Return False if equations are not the same
        else:
            return True  # Return True if equations are the same

    # error handling
    except TypeError:
        print('Invalid equation. Please try again.')
        return 'try again'


def find_random_coordinate(graph_formula):
    max_iterations = 1000  # Maximum number of iterations to avoid infinite loop
    iteration = 0

    while iteration < max_iterations:
        x = random.randint(-5, 5)  # Assuming x ranges from -5 to 5
        x_val = sp.symbols('x')
        y = sp.sympify(graph_formula).subs(x_val, x)  # Evaluate the equation with the random x value

        if isinstance(y, int):
            return x, y

        iteration += 1


    # If no integer value is found within the maximum iterations, search for a y value with one decimal place
    while True:
        x = random.randint(-5, 5)
        x_val = sp.symbols('x')

        y = sp.sympify(graph_formula).subs(x_val, x)  # Evaluate the equation with the random x value
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


def equation_checker(question, int_only):
    global user_equation_answer

    user_equation_answer = num_check(question, int_only)

    if user_equation_answer == "end_game":
        exit()

    plt.close()


def main():

    yes_no_list = ['yes', 'no']
    difficulty_list = ['easy', 'medium', 'hard']
    modes_list = ['linear', 'parabola', 'mixed']

    statement_generator('WELCOME TO GRAPHS QUIZ', '📈', '*', True)

    played_before = user_choice('Have you tried out this quiz before? ', yes_no_list)

    if played_before == 'no':
        instructions()

    how_many_questions = num_check("How many questions would you like to attempt? <enter> for continuous mode: ", True)
    if how_many_questions == "end_game":
        print("Thanks for playing! ")
        exit()

    graph_mode = user_choice("What mode would you like to play? (linear, parabola, or mixed): ", modes_list)
    quiz_difficulty = user_choice("What difficulty would you like to play at? (easy, medium, or hard): ",
                                  difficulty_list)

    end_game = False
    while not end_game:
        questions_attempted = 0
        questions_correct = 0
        questions_wrong = 0
        game_summary = []
        guess_array = []

        while how_many_questions == "" or questions_attempted < int(how_many_questions):
            questions_attempted += 1
            print()

            if how_many_questions == "":
                heading = f"Continuous Mode: Question {questions_attempted}"
            else:
                heading = f"Question: {questions_attempted} of {how_many_questions}"
            print(heading)

            # Generate graph details
            x, y, graph_formula, type_graph = graph_generator(quiz_difficulty, graph_mode)
            amount_guesses = 0
            next_question = False

            while not next_question:
                hint_given = False

                if amount_guesses == 3:
                    print(f"You have unfortunately run out of guesses. \nThe equation of the graph was {graph_formula}")
                    questions_wrong += 1
                    next_question = True

                elif amount_guesses <= 2:
                    amount_guesses += 1
                    print(f"\nGuess {amount_guesses} of 3")
                    print(f"{graph_formula}")
                    if amount_guesses == 3:
                        print("This is your last attempt!")

                    if '.0' in str(graph_formula):
                        graph_formula = graph_formula.replace('.0', '')

                    ask_equation_thread = threading.Thread(target=equation_checker,
                                                           args=("\nWhat is the equation of the graph? ", False), )
                    ask_equation_thread.start()

                    # Display the graph
                    display_graph(x, y, type_graph)

                    ask_equation_thread.join()

                    if user_equation_answer == 'end_game':
                        plt.close()
                        end_game = True
                        break

                    users_result = answer_checker(graph_formula, user_equation_answer)

                    if users_result == 'try again':
                        amount_guesses -= 1
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
                        print(f"Your equation is: {user_equation_answer}")
                        print()
                        print("Your answer is correct ✅✅")
                        questions_correct += 1
                        next_question = True

                    # outcome variable for game summary
                    if users_result is True:
                        outcome = f"Question {questions_attempted}: Correct in {amount_guesses}"
                    else:
                        outcome = f"Question {questions_attempted}: You ran out of guesses 💀😂"
                    game_summary.append(outcome)
                    guess_array.append(amount_guesses)

            if end_game:
                break

        # calculate quiz stats
        try:
            average_guesses = mean(guess_array)
        except ValueError:
            average_guesses = 0

        print()
        print("*** Quiz Stats ***")
        print()

        if questions_attempted == 1:
            print(f'You attempted {questions_attempted} question!! 😊')
        else:
            print(f'You attempted a total of {questions_attempted} questions!! 😊')

        print(f"AVG: {average_guesses}\t|\tWRONG: {questions_wrong}\t|\tCORRECT: {questions_correct}")
        print()
        for game in game_summary:
            print(game)
        exit()


main()
