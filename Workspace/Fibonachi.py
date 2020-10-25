n = int(input())


def fibonachi(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


print(fibonachi(n))

