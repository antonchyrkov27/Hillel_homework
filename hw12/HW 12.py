#1

with open ('hw12.txt', 'w') as file:
    file.write("first\n")

#2

with open('hw12.txt', 'r') as file:
    contents = file.read()
    print(contents)

#3

f = open('hw12.txt', mode='a')
f.write('second\n')
f.close()

f= open('hw12.txt', mode='r')
print(f.read())

#4

with open('hw12.txt', 'r') as file:
    lines= file.readlines()
    for line in lines:
        print(line)

#5

lines =[]
while True:
    line = input(">")
    if line == 'exit':
        break
    lines.append(line + '\n')

with open('input__.txt', 'w' ) as f:
    f.writelines(lines)