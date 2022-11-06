str_1 = input('Enter the first sentence: ')

str_2 = input('Enter the second sentence: ')

str_3 = input('Enter the third sentence: ')

for x in str_1, str_2, str_3:
      print(x[(len(x)-1)//2:(len(x)+2)//2])