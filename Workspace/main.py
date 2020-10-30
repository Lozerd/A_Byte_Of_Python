# ctrl+alt+L, PEP8 auto-fix
import random as rand

arr = []

for i in range(1, 100, 1):
    x = i
    arr.append(x)
y = rand.choice(arr) + 1
print("Я ебал тебя", y, end='')

if y >= 11 and y <= 19:
    print(' раз')
elif y % 10 == 1:
    print(' раз')
elif y % 10 >= 2 and y % 10 <= 4:
    print(' раза')
else:
    print(' раз')

# y = arr[-1]
# if y % 10 == 2 == 3:
#     u = 'раза'
#     print(u)

# x = rand.randrange(1, 365, 1)

# get

# arr = list('список')
# print(arr)
# c = [c * 3 for c in 'list']
# print(c)
