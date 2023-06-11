#1

class PlaceHolder:
    pass

#2#3

class HW:
    class_s_name = 'Chyrkov'       #3
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(f'My name is {self.name}')

    @staticmethod
    def class_s_name(cls):
        print(HW.class_s_name)

a = HW('Anton')
print(a)
print(a.print_name())


#3

class MainHW(HW):
    def __init__(self,name,number):
        HW.__init__(self,name)
        self.number = number
    def number(self):
        return f'MAin HW is # {self,number}'

x = MainHW('Main HW is', 'HW')

print(x.number)
print(x.name)
