size = int(input("Введіть розмір сторони квадрата: "))

# for i in range(size):
#     for j in range(size):
#         if(i == 0 or i == size - 1 or j == 0 or j == size - 1):
#             print('#', end='  ')
#         else:
#             print(' ', end='  ')
#     print()
#
#
for x in range(size):
    for i in range(size):
        if x == 0 or x == size - 1 or i == 0 or i == size - 1:
            print('#', end='  ')
        else:
            print(' ', end='  ')
    print()