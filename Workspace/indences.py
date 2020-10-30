word = input()
space = ' '
for i in range(1, 6):
    print("{0}{1}".format(space, word))
    space += space[0]
