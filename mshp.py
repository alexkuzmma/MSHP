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
# a, b, c = int(input()), int(input()), int(input())
# max = a
#
# if b > max:
#     max = b
# if c > max:
#     max = c
#
# if a + b + c - max < max:
#     print('успешный ларек')
# else:
#     print('слияние двух слабых ларьков')
# Homework 09.12.25
# 1
# a = int(input())
#
# if a == 5:
#     print('A')
# elif a == 4:
#     print('B')
# elif a == 3:
#     print('C')
# elif a == 2:
#     print('F')
# 2
# n = int(input())
#
# if n >= 11 and n <= 14:
#     s = 'korov'
# elif n % 10 == 1:
#     s = 'korova'
# elif n % 10 >= 2 and n % 10 <= 4:
#     s = 'korovy'
# else:
#     s = 'korov'
#
# print(n, s)
#
# 3
# s = input()
#
# if s == 'Привет':
#     print('Привет!')
# elif s == 'Пока':
#     print('До встречи!')
# elif s == 'Открой гугл':
#     print('Открываю google...')
# elif s == 'Включи музыку':
#     print('Включаю ваш любимый трек...')
# elif s == 'Покажи смешную картинку':
#     print('Ищу мемы в интернете...')
# else:
#     print('Я вас не понимаю')
#
# 4 ( SPECIAl )
n = int(input())
s = int(input())
year = n % 10000
n = n // 10000
month = n % 100
day = n // 100

year1 = s % 10000
s = s // 10000
month1 = s % 100
day1 = s // 100

if n == s:
    print('В один день')
elif year < year1:
    print('Соревнование по прыжкам с табуретки')
elif year1 < year:
    print('Кулинарный фестиваль бутерброда')
elif year == year1:
    if month < month1:
        print('Соревнование по прыжкам с табуретки')
    elif month1 < month:
        print('Кулинарный фестиваль бутерброда')
    elif month == month:
        if day < day1:
            print('Соревнование по прыжкам с табуретки')
        else:
            print('Кулинарный фестиваль бутерброда')


































