def name(a, s): ...


class Human:
    # атрибут уровня класса
    head = 1

    # функция,метод, магические методы,
    # конструктор класса Human
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # метод
    def runn(self):
        print(f'{self.name} is runn')

    # магический метод
    # внедрять привычные функции в наш класс
    def __str__(self):
        return f'{self.name} {self.age} {self.head}'

    # def __len__(self):
    #     return len(self)

a = Human('Beka', 19)
a.runn()
a.age=18
a.name='1'
a.head=0
print(a.name, a.age, a.head)
a.runn()
d=Human('beka',10)
print(len(d.name))

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)
c=Point(1,1,1,1,1,1,1)
print(len(c))