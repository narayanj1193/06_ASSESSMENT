def num_check(question):
    # error code
    error = "Please enter an integer that is more than zero (or <enter> for continuous mode)"

    while True:
        # ask the Question
        response = input(question)

        if response == "xxx":
            return response

        elif response != "":
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
instruction = "enter a number"

# ask user for # of Questions, <enter> for continuous mode
questions = num_check("How many questions would you like to answer? <enter> for continuous mode: ")

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
    choose = input(f"{instruction} or 'xxx' to end: ")

    if choose == "xxx":
        break

    # Rest of loop
    print(f"You chose {choose}")
    questions_attempted += 1

print("Thanks for playing!")
