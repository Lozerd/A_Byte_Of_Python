first = int(input())
second = int(input())


def gcd(n, k):
    if k == 0:
        return n
    return gcd(k, n % k)


print(gcd(first, second))
