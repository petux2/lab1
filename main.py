import csv
# ID;Название;Тип;Автор;Автор (ФИО);Возрастное ограничение на книгу;Дата поступления;Цена поступления;Кол-во выдач;Дата списания книги;Инвентарный номер;Выдана до;Жанр книги
c = 0
more_than_30 = 0
all = -1
a = set()
with open('books.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i in reader:
        if all == -1:
            all = 0
            continue
        #print(i)
        #print(' '.join(i))
        s = ' '.join(i).split(';')
        if len(s[1]) > 30: more_than_30 += 1
        all += 1
        #print(s[3])
        a.add(s[3])
        #print(s, len(s))
        #c += 1
        #if c == 50: break
print(all, more_than_30)
#print(a)