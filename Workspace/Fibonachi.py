import time


# четные цифры фибоначчи, со входом их количества
def fib(x):
    a, b = 0, 1
    while x:
        a, b = b, a + b
        if a % 2 == 0:
            x -= 1
            print(a)


start_time = time.time()
fib(100)
print(f'\n{time.time() - start_time} seconds')

# n = int(input())
#
#
# def fibonachi(n):
#     a, b = 0, 1
#     while a < n:
#         print(a)
#         a, b = b, a + b
#
#
# print(fibonachi(n))
