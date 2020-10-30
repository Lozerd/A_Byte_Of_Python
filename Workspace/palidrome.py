def reverse(text):
    return text[::-1]


def is_palidrome(text):
    return text == reverse(text)


searched_word = input("Введите слово на проверку: ")

if is_palidrome(searched_word):
    print('Слово {0} является палидромом'.format(searched_word))
else:
    print('Слово {0} не являетя палидромом'.format(searched_word))
