import os
import time
from zipfile import *

# Директория которая будет преобразована в архив (также можно указать сам файл)
# "\\" для имён с пробелами e.g - " "
# меняешь имена папок, меняй и тут. Вылезает ошибка в виде не найденой папки. :-(
source = ['H:\_PyCharm\Projects\Workspace']

# Директория, в которой будет создан архив
target_dir = 'H:\_PyCharm\Projects\Backup'

# Дата создания архива
today = target_dir + os.sep + time.strftime("%Y-%m-%d")

# Время создание архива
now = time.strftime("%H-%M")

# Пользовательский ввод для имени архива, для уточнения изменений
comment = input('Введите имя архива --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    # target - конечное путь архива
    # comment имя архива + '.zip'
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

# Создание каталога даты создания архива
if not os.path.exists(today):
    os.mkdir(today)  # Создание каталога
    print('Каталог успешно создан', today)

# Создание переменной для команды в командной строке
# В случае ошибки создания архива, вывести print(zip_command), изменить путь
# перед проверкой состояния (не принципиально)
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

#print(zip_command)

# Вывод в консоль состояния выполнения архивации
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
