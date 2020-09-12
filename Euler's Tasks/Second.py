a, b = 0, 1
even = []
while a < 4000000:
    a, b = b, a + b
    if b % 2 == 0:
        even.append(b)
    else:
        continue
print(even)