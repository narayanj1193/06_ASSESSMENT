import random

# Functions at the top
def statement_generator(statement, decoration, above_below):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = above_below * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine

questions_answered = 0
questions_attempted = 0
questions_incorrect = 0

amount_guesses = 0
guess = 0

question_summary = []

# creates a decorative statement, adds aesthetic to program, welcomes users

statement_generator("Welcome to Graphs Quiz", "!", "*")

# ask user if they have played before, if not, display instructions
played_before = yes_no_checker("Have you tried this quiz before? ")
if played_before == "no":
    instructions()

# asks user if they would like to do a quiz on types of graphs
mode = choice_checker("Would you like to be quizzed on Linear graphs, Parabola graphs, or a mix? ")

# asks for rounds
rounds = num_check("How many questions would you like to answer? <enter> "
                   "for continuous mode: ")

if rounds = "":
    rounds_mode = "continuous"

end_game = "no"
while end_game == "no":

    if mode != "continuous" and questions_attempted == rounds:
        break

    questions_attempted += 1

    # Question heading
    print()

    if rounds_mode == "continuous":
        heading = f"Continuous Mode: {questions_attempted}"

    else:
        heading = f"Round {questions_attempted} of {rounds}"
    print(heading)

    # Generate graph according to mode
    while amount_guesses <= 3:

        if mode == "linear":
            # linear_generator()
            pass
        if mode == "Parabola":
            parabola_generator()

        if mode == "mixed":
            mixed_choose = random.randint(0, 1)

            if mixed_choose == "0":
                parabola_generator()

            else:
                linear_generator()

