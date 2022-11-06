# Нагадаємо, що відповідно до
# григоріанським календарем, рік є високосним,
# якщо його номер кратний 4, але не кратний 100,
# а також якщо він кратний 400.
#
# year = int(input('Вкажіть рік: '))
# print ('YES' if (year % 4 == 0 and year % 100) or year % 400 == 0 else 'NO')

year = int(input('Вкажіть рік: '))
if year % 400 == 0:
    print('YES')
elif year % 100 == 0:
    print('NO')
elif year % 4 == 0:
    print('YES')
else:
    print('NO')

# test string