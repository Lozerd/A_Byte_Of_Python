<<<<<<< HEAD
def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


total(10, 1, 2, 3, 4, extra_number=50)
# total(10, 1, 2, 3)
# вызовет ошибку, т.к. не указан аргумент по умолчанию extra_number
=======
x = 50
def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)
func(x)
print('x по-прежнему', x)
>>>>>>> 58234a5e5b6c4f344b59ea1e73f9d196bde5f7fe
