poem = """\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Python"""

file = open('text/poem.txt', 'w')
file.write(poem)
file.close()

file = open('text/poem.txt', 'r')

while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line, end='')

file.close()
