import sympy as sp
import fractions


def num_check(question, int_only=True):
    # Error message
    error = "Please enter a valid number or 'xxx' to exit."

    while True:
        # Ask the question
        response = input(question)

        if response == "xxx":
            return response
        elif response == "":
            if int_only:
                return response
            else:
                print(error)
                continue

        elif response != "":
            if not int_only:

                try:

                    # Check if the number is a float or fraction
                    if isinstance(number, float) or isinstance(number, int) or isinstance(number, fractions.Fraction):
                        return number
                    else:
                        print(error)
                        continue

                except NameError:
                    print(error)
                    continue
                except ZeroDivisionError:
                    print("Error: Division by zero.")
                    continue
                except SyntaxError:
                    print("Error: Invalid expression.")
                    continue

            # if int_only is true
            else:
                try:
                    # Check that the response is an integer more than zero
                    response = int(response)

                    # if the amount is too low
                    if response < 1:
                        print(error)
                        continue

                except ValueError:
                    print(error)
                    continue
            return response


def compare_equations(eq1, eq2):
    eq1 = str(eq1)
    eq2 = str(eq2)

    if '^' in eq1:
        eq1 = eq1.replace('^', '**')

    if '^' in eq2:
        eq2 = eq2.replace('^', '**')

    x = sp.Symbol('x')
    correct = True

    for i in range(-20, 21):
        x_val = i
        y1 = sp.sympify(eq1).subs(x, x_val)
        y2 = sp.sympify(eq2).subs(x, x_val)

        if y1 != y2:
            correct = False
            break

    if correct:
        print("Your equation is correct")
    else:
        print("Your equation is incorrect")


# Example usage:
eq1 = "(x + 2) * (x - 3)"
while True:
    eq2 = num_check("Enter an equation: ", False)
    try:
        compare_equations(eq1, eq2)
        print(eq2)

    except sp.SympifyError:
        print("Invalid equation format. Please try again.")
