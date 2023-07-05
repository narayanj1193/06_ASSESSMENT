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
                # Check if the response is 'x' or an equation containing 'x'
                if response.lower() == 'x' or ('x' in response.lower() and '+' in response or '-' in response):
                    return response

                try:
                    # Attempt to parse the response as a number
                    number = eval(response)

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
                    # Return the response as a string if it's a valid equation
                    return response

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



def answer_checker(eq1, eq2):
    try:
        if '^' in eq1:
            eq1 = eq1.replace('^', '**').replace(' ', '')

        if '^' in eq2:
            eq2 = eq2.replace('^', '**').replace(' ', '')

    except TypeError:
        print("Invalid equation. Please try again.")
        return

    x = sp.symbols('x')
    correct = True

    for i in range(-20, 21):
        x_val = i
        try:
            # Evaluate the equations
            y1 = eval(eq1)
            y2 = eval(eq2)

            if y1 != y2:
                correct = False
                break

        except TypeError:
            print("Invalid equation. Please try again.")
            return

    return correct

# Example usage:
eq1 = 'x^2'
while True:
    eq2 = num_check("Enter an equation: ", False)
    answer_checker(eq1, eq2)
    print(eq2)

