while True:
    str_1 = input('Введіть речення: ')
    if len(str_1) > 10:
        print('Рядок має бути не довшим ніж 10 символів')
        continue
    else:
        l_3 = str_1[-3:].lower()
        str_2 = str_1[:-3]
        h_cut = len(str_2)//2
        print(str_2[:h_cut] + l_3 + str_2[h_cut:])
        break


print(str_1[:(len(str_1)-3)//2]+str_1[-3:] + str_1[(len(str_1)-3)//2:-3])


