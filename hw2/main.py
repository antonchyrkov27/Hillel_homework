#1
zminna_a = 'dnipro' #a
zminna_b = 'Dnipro' #b
zminna_b1 = 'DniprO' #b
zminna_c = 'Dnipro_Dnipro' #c
zminna_d = 50 #d
zminna_e = '_Dnipro' #e
ZMINNA_F= 'RASHKA PIDORASHKA' #f
Ukraine = "Ukr_"    #g
zminna_aa = 10

#2
print(zminna_aa + zminna_d) #a
print(zminna_aa - zminna_d)  #b
print(zminna_aa / zminna_d) #c
print(zminna_aa * zminna_d) #d
print(zminna_aa ** zminna_aa) #e
print(zminna_aa // zminna_d) #f
print(zminna_aa % zminna_d) #g
print(zminna_d + zminna_d - zminna_aa)  #h

#3
zminna_3=100

zminna_3+=77
print(zminna_3)  #a

zminna_3-=10
print(zminna_3) #b

zminna_3 /=2
print(zminna_3) #c

zminna_3 *=2
print(zminna_3) #d

zminna_3 **=2
print(zminna_3) #e

zminna_3 //=2
print(zminna_3) #f

zminna_3 %=100
print(zminna_3) #g

#4

zmin4_1=10
zmin4_2=20

if zmin4_1<zmin4_2:
    print('super')
else:
    print("pomylka") #a #b

if zmin4_1 == 0:
    result= zmin4_2 / zmin4_1
    print('pomylka "/0"')
elif zmin4_2 == 0:
    result = zmin4_1 / zmin4_2
    print('pomylka "/0"')
else:
    print('OK'); #c


if zmin4_1 == zmin4_2:
    print('zmin4_1=zmin4_2',sep=' ')
elif zmin4_1 != zmin4_2:
    print('zmin4_1','zmin4_1',sep=' NO= ') #d #e


age = 18

if age < 18:
    print('go to school')
elif age >= 18 and age<27:
    print('go to university')
elif age >=27 and age <60:
    print('go to army')
else:
    print('You are pensioner') #f