while True:
    str_1 = input('Введіть речення: ')
    if not 15 >= len(str_1) >= 5:
        print('Речення має бути не меньше 5 та не більше 15 символів')
        continue
    else:
        h_cut = len(str_1)//2 # дільник навпіл
        str_2 = str_1[h_cut:]+str_1[:h_cut] # новий зміннений рядок
        print(str_2[:-3]+str_2.upper()[-3:])
        break
