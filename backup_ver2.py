import os
import time

# Директория которая будет преобразована в архив (также можно указать сам файл)
# "\\" для имён с пробелами e.g - " "
source = ['H:\PyCharm\Projects\Workspace']

# Директория, в которой будет создан архив
target_dir = 'H:\PyCharm\Projects\Workspace\Backup'

# Дата создания архива
today = target_dir + os.sep + time.strftime("%Y-%m-%d")

# Время создание архива
now = time.strftime("%H-%M")

# Создание каталога для даты создания архива
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

# Имя архива
target = today + os.sep + now + '.zip'

# Создание переменной для команды в командной строке
# В случае ошибки создания архива, вывести print(zip_command) перед проверкой состояния (не принципиально)
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# Вывод в консоль состояния выполнения архивации
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
