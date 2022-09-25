import csv
import random

# Вариант 4

over_30 = 0
all = -1
id_set = set()
title_set = set()
popular = [0]*20

name = input('Введите автора: ')

with open('books.csv') as f:
    reader = csv.reader(f, delimiter=";")

    for s in reader:
        if all == -1: all = 0; continue
        if s[8] == '25': print(s[1])
        if len(s[1]) > 30: over_30 += 1
        all += 1

        # if name.lower() in s[3].lower() and float(s[7]) < 200:
        #     if s[0] not in id_set and s[1] not in title_set: #Исключение повторов
        #         print(s[1])
        #
        # if int(s[8]) > popular[0]:
        #     popular[0] = int(s[8])
        # popular.sort()
        # #print(popular)

        if s[0] not in id_set and s[1] not in title_set:  # Исключение повторов
            if name.lower() in s[3].lower() and float(s[7]) < 200:
                print(s[1])

            if int(s[8]) > popular[0]:
                popular[0] = int(s[8])
            popular.sort()
        print(popular)
        id_set.add(s[0])
        title_set.add(s[1])


with open('books.csv') as f:
    reader = csv.reader(f, delimiter=";")

    a = random.sample(list(id_set), 20)

    c = 0
    w = open('file.txt', 'w')

    for s in reader:
        if s[0] in a and c < 20:
            c += 1
            w.write(f"{c}. {s[3]}. {s[1]} - {s[6].split(' ')[0].split('.')[2]}\n")

print('-'*30)
print(f'Количество записей: {all}')
print(f'Кол-во записей с названием длиннее 30: {over_30}')