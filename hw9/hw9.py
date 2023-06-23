#1

lam1 = lambda x, y=100: print(x*y)
lam1('2',200)

#2

lam2 = lambda x, y : print(max(x, y))
lam2(33, 11)

#3

lam3 = (lambda : 10)()
print(lam3)

#decorators

def make_bold(fn):
    def wrapped():
        return '<b>' + fn() + '</b'
    return wrapped

def make_italic(fn):
    def wrapped():
        return '<i>' + fn() + '</i>'
    return wrapped

def make_underline(fn):
    def wrapped():
        return '<u>' + fn() + '</u>'
    return wrapped

@make_bold
@make_italic
@make_underline
def hello_world():
    return 'hello_world'

print(hello_world())

#list comprehension

list1 = [44,54,74,104]
list2= [i+6 for i in list1]
print(list2)

list3 = [2,4,6,8,10,12,14]
list4 = [i*i for i in list3]
print(list4)

car_dict = {'sedan':1500,
            'SUV': 2000,
            'Pickup':2500,
            'Minivan':1600,
            'Van':2400,
            'Semi':13600,
            'Bicycle': 7,
            'Motocucle':110
            }
list5 = [key.upper() for key,value in car_dict.items() if value<5000]
print(list5)