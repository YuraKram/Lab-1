import csv

count = 0
f = open('result.txt', 'a')
with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for _ in table:
        count += 1
if '1 задание\n' not in open('result.txt', 'r'):  # проверка файла на повтор
    f.write('1 задание\n' + str(count - 1) + ' записей.\n')  # count - 1 т.к. 1 строка - названия столбцов таблицы

f.close()
