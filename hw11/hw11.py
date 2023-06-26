from abc import abstractmethod,ABC
#1

class HW_11:
    @abstractmethod
    def abc_method(self):
        pass

#2

class ABCClass(ABC):
     @abstractmethod
     def abc_method(self):
        pass

#_abc_class = ABCClass()

#3

class ABCnew(ABC):
    @abstractmethod
    def abc_method(self):
        pass


class SecondClass(ABCClass,ABCnew):
    def abc_method(self):
        print('Hi')

s_class = SecondClass()

s_class.abc_method()

print(SecondClass.mro())