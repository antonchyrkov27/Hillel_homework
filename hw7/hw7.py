#1

def fibonacci_list(n,l):
    count = len(l)
    if len(l)<2:
        return []
    num1=l[count-2]
    num2=l[count-1]
    if (num1+num2)<n:
        l=l+[num1+num2]
        return fibonacci_list(n,l)
    else:
        return l
fibo=fibonacci_list(90,[1,1])
print(fibo)

#1.2

def fibonacci_list(n):
    if n<=0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence= fibonacci_list(n-1)
        sequence.append(sequence[-1]+sequence[-2])
        return sequence
n=25
fibonacci = fibonacci_list(n)
print(fibonacci)

#2

def sum_range(start,end):
    if start > end:
        start, end = end,start
    print(sum(range(start,end + 1)))
sum_range(28,10)

#3

def season(month):
    if month in list_winter:
        return 'winter'
    elif month in list_spring:
        return 'spring'
    elif month in list_summer:
        return 'summer'
    elif month in list_autumn:
        return 'autumn'
    else:
        return 'you need to read the fairy tale "12 Months"'

list_winter = [12,1,2]
list_spring = [3,4,5]
list_summer = [6,7,8]
list_autumn = [9,10,11]
print(season(0))

#4

def get_filtered(fibo):      #fibo - аналогичный список из первого задания
    for element in fibo:
        if element <5:
            print(element)
get_filtered(fibo)