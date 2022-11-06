with open('file_1.txt', 'r') as fl:
    for x in fl:
        print(type(x), x)
        lst = x.split()
        fizz = int(lst[0])
        buzz = int(lst[1])
        leng = int(lst[2])
        print((['F' * (not i % fizz) + 'B' * (not i % buzz) or i for i in range(1, leng + 1)]))