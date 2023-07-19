import sympy as sp
import fractions

from matplotlib import pyplot as plt

user_answer = 0

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
    eq1 = str(eq1)  # Convert eq1 to a string
    eq2 = str(eq2)  # Convert eq2 to a string

    # Replace '^' with '**' and remove any spaces. Python does not allow '^' for equation solving. Instead, it will
    # cause a SyntaxError
    if '^' in eq1:
        eq1 = eq1.replace('^', '**').replace(' ', '')

    if '^' in eq2:
        eq2 = eq2.replace('^', '**').replace(' ', '')

    if '(' in eq2 and '* (' not in eq2:
        # Insert a multiplication operator before opening parentheses if not already present
        eq2 = eq2.replace('(', '* (')

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


# Example usage:
computer = "x**2"
while True:
    num_check("Enter an equation: ", False)
    result = answer_checker(user_answer, computer)
    print(user_answer)

    if result is True:
        print('Your answer is correct')
    else:
        print("your answer is incorrect")


