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

    plt.grid()

    # shows graph
    plt.show()


def graph_generator(difficulty, mode):
    graph_formula = 0
    x_graph = np.linspace(-20, 20, 10000)
    y_graph = ''
    types_of_graphs = ['linear', 'parabola']

    if mode == 'mixed':
        mode = random.choice(types_of_graphs)

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
            graph_formula = f"{k} * (x - {b})^2 + {c}"

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

            # if int_only is true
            else:
                try:
                    # Check that the response is an integer
                    response = int(response)

                    # if the amount is too low or too high
                    if response < 1 or response > 50:
                        print("Please enter an integer that is more than 1 and less than 50.")

                        continue

                except ValueError:
                    print(error)
                    continue
                return response


# Function that simplifies two equations and compares them to see if they are the same
def answer_checker(eq1, eq2):
    eq1 = str(eq1)  # Convert eq1 to a string
    eq2 = str(eq2)  # Convert eq2 to a string

    # Replace '^' with '**' and remove any spaces. Python does not allow '^' for equation solving. Instead, it will
    # cause a SyntaxError
    if '^' in eq1:
        eq1 = eq1.replace('^', '**').replace(' ', '')

    if '^' in eq2:
        eq2 = eq2.replace('^', '**').replace(' ', '')

    if '(' in eq1 and '* (' not in eq1:
        # Insert a multiplication operator before opening parentheses if not already present
        eq1 = eq1.replace('(', '* (')

    # swaps the symbols with a valid number so that it can be evaluated. 120 was chosen because of ascii code
    eq1 = eq1.replace('x', '120')  # Replace 'x' with '120' in eq1
    eq2 = eq2.replace('x', '120')  # Replace 'x' with '120' in eq2

    try:
        # evaluates the equations
        eq1_calculated = eval(eq1)
        eq2_calculated = eval(eq2)

        # if they are not the same then return false. else return true
        if eq1_calculated != eq2_calculated:
            return False  # Return False if equations are not the same
        else:
            return True  # Return True if equations are the same

    # error handling
    except (TypeError, SyntaxError):
        print('Invalid equation. Please try again.')  # Print error message if there is an invalid equation
        return 'try again'  # Return 'try again' so that the code will not continue with the guess


def find_random_coordinate(graph_formula):
    # if iterations reach max_iterations it continues to the next loop.
    # makes sure it does not run infinitely
    for i in range(1, 100):
        x = random.randint(-5, 5)  # Assuming x ranges from -5 to 5
        x_val = sp.symbols('x')  # Create a symbolic variable 'x' for substitution

        try:
            y = sp.sympify(graph_formula).subs(x_val, x)  # Evaluate the equation with the random x value
            if y == round(y, 0):
                return x, y  # Return the coordinates (x, y)
        except TypeError:
            pass

    # If no integer value is found within the maximum iterations, search for a y value with one decimal place
    while True:
        x = random.randint(-5, 5)  # Generate another random x value
        x_val = sp.symbols('x')  # Create a symbolic variable 'x' for substitution

        try:
            y = sp.sympify(graph_formula).subs(x_val, x)  # Evaluate the equation with the random x value
            y = round(y, 1)  # Round the y value to one decimal place
            return x, y  # Return the coordinates (x, y)

        # error handling
        except TypeError:
            pass


def statement_generator(statement, decoration, above_below, has_emoji=False):
    sides = decoration * 3  # Create a string of the decoration repeated three times
    statement = f"{sides} {statement} {sides}"  # Add the sides to the statement

    if has_emoji:
        top_bottom_length = len(statement) + (len(sides) * 2) + 2  # Calculate the length of the top and bottom
        # decorations
    else:
        top_bottom_length = len(statement)  # Calculate the length of the top and bottom decorations

    top_bottom = above_below * top_bottom_length  # Create a string of the above/below decoration repeated based on the
    # length

    print(top_bottom)  # Print the top decoration
    print(statement)  # Print the statement with decorations
    print(top_bottom)  # Print the bottom decoration

    return


def instructions():
    print("*** How to Play Graphs Quiz ***\n")

    # Sections with Numbers
    print("Your objective is to answer graph-related questions by providing the equation of the presented graph. \nYou "
          "have up to three attempts to guess the correct equation. Choose your preferred difficulty level (easy,\n "
          "medium, or hard) and graph mode (linear, parabola, or mixed) to customize your quiz experience. The game\n "
          "will keep track of your progress, including the number of questions attempted, correct answers,\n "
          "wrong answers, and your average number of guesses. Have fun and enjoy the challenge!\n")
    print("1. Objective")
    print("2. How to Answer")
    print("3. Difficulty Levels")
    print("4. Exiting the game\n")

    # Ask the user to select a section
    selected_section = input("If you would like to learn more enter the number of your desired section,"
                             " otherwise press <enter>: ")

    if selected_section == "":
        return

    # Display the selected section
    elif selected_section == "1":
        # Game Objective
        print("\nObjective:")
        print("Answer graph-related questions by providing the equation of the presented graph.\n")

    elif selected_section == "2":
        # How to Answer
        print("\nHow to Answer:")
        print("- You will be shown a graph, and you need to determine its equation.")
        print("- You have a maximum of three attempts per question.")
        print("- Enter your answer using a valid equation format.")
        print("- For linear equations please use the format 'a * x + y' - if it is not in this format, your equation "
              "will not be accepted")
        print("- For quadratic equations please use either 'k * (x-a)^2 + b' or 'k * (x-a)*(x-b)'. Reminder,"
              "if it is not in this format, it is likely your equation will not be accepted.")

        print("\bYou have a maximum of three attempts to guess the correct equation for each graph.\b\n")

    elif selected_section == "3":
        # Difficulty Levels
        print("\nDifficulty Levels:")
        print("- Easy: Graphs with simple features and integer coordinates.")
        print("- Medium: Graphs with more complex features and decimal coordinates.")
        print("- Hard: Challenging graphs with a wide range of features and fractional coordinates.\n")

    elif selected_section == "4":
        # Exiting the Game
        print("\nExiting the Game:")
        print("If you wish to quit the game at any time, enter 'xxx' as your answer to any question.")
        print("Make sure to close the graph before entering the exit code. \n")

    else:
        # Invalid input
        print("Invalid input. Please select a valid section number.")

    print("Enjoy the game and have fun! 📈💡\n")


# function is used as a response to limitations with threading
def equation_checker(question, int_only):
    global user_equation_answer
    # global variable is used to work around limitations with threading

    user_equation_answer = num_check(question, int_only)

    if user_equation_answer == "end_game":
        exit()

    # closes graph after receiving answer
    plt.close()


