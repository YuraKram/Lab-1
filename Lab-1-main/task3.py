import csv
import mymodule  # Для улучшения читаемости кода вынесем все функции в отдельный модуль

var = int(input('Введите вариант ограничения\n' +
                '| Варианты | Ограничения |\n' +
                '| -------- | ----------- |\n' +
                '| 1 | До 150 рублей |\n' +
                '| 2 | До 2016 года |\n' +
                '| 3 | Только 2014, 2016 и 2017 года |\n' +
                '| 4 | До 200 рублей |\n' +
                '| 5 | Нет |\n' +
                '| 6 |	От 150 рублей |\n' +
                '| 7 | От 2016 до 2018 года |\n' +
                '| 8 | Только 2015 и 2018 года |\n' +
                '| 9 | От 200 рублей |\n' +
                '| 10 | От 2018 года |\n'))
full_name = input('Введите ФИО автора для поиска книги\n')

if '3 задание\n' not in open('result.txt', 'r'):
    mymodule.f.write('3 задание\n')

with open('books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    if var == 1:
        mymodule.var1(table, full_name)
    if var == 2:
        mymodule.var2(table, full_name)
    if var == 3:
        mymodule.var3(table, full_name)
    if var == 4:
        mymodule.var4(table, full_name)
    if var == 5:
        mymodule.var5(table, full_name)
    if var == 6:
        mymodule.var6(table, full_name)
    if var == 7:
        mymodule.var7(table, full_name)
    if var == 8:
        mymodule.var8(table, full_name)
    if var == 9:
        mymodule.var9(table, full_name)
    if var == 10:
        mymodule.var10(table, full_name)

mymodule.f.close()
