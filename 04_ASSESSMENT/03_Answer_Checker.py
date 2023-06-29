from sympy import symbols, Eq, solve

def answer_checker(user_answer, valid_answer):
    if user_answer == valid_answer.replace('**', '^'):
        print(user_answer, valid_answer)
        return True

    else:
        print(user_answer, valid_answer)
        return False

x = symbols('x')
y = symbols('y')

valid_answer = "y = x**2"
user_answer = input("What is the equation? ")

true = answer_checker(user_answer, valid_answer)

if true:
    print("Your answer is correct")

elif true == False:

