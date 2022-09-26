import csv
import random

# Вариант 4

over_30 = 0
all = -1
id_set = set()
title_set = set()
popular = {0: 0}
tags = set()

name = input('Введите автора: ')

with open('books.csv') as f:
    reader = csv.reader(f, delimiter=";")

    for s in reader:
        if all == -1: all = 0; continue
        if len(s[1]) > 30: over_30 += 1
        all += 1

        #поиск книг по автору
        if s[0] not in id_set and s[1] not in title_set:
            if name.lower() in s[3].lower() and float(s[7]) < 200:
                print(s[1])

        #поиск самых популярных книг
        #т.к. в файле есть несколько копий одной книги считает кол-во выдачей для всех копий
        if s[1] in popular: popular[s[1]] += int(s[8])
        else: popular[s[1]] = int(s[8])

        tags.update(*[x.split('#') for x in s[12].split('# ')])

        id_set.add(s[0])
        title_set.add(s[1])

popular = dict(sorted(popular.items(), key=lambda item: item[1]))

#запись 20 рандомных книг в файл
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
print('-'*30)
print('20 самых популярнтых книг:')
for i in range(len(popular) - 1, len(popular) - 21, -1):
    print(list(popular.keys())[i])
print('-'*30)
tags.remove('')
print(f"Все жанры: {', '.join(tags)}")