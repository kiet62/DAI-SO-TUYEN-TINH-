from sympy import Symbol, solve
x = Symbol('x')
bieuthuc1 = x + 3 - 5
result = solve(bieuthuc1)
print(result)



bieuthuc2 = x**2 + 3 - 5


nghiemx = solve(bieuthuc2)

print(f"nghiemx: {nghiemx}")
print(f"nghiemx[0]: {nghiemx[0]}")
print(f"nghiemx[1]: {nghiemx[1]}")