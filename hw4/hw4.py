#1
import copy

string_a='London is the capital of Great Britain'
print(string_a)

string_b='''
London is the capital of Greate Britain
   Berlin is the capital of Germany
     Kyiv is the capital of Ukraine
'''
print(string_b)

string_b1 = 'London is the capital of Greate Britain\nBerlin is the capital of Germany\nKyiv is the capital of Ukraine'
print(string_b1)

string_c=r'London is\n the capital of Greate Britain'
print(string_c)

string_d='dlfnslfgjsdjflksdjlkfsjdklfskldfjlksjgkvnblnlb' \
         'ksdjlfkjsdlkfjsldkjflskdjflsdjflksjlfkksfjlskjf' \
         'klsdjflksdjflksjdflksjdlfksjdkfjsldfjsldkfj'
print(string_d)

#2

listA=[1,2,3,4,5]
print('ListA id: {}'.format(id(listA)))
print(listA)                                #a

listB= listA
print('ListB id: {}'.format(id(listB)))
print(listB)                                #b

shallow_listA = listA.copy()
print('shallow_listA id:{}'.format(id(shallow_listA)))
print(shallow_listA)                        #c

deep_listA= copy.deepcopy(listA)
print('deep_listA id:{}'.format(id(deep_listA)))
print(deep_listA)                           #d

print(shallow_listA, deep_listA) #e

shallow_listA.append(88)
print(shallow_listA)
print(shallow_listA, deep_listA)  #f

#3

dictionary={}
new_dictionary= dict()   #a

new_dict = {
    'name':'Anton',
    'surname' : 'Chyrkov',
    'location':'Dnipro'
}
print(new_dict)          #b

new_dict['age'] = '29'
print(new_dict['age'])
print(new_dict)          #c

update_dict = {
    'drive category':'b',
    'citizen':'ukr'
}
new_dict.update(update_dict)
print(new_dict)          #d

pop_new_dict = new_dict.pop('drive category')
print('pop element {}',format(pop_new_dict))
print(new_dict)             #e

popitem_new_dict= new_dict.popitem()
print(popitem_new_dict)
print(new_dict)            #f

deep_copy_new_dict = copy.deepcopy(new_dict)
print('id deep copy :', format(id(deep_copy_new_dict)))    #g

new_dict['car'] = 'bmw'
print(new_dict['car'])
dict_values = new_dict.values()
print(dict_values)      #h

list_of_keys = new_dict.keys()
print(list_of_keys)     #i

list_of_values = new_dict.values()
print(list_of_values)    #j

#4

ternary1 = 'check your car' if 'bmw' in list_of_values else 'ok'
print(ternary1)        #1

ternary2 = 'You are very younger' if 'age' == '30' in new_dict else 'hello'
print(ternary2)

if 'age'=='30' in new_dict:
    print('Helo')
else:
    print('You are very younger')  #2


#5
list5 = ([new_dict],[listA],[list_of_values])
print(list5)    #a

#1,2

list5 = ([new_dict],[listA],[list_of_values])
print(list5)   #b


list_drive=['a','b','c','d']
dict_c = {
    'open_drive':[list_drive]
}
print('You can open drive category :', format(dict_c))   #c

deep_list_c = dict_c['open_drive'].copy()
print(deep_list_c)                #d

#6

a= 1
b= 2
result=a&b
print(result)
result_2 = b&b
print(result_2)         #1

#c= 'an'
#d='ch'
#result3=c&d
#result4=c&c
#print(result3)
#result(result4)

resulr_or= a|b
result_xor=a^b
result_not_a=~a
result_not_b=~b

print(resulr_or)
print(result_xor)
print(result_not_a)
print(result_not_b)     #b

result_1bit=a<<1
result_2bit=a<<2
result_3bit=a<<3

print(result_1bit)
print(result_2bit)
print(result_3bit)    #c

result_1bit_right = a>>1
result_2bit_right = a>>2
result_3bit_right = a>>3

print(result_1bit_right)
print(result_2bit_right)
print(result_3bit_right)   #d