def main():
    yes_no_list = ['yes', 'no']  # List of choices for yes/no questions
    difficulty_list = ['easy', 'medium', 'hard']  # List of difficulty levels
    modes_list = ['linear', 'parabola', 'mixed']  # List of graph modes

    statement_generator('WELCOME TO GRAPHS QUIZ', '📈', '*', True)  # Generate and print a decorated welcome statement

    # Prompt for user input regarding previous quiz attempts
    played_before = user_choice('Have you tried out this quiz before? ', yes_no_list)

    if played_before == 'no':
        instructions()  # Display instructions if the user hasn't played before

    default_settings = user_choice("\nWould you like to play at default settings? ", yes_no_list)

    if default_settings == 'no':
        # asks user for the number of questions to attempt
        how_many_questions = num_check("How many questions would you like to attempt? <enter> for continuous mode: ",
                                       True)
        if how_many_questions == "end_game":
            print("Thanks for playing! ")
            exit()  # End the program if the user wants to quit

        # asks user for graph mode
        graph_mode = user_choice("What mode would you like to play? (linear, parabola, or mixed): ", modes_list)
        # asks user for the quiz difficulty level
        quiz_difficulty = user_choice("What difficulty would you like to play at? (easy, medium, or hard): ",
                                      difficulty_list)

    else:
        how_many_questions = 10
        graph_mode = 'mixed'
        quiz_difficulty = 'easy'

    end_game = False  # controls game loop
    while not end_game:
        questions_attempted = 0  # Counter for the number of questions attempted
        questions_correct = 0  # Counter for the number of questions answered correctly
        questions_wrong = 0  # Counter for the number of questions answered incorrectly
        game_summary = []  # List to store the summary of each question
        guess_array = []  # List to store the number of guesses for each question

        while how_many_questions == "" or questions_attempted < int(how_many_questions):
            questions_attempted += 1  # Increment the number of questions attempted
            print()

            if how_many_questions == "":
                # Generate the heading for continuous mode
                heading = f"Continuous Mode: Question {questions_attempted}"
            else:
                # Generate the heading for regular mode
                heading = f"Question: {questions_attempted} of {how_many_questions}"
            print(heading)

            # Generate the graph details based on the quiz difficulty and graph mode
            x, y, graph_formula, type_graph = graph_generator(quiz_difficulty, graph_mode)
            # Counter for the number of guesses for the current question
            amount_guesses = 0

            next_question = False
            while not next_question:

                if amount_guesses == 3:
                    print(f"You have unfortunately run out of guesses. \nThe equation of the graph was {graph_formula}")
                    questions_wrong += 1  # Increment the number of questions answered incorrectly
                    next_question = True  # Move to the next question

                elif amount_guesses <= 2:
                    amount_guesses += 1  # Increment the number of guesses
                    print(f"\nGuess {amount_guesses} of 3")

                    # print(graph_formula) - testing purposes

                    if amount_guesses == 3:
                        print("This is your last attempt!")

                    if '.0' in str(graph_formula):
                        # Remove decimal point if it exists in the graph formula
                        graph_formula = graph_formula.replace('.0', '')

                        # assigns thread so that question can be asked while the graph display function is running
                    ask_equation_thread = threading.Thread(target=equation_checker,
                                                           args=("\nWhat is the equation of the graph? ", False), )
                    ask_equation_thread.start()  # Start a new thread to prompt for the equation input

                    # Display the graph
                    display_graph(x, y, type_graph)

                    # Wait for the equation input thread to complete
                    ask_equation_thread.join()

                    if user_equation_answer == 'end_game':
                        plt.close()
                        end_game = True
                        break

                    # Check the user's answer against the graph formula
                    users_result = answer_checker(graph_formula, user_equation_answer)

                    if users_result == 'try again':
                        amount_guesses -= 1
                        continue

                    if users_result is False:
                        print("Incorrect ❌")

                        if amount_guesses <= 2:
                            give_hint = user_choice('Would you like a hint? ', yes_no_list)

                            if give_hint == "yes":
                                random_coordinate = find_random_coordinate(graph_formula)
                                print(f"The graph passes through: {random_coordinate}")

                    else:
                        print(f"The equation of the graph is: {graph_formula}")
                        print(f"Your equation is: {user_equation_answer}")
                        print()
                        print("Your answer is correct ✅✅")
                        questions_correct += 1  # Increment the number of questions answered correctly
                        next_question = True  # Move to the next question

                    outcome = ''
                    # outcome variable for game summary
                    if users_result is True:
                        outcome = f"Question {questions_attempted}: Correct in {amount_guesses}"
                    elif users_result is False and amount_guesses == 2:
                        outcome = f"Question {questions_attempted}: You ran out of guesses 💀😂"
                    game_summary.append(outcome)  # Append the outcome to the game summary list
                    guess_array.append(amount_guesses)  # Append the number of guesses to the guess array list

            if end_game:
                break  # Exit the game loop if the user wants to quit

        # calculate quiz stats
        try:
            average_guesses = mean(guess_array)  # Calculate the average number of guesses
            average_guesses = round(average_guesses, 2)
        except ValueError:
            average_guesses = 0  # Set average guesses to 0 if there are no guesses

        print()
        statement_generator("Quiz Stats", "*", '')  # Generate and print a decorated statement for quiz stats
        print()

        if questions_attempted == 1:
            print(f'You attempted {questions_attempted} question!! 😊')
        else:
            print(f'You attempted a total of {questions_attempted} questions!! 😊')

        print(f"AVG: {average_guesses}\t|\tWRONG: {questions_wrong}\t|\tCORRECT: {questions_correct}")
        print()
        for game in game_summary:
            print(game)  # Print the summary of each question
        exit()  # End the program


main()  # run the program.
