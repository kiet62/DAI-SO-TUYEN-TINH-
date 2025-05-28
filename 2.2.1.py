from sympy import Symbol, factor, expand

x = Symbol('x')
y = Symbol('y')

bieuthuc_factor = x**3 - y**3
print(factor(bieuthuc_factor))

bieuthuc_expand = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc_expand))