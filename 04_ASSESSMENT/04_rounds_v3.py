import fractions
from sympy import symbols


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
                x = symbols('x')
                y = symbols('y')

                try:
                    # Attempt to parse the response as a number
                    number = eval(response.replace('x', '120').replace('y', '121'))

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


# Main routine
questions_attempted = 0
instruction = "Enter a number"

# Ask the user for the number of questions or enter for continuous mode
questions = num_check("How many questions would you like to answer? <enter> for continuous mode: ", True)

while questions != "xxx":

    if questions_attempted == questions:
        break

    # Questions Heading
    print()
    if questions == "":
        heading = f"Continuous Mode: Question {questions_attempted + 1}"
    else:
        heading = f"Question {questions_attempted + 1} of {questions}"

    print(heading)
    choose = num_check(f"{instruction} or 'xxx' to end: ", False)

    if choose == "xxx":
        break

    # Rest of the loop
    print(f"You chose {choose}")
    questions_attempted += 1

print("Thanks for playing!")
