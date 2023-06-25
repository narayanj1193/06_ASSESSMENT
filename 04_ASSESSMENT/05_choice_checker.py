def user_choice(question):

    # valid inputs:
    valid_difficulty = ["easy", "medium", "hard", "xxx"]

    # error code
    error = "Please choose a valid input."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_difficulty:
            if response == item[0] or response == item:
                return item

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


# Main routine
difficulty = ""
while difficulty != "xxx":

    # ask user for choice, check if its valid
    difficulty = user_choice("Choose your difficulty (Easy, Medium, or Hard): ")

    # print output
    if difficulty == "xxx":
        break
    else:
        print(difficulty)
