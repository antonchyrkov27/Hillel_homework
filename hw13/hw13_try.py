#aryfmetyka

try:
  a= 10
  b= 0
  result = a/b
  print('Result:' ,result)
except ZeroDivisionError:
  print('err /0' )
except Exception as e:
  print('err', str(e))


#kolekcija

my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    print(my_list[10])
    print(my_dict['d'])
except IndexError:
    print("Помилка індекс: Елемент не знайдено у списку")
except KeyError:
    print("Помилка ключ: Ключ не знайдений у словнику")
except Exception as e:
    print("Інша помилка:", str(e))
