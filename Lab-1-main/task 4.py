from random import randint
import csv

f = open('result for 4.txt', 'w')
f.close()
f = open('result for 4.txt', 'a')
for i in range(1, 21):
    line = randint(2, 9409)
    count = 0
    with open('books.csv', 'r') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        for row in table:
            count += 1
            if count == line:
                if row[4] != '':
                    f.write(str(i)+')'+row[4]+'. '+'"'+row[1]+'"'+' - '+row[6][6:11]+'\n')
                else:
                    f.write(str(i) + ')' + 'Автор неизвестен' + '. ' + '"' + row[1] + '"' + ' - ' + row[6][6:11] + '\n')
# Программа рандомно генерирует 20 библиографических ссылок
