from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

s = x*y + y*x
print(s)

p = x*(x + 2*x)
print(p)