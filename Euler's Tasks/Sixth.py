def sum_of_squares():
    result = 0
    for square in range(1, 101):
        result += square ** 2
    return result


def square_sum():
    summa = 0
    for numbers in range(1, 101):
        summa += numbers
    summa **= 2
    return summa


print(square_sum() - sum_of_squares())

