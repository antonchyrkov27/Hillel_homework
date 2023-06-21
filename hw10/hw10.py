 #1

class Car:
     def wheels(self):
         print('4 wheels')
     def mode_of_transport(self):
         print('Private usage')

class Bus:
    def wheels(self):
        print('8 wheels')

    def mode_of_transport(self):
        print('Public usage')

car=Car()
bus=Bus()

object=[car,bus]
for obj in object:
    obj.wheels()
    obj.mode_of_transport()


#2

class Venicle:
    def desc(self):
        print('Transport')
    def wheels(self):
        print('Kolesa')

class Bmw(Venicle):
    def desc(self):
        print('BMW is auto')
    def wheels(self):
        print('expensive kolesa')

class Audi(Venicle):
    def desc(self):
        print('Audi is auto')
    def wheels(self):
        print('same expensive kolesa')

venicle = Venicle()
venicle.desc()
venicle.wheels()

car_bmw=Bmw()
car_bmw.desc()
car_bmw.wheels()

car_audi = Audi()
car_audi.desc()
car_audi.wheels()

#Encapsulation

class encaps:
    def __init__(self, _a, __a):
        self._a = _a
        self.__a = __a

_a, __a = 10, 20
obj = encaps(_a,__a)
print(obj._a)
print(obj._encaps__a)


