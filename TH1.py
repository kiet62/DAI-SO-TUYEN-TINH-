from sympy import Symbol

x = Symbol('x')
y = Symbol('y')


bieuthuc = x**2 - x*y + y**2


giatri = bieuthuc.subs({x: 3, y: x})
print(giatri)