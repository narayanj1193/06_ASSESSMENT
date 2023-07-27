def instructions():
    print("*** How to Play ***")
    print()
    print("These are the rules:")
    print()
    return ""

def user_choice(question, valid_list):

    # error code
    error = "Please choose a valid input."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


# Main routine
yes_no_list = ['yes', 'no']

while True:
    played_before = user_choice("Have you played this game before? ", yes_no_list)

    if played_before == "no":
        instructions()
    else:
        print("Program Continues")

    print()
