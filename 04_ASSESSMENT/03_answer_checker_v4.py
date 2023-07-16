import sympy as sp
import fractions

from matplotlib import pyplot as plt


def num_check(question, int_only=True, graph_close=False):
    error = "Please enter a valid number or 'xxx' to exit."

    while True:
        global user_answer
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
                        return
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

    except TypeError:
        print('Invalid equation. Please try again.')
        return 'try again'


# Example usage:
eq1 = "(x + 2) * (x - 3)"
while True:
    eq2 = num_check("Enter an equation: ", False)
    try:
        result = answer_checker(eq1, eq2)
        print(eq2)
        print(result)

    except sp.SympifyError:
        print("Invalid equation format. Please try again.")
