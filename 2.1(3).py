from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

p = (x + 2)*(y + 3)
print(p)

p = (x + 2)*(y + 3) + (x + 2)*(x - 3)
print(p)