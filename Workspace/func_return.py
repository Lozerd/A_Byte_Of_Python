def maximum(x, y):  # передаём параметры
    if x > y:  # x больше y?
        return x  # return возвращает какие-то вычисления сделанные в функции, по умолчанию None.none
    elif x == y:  # x равно y?
        return 'Числа равны'
    else:  # во всех остальных случаях (когда x меньше y)
        return y


print(maximum(2, 3))  # находит максимальное из двух чисел
# также можно использовать функцию max(), которая ищет наибольшее из переданных переменных