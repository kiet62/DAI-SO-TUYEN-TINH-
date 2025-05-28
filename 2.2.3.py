from sympy import Symbol, simplify, sin, cos

x = Symbol('x')
y = Symbol('y')

bieuthuc = x*x - x*y + y*y
print(bieuthuc)

bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print(bieuthuc_moi)

dongian = simplify(bieuthuc_moi)
print(dongian)

x = Symbol('x')
y = Symbol('y')

bt = sin(x)*cos(y) + cos(x)*sin(y)
print(bt)

bt_moi = simplify(bt)
print(bt_moi)