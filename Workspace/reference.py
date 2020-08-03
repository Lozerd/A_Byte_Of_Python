print('Просто присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist  # mylist - лишь ещё одно имя, указывающее на тот же объект!

del shoplist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)
# Два этих списка указывают на один объект, удаляя элементы они пропадают у всех списков

print('Копирование при помощи полной вырезки')
mylist = shoplist[:]  # Создаём копию путём полной вырезки
del mylist[0]

print('shoplist', shoplist)
print('mylist', mylist)
# Списки теперь разные