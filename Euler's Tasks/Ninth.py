import time
from memory_profiler import memory_usage  # Использование памяти

# Начано отсчета времени выполнения программы
start = time.time()


# Принимает два аргумента: длину цикла и сумму пифагоровой тройки
def piphaghor(t, need):
    # присваивает значения n в диапазоне
    for n in range(1, t + 1):
        # присваивает значения m в диапазоне
        for m in range(1, t + 1):
            # Формула для нахождения пифагоровой тройки
            primitive = (m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2)  # primitive[0] > 0
            p = primitive
            if p[0] > 0:
                # Проверка теоремы пифагора
                if p[0] ** 2 + p[1] ** 2 == p[2] ** 2:
                    #  Объявление переменной суммы списка
                    total = sum(list(p))
                    # Проверка равенства суммы списка и нужной суммы
                    if total == need:
                        print(primitive)


piphaghor(int(input('Введите длину цикла: ')), int(input('Введите нужную сумму пифагоровой тройки: ')))
# Вывод итогового времени выполнения программы
print(time.time() - start)
# Вывод количества используемой памяти
print(memory_usage())
