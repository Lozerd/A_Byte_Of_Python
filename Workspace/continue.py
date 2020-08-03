while True:
    s = input('Enter some text: ')

    if s == 'exit':
        break
    if len(s) < 3:
        print('Your sentence is too small')
        continue
    print('Your sentence has right length')
