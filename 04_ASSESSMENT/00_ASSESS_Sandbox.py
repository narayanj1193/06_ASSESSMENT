from sympy import symbols, Eq, solve

# Value of 'x' for substitution
x_value = input("enter x: ")

x = symbols('x')
y = symbols('y')

equation = Eq(x**2, y)
solution = solve(equation.subs(x, x_value), y)

if solution:
    y_value = solution[0]
    print(f"When x = {x_value}, y = {y_value}")
else:
    print("No real solution exists for the given equation and x value.")
