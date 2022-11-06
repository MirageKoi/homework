#option 1
fizz = 2
buzz = 5
leng = 18
for x in range(1, leng+1):
    if x % fizz == 0 and x % buzz == 0:
        print('FB')
    elif x % fizz == 0:
        print('F')
    elif x % buzz == 0:
        print('B')
    else:
        print(x)

#option 2
fizz = int(input('Enter integer Fizz: '))
buzz = int(input('Enter integer Buzz: '))
leng = int(input('Enter the length: '))


print(['F'*(not i % fizz)+'B'*(not i % buzz) or i for i in range(1, leng+1)])

