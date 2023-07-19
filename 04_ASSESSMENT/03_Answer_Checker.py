from sympy import symbols


def answer_checker(user_answer, valid_answer):
    if user_answer.replace('**', '^') == valid_answer.replace('**', '^'):
        return True

    else:
        return False

x = symbols('x')
y = symbols('y')

valid_answer = "y = x**2"

while True:
    user_answer = input("What is the equation? ")

    true = answer_checker(user_answer, valid_answer)

    if true:
        print("Your answer is correct")

    elif not true:
        print("Your answer is incorrect ")

