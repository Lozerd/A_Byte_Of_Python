class SchoolMember:
    """Представляет любого человека в школе."""

    # __init__ - при передаче аргумента первый класс в кортеже принимает эти аргументы в функцию
    def __init__(self, name, age):
        self.name = name  # присваивание self.name аргумента
        self.age = age

        print('(Создан новый SchoolMember: {0})'.format(self.name))

    def tell(self):
        """Вывести информацию"""
        print('Имя: {0} Возраст: "{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):  # передача SchoolMember как аргумента для наследственности
    """Представляет преподавателя"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # используя наследственность, передаём инициализированные аргументы
        self.salary = salary  # передача дополнительной перменной
        print('(Создан новый Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)  # использование SchoolMember как "аргумента"
        print('Зарплата: "{0}"'.format(self.salary))


class Student(SchoolMember):
    """Представляет студента"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks  # ещё один доп аргумент (зарплата)
        print('(Создан новый Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()  # пустое место

members = [t, s]
for member in members:
    member.tell()
