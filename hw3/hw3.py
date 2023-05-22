
#2
name = 'Anton'
surname = 'Chyrkov'

print('My name is ' + name )
print('My full name is {} {}'.format(name,surname))
print(f'Surname is "{surname}"')


#3
list = "Anton Chyrkov is an excellent employee"

split_list = list.split()
print(split_list)

upper_list= list.upper()
print('!!!', upper_list)

lower_list = list.lower()
print('!!!', lower_list)

capitalize_list = list.capitalize()
print('', capitalize_list)

find_list= list.find('Chyrkov')
print('', find_list)

#4

first_list = [1,2,3,4]   #a
print(first_list)

new_first_list = first_list.copy()    #b
print(new_first_list)

new_first_list.append(77)    #c
print(new_first_list)

new_first_list.insert(0,88)   #d
print(new_first_list)

new_first_list.insert(1,list)  #e1
print(new_first_list)

new_first_list.append(list) #e2
print(new_first_list)

pop_list = first_list.pop(3)  #f
print(pop_list)

list88=[1,4,8,9]
list88.remove(9)   #g
print(list88)

list88_del=list88.pop(0) #h
print(list88_del)

#5

list4=[1,2,3,4,5,6,7]
list5='london is the capital'

slice_list4 = list4[::-1]      #a
print(slice_list4)

slice_list5 = list5[::-1]     #b
print(slice_list5)

slice_list_c= list4[1:6:2]   #c
print(slice_list_c)

slice_list_5 = list5[0:4] #d
print(slice_list_5)




