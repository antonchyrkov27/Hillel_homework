import csv

with open('/Users/kateryna21/PycharmProjects/pythonProject1hillel/hw13/SampleCSVFile_11kb.csv' , 'r', encoding = 'utf-8', errors = 'ignore') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        #print(''.join(row)) #виводить список з  першої строки шапки таблиці?
