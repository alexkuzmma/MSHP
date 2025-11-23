# тут будут мои работы в МШП 6 класс

# f-строки
# import math
# name = 'Вася'
# age = 15
#
# print(f'Меня зовут {name} и мне {age} лет')
# print(f'В следующем году мне исполняется {age + 1} лет')
# print(f'В прошлом году мне было {age - 1} лет')
#
#
# print(math.pi)
# print(f'Число Пи равно {math.pi:.3}')

# 07.10.25
# 1
# n = int(input())
#
# print(n // 10 % 10)
# 2
# x = int(input())
# z = x // 1000
# s = x // 100 % 10
# c = x // 10 % 10
# v = x % 10
#
# print(z + s + c + v, z * s * c * v)
# 3
# x = int(input())
# s = x // 100 % 10
# c = x // 10 % 10
# v = x % 10
#
# print(c * 100 + s * 10 + v)

# 09.11.25
# 1
# import time
# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
#
# print('Подождите идет расчет...')
# time.sleep(5)
# n = a + b + c + d + e
# print('Ответ:', n)

# 23.11.25
# 1
# n = int(input())
# if n > 5:
#     print('YES')
# else:
#     print('NO')
#
# 2
# a, b, c = int(input()), int(input()), int(input())
# max = a
#
# if b > max:
#     max = b
# elif c > max:
#     max = c
#
# if c == 9876:
#     print('Максимум равен ', 9876)
# else:
#     print(max)
#
# 3
a, b, c = int(input()), int(input()), int(input())
max = a

if b > max:
    max = b
if c > max:
    max = c

if a + b + c - max < max:
    print('успешный ларек')
else:
    print('слияние двух слабых ларьков')




































