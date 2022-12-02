# def printe(name):
#     print(f'{name} its may name')
#
# printe('Beka')
# printe('Bakyt')

#
class Human:
    # атрибут уровня класса
    head=1
    hand=2
    # конструктор класса,метод класса,функция
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # функция внутри класса называется метод
    def printt(self):
        print(self.name, 'is runn')

beka=Human('beka',19)
beka.printt()
hum2=Human('Nurbek',20)
print(hum2.printt(),hum2.age)
# # обьект класса

# human=Human('Beka',19)
# print(human.name,human.age)
# print(human.head)
# human2=Human('jumabek',20)
# print(human2.name,human2.age)
# print(human2.head)
#
#
#
class Car:
    motor=1
    def __init__(self,model,age,mark):
        self.model=model
        self.age=age
        self.mark=mark
    def __str__(self):
        return f'model is {self.model}\n' \
               f'age is {self.age}\n' \
               f'mark is {self.mark}'

car1=Car('bmw',2010,'x5')
print(car1)
print()
car2=Car('mersedes',2021,'S')
print(car2)
