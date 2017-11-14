angka1, angka2 = 0, 1
total = 0
while True:
    angka1, angka2 = angka2, angka1 + angka2
    if cur >= 4000000:
        break
    if angka2 % 2 == 0:
        total += angka2
print(total)
