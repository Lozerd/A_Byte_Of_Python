n = list(map(int, list(input())))
print('Счастливый' if sum(n[:3]) == sum(n[3:]) else 'Обычный')

# n = input()
#
# k = sum([int(n[0]), int(n[1]), int(n[2])])
# l = sum([int(n[3]), int(n[4]), int(n[5])])
#
# if k == l:
#     print("Счастливый")
# else:
#     print("Обычный")