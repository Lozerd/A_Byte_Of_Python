def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


total(10, 1, 2, 3, 4, extra_number=50)
# total(10, 1, 2, 3)
# вызовет ошибку, т.к. не указан аргумент по умолчанию extra_number
