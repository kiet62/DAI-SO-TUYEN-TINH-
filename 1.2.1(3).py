import itertools
tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20)))
for i in tap_sinh:
    print(i, end=" ")
ket_qua_zip=list(zip(range(4), range(7, 12), reversed(range(11) ) ) ) 
print("A  B  C")
for a, b, c in ket_qua_zip:
    print(f"{a:<2} {b:<2} {c:<2}")