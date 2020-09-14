A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))


def Summa(A, B):
    summ = 0
    while A <= B:
        summ += A
        A += 1
    return summ


print(Summa(A, B))
print()
