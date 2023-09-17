import csv

count = 0
f = open('result.txt', 'a')
with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        if len(row[1]) > 30:
            count += 1
if '2 задание\n' not in open('result.txt', 'r'):
    f.write('2 задание\n'+'Записей, у которых в поле "Название" строка длиннее 30 символов, ровно '+str(count)+'\n')

f.close()