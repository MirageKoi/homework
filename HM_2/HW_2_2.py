# Нагадаємо, що відповідно до
# григоріанським календарем, рік є високосним,
# якщо його номер кратний 4, але не кратний 100,
# а також якщо він кратний 400.


# option 1

year = int(input('Вкажіть рік: '))
if year % 400 == 0:
    print('YES')
elif year % 100 == 0:
    print('NO')
elif year % 4 == 0:
    print('YES')
else:
    print('NO')


# option 2

year = int(input('Вкажіть рік: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
else:
    print('NO')


# option 3

year = int(input('Вкажіть рік: '))
if year % 4:
    print('NO')
elif not year % 4 and year % 100:
    print('YES')
elif not year % 4 and not year % 400:
    print('YES')
else:
    print('NO')


# option 4

year = int(input('Вкажіть рік: '))
if year % 4 == 0 and year % 100:
    print('YES')
elif year % 4 == 0 and year % 400 == 0:
    print('YES')
elif year % 100 == 0 and year % 400:
    print('NO')
else:
    print('NO')


#option 5

year = int(input('Вкажіть рік: '))
if year % 4 or (not year % 100 and year % 400):
    print('NO')
else:
    print('YES')


#option 6

year = int(input('Вкажіть рік: '))
if (not year % 4 and not year % 400) or (not year % 4 and year % 100):
    print('YES')
else:
    print('NO')


#option 7

year = int(input('Вкажіть рік: '))
print('YES' if (not year % 4 and not year % 400) or (not year % 4 and year % 100) else 'NO')


#option 8

year = int(input('Вкажіть рік: '))
print ('NO' if (year % 4 and year % 400) or (not year % 4 and not year % 100 and year % 400) else 'YES')


#option 9

year = int(input('Вкажіть рік: '))
print('NO' if year % 4 or (not year % 100 and year % 400) else 'YES')

