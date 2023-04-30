import sympy
from sympy import symbols
from sympy.abc import y
from sympy.solvers import solve
from sympy import *

x = symbols('x')

# Put the equation here
eq = x - 2
print("x = ", solve(eq,x))

eq = 2*x + 1
print("x = ", solve(eq,x))

# Another way

eq = input("Enter equation: 0 = ")
print("x = ", solve(eq,x))

## Another

solution = solve(eq, x)
print("x =", solution[0])


# if I have more the two ways to get the equation
# eq = 2*x - 4

eq = input('Enter equation: 0 = ')
solution = solve(eq,x)
for s in solution:
    print("x = ", s)

## More

var('x y')

# First equation set equal to zero, ready to solve
first = 2*x + 10

# Sympy syntax for equation equal to zero, ready to factor
eql = Eq(first, 0)
# eql = Eq(first, y)


# Sympy solve for x
sol = solve(eql, x)

# Show factored results
print("x = ", sol[0])

# More..

var('x y')

# Equation set equal to zero, ready to solve
eq = 2*x + 10 * y + 3
# eq = x**3 - 2*x**2 - 5*x + 6

sympy.factor(eq)
