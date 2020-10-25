# (c1, c2, c3) = map(int, input().split())
#
# middle from a
#
# (c1, c2, c3, c4) = map(int, input().split())
# arr = ['c1', 'c2', 'c3', 'c4']
# middle = (c1+c2+c3+c4)/len(arr)
# print(middle)
#
# The greatest of 3 numbers using 2 operations
#
# a = int(input())
# b = int(input())
# c = int(input())
# sum = []
# sum.append(a+b*c)
# sum.append(a*b+c)
# sum.append(a*b*c)
# sum.append((a+b)*c)
# print(max(sum))
#
# Electronic Clock
#
# t1 = int(input())
# minutes = t1 % 60
# while t1 < 1440:
#     t1 //= 60
# else:
#     t1 -= 1440
# print(t1, minutes)
#
# Multiplicity of the given number (% 6)
#
# number = int(input())
# print(number % 6 == 0) :True (30)
#
# Rectangular triangle
#
# a=int(input())
# b=int(input())
# c=int(input())
#
# print(a*a+b*b==c*c and (a+b)>c and (b+c)>a and (a+c)>b)
#
# Time library
#
# from time import gmtime, strftime
#
#
# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')
# age = int(input('Enter your age: '))
# # time = time.localtime()
# year = strftime("%Y-%m-%d", gmtime())
# time = strftime("%H:%M:%S", gmtime())
#
# print('In the {0} at {1} (Greenwich time) - {2} {3} is {4}'.format(year, time, first_name, last_name, 18))
#
# Guessing game
#
# #number = 23
# running = True
#
# while running:
#     guess = int(input('Введите целое число : '))
#
#     if guess == number:
#         print('Поздравляю, вы угадали.')
#         running = False  # это останавливает цикл while
#     elif guess < number:
#         print('Нет, загаданное число немного больше этого.')
#     else:
#         print('Нет, загаданное число немного меньше этого.')
# else:
#     print('Цикл while закончен.')
# # Здесь можете выполнить всё что вам ещё нужно
# print('Завершение.')
#
# fibonachi odd
#
# def fibonachi(last):
#     numbers = [1, 2]
#     i = 1
#     while True:
#         numbers.append(numbers[i] + numbers[i - 1])
#         if numbers[i + 1] > int(last):
#             del numbers[i + 1]  # or numbers.pop()
#             break
#         i += 1
#     print("Колличество элементов: ", len(numbers))
#     print("Сумма все четных чисел: ", [x for x in numbers if x % 2 == 0])
#
#
# fibonachi(4000000)
#
# #List with user input
#
# def array(n):
#     arr =[]
#     for i in range (n):
#         arr.append(input('Введите элемент: '))
#         print(arr)
#     # arr = [input('Введите элемент: ') for i in range(n)]
#     # print(arr)
#     else:
#         print('Программа закрывается')
#         input('Напишите выход: ')
#
# array(int(input('Введите длину списка: ')))
#
