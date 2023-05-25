#1

first_tuple=(1,2,3,4,5,6)  #a
print(first_tuple)  #b

#2

set1= {1,2,3,4,5,6,7}
print(set1)              #a

set2={5,6,7,8,9,10,11}
print(set2)              #b

set1.add(0)
print(set1)     #c

set3= set1.intersection(set2)
print(set3)             #d

set4 = set1.difference(set2)
print(set4)          #e

set5 = set1.symmetric_difference(set2)
print(set5)            #f





