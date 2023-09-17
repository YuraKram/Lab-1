f = open('result.txt', 'a')


def var1(table, full_name):
    for row in table:
        if row[0] != 'ID' and float(row[7]) <= 150 and full_name == row[4]:
            f.write(row[1] + '\n')


def var2(table, full_name):
    for row in table:
        if row[0] != 'ID' and int(row[6][6:11]) <= 2016 and full_name == row[4]:
            f.write(row[1] + '\n')


def var3(table, full_name):
    for row in table:
        if row[0] != 'ID' and (
                int(row[6][6:11]) == 2014 or int(row[6][6:11]) == 2016 or int(row[6][6:11]) == 2017) and full_name == \
                row[4]:
            f.write(row[1] + '\n')


def var4(table, full_name):
    for row in table:
        if row[0] != 'ID' and float(row[7]) <= 200 and full_name == row[4]:
            f.write(row[1] + '\n')


def var5(table, full_name):
    for row in table:
        if row[0] != 'ID' and full_name == row[4]:
            f.write(row[1] + '\n')


def var6(table, full_name):
    for row in table:
        if row[0] != 'ID' and float(row[7]) >= 150 and full_name == row[4]:
            f.write(row[1] + '\n')


def var7(table, full_name):
    for row in table:
        if row[0] != 'ID' and 2016 <= int(row[6][6:11]) <= 2018 and full_name == row[4]:
            f.write(row[1] + '\n')


def var8(table, full_name):
    for row in table:
        if row[0] != 'ID' and (int(row[6][6:11]) == 2015 or int(row[6][6:11]) == 2018) and full_name == row[4]:
            f.write(row[1] + '\n')


def var9(table, full_name):
    for row in table:
        if row[0] != 'ID' and float(row[7]) >= 200 and full_name == row[4]:
            f.write(row[1] + '\n')


def var10(table, full_name):
    for row in table:
        if row[0] != 'ID' and int(row[6][6:11]) >= 2018 and full_name == row[4]:
            f.write(row[1] + '\n')


