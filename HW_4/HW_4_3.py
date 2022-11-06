from random import randrange as r

lst_1 = [r(1,500) for i in range(22)]

print(lst_1)

for i in range(0, len(lst_1), 5):
    lst_1[i:i+5] = sorted(lst_1[i:i+5], reverse=(i//5%2))

print(lst_1)


