import random as r

lst_1 = [r.randrange(1,500) for i in range(10)]
# lst_1 = [186, 466, 466, 45, 457, 337, 209, 12, 432, 459]

print('Первинний рядок:', lst_1)
print('Парні індекси елементів:', lst_1[::2])
print('Сумма всіх елементів:', sum(lst_1))
print('Сумма парних елементів:', sum(lst_1[::2])) #sum([i for i in lst_1 if i % 2 == 0]))
print('Сумма парних елементів:',sum([i for i in lst_1 if i % 2 == 0]))
print('Сумма непарних елементів:', sum([i for i in lst_1 if i % 2 ]))
print(f'Найбільший елемент: {max(lst_1)}, індекс: {lst_1.index(max(lst_1))}')

