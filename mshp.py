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
# n = int(input())
# s = int(input())
# year = n % 10000
# n = n // 10000
# month = n % 100
# day = n // 100
#
# year1 = s % 10000
# s = s // 10000
# month1 = s % 100
# day1 = s // 100
#
# if n == s:
#     print('В один день')
# elif year < year1:
#     print('Соревнование по прыжкам с табуретки')
# elif year1 < year:
#     print('Кулинарный фестиваль бутерброда')
# elif year == year1:
#     if month < month1:
#         print('Соревнование по прыжкам с табуретки')
#     elif month1 < month:
#         print('Кулинарный фестиваль бутерброда')
#     elif month == month:
#         if day < day1:
#             print('Соревнование по прыжкам с табуретки')
#         else:
#             print('Кулинарный фестиваль бутерброда')
#
# a, b, c, d, e, h = map(int, input().split())
# sum = 0
#
# if a % 2 == 0 and a % 4 != 0:
#     sum += 1
# if b % 2 == 0 and b % 4 != 0:
#     sum += 1
# if c % 2 == 0 and c % 4 != 0:
#     sum += 1
# if d % 2 == 0 and d % 4 != 0:
#     sum += 1
# if e % 2 == 0 and e % 4 != 0:
#     sum += 1
# if h % 2 == 0 and h % 4 != 0:
#     sum += 1
#
# print(sum)
#
# Homework
# 1
# num1, num2, num3, num4 = map(int, input(). split())
# sum = 1
#
# if 3 <= num1 <= 9:
#     sum *= num1
# if 3 <= num2 <= 9:
#     sum *= num2
# if 3 <= num3 <= 9:
#     sum *= num3
# if 3 <= num4 <= 9:
#     sum *= num4
# if sum == 1:
#     sum = -1
#
# print(sum)
#
# 2
# num1, num2, num3, num4, num5 = map(int, input(). split())
# sum = 0
#
# if num1 % 4 == 0:
#     sum += 1
# if num2 % 4 == 0:
#     sum += 1
# if num3 % 4 == 0:
#     sum += 1
# if num4 % 4 == 0:
#     sum += 1
# if num5 % 4 == 0:
#     sum += 1
#
# print(sum)
#
# 29.12.2025
# 1
# n = int(input())
# print('акула') if n > 8 else print('акульчик')
#
# 2 olymp
# old_password = int(input())
# a = old_password // 100000
# b = old_password // 10000 % 10
# c = old_password // 1000 % 10
# d = old_password // 100 % 10
# e = old_password // 10 % 10
# f = old_password % 10
#
# if (a + b + c + d + e + f) % 2 == 0:
#     new_password = f * 100000 + e * 10000 + d * 1000 + c * 100 + b * 10 + a
# else:
#     new_password = b * 100000 + a * 10000 + d * 1000 + c * 100 + f * 10 + e
#
# print('Новый код на сейфе:', new_password)
#
#
# 31.12.2025
# Новогодний марафон ( 10 задач )
# 1
# S = int(input())
# a, b, c, d = map(int, input(). split())
# res = S - a - b - c * 4 - d * 7
#
# print(res)
#
# 2
# a, b = int(input()), int(input())
# print(b - a + 1)
#
# 3
# a = int(input())
# print(a // 4)
#
# 4
# N, M = int(input()), int(input())
# print(N // M, N % M)
#
# 5
# K = float(input())
# print(K / 6)
#
# 6
# num = int(input())
# print(num // 10 % 10)
#
# 7
# K, N = int(input()), int(input())
# gift = 'nothing'
#
# if K > N:
#     gift = 'электросамокат'
# elif K == N:
#     gift = 'носочки'
# else:
#     gift = 'учебник по истории'
#
# print(gift)
#
# 8
# Code = input()
#
# if Code == 'rus':
#     print('Дед Мороз')
# elif Code == 'arm':
#     print('Каханд Пап')
# elif Code == 'fin':
#     print('Йоллупукки')
# elif Code == 'hol':
#     print('Синтер клаас')
# elif Code == 'est':
#     print('Йыулувана')
# elif Code == 'uzb':
#     print('Корбобо')
# elif Code == 'bru':
#     print('Зюзя')
#
# 9
# # Первое решение
# a, b, c = map(int, input(). split())
# max = a
#
# if max < b:
#     max = b
# if max < c:
#     max = c
#
# print(max)
# # Второе решение ( хитрое )
# a, b, c = map(int, input(). split())
# print(max(a, b, c))
#
# FINAL
# 10
# a, b, c, d, e = map(int, input(). split())
# res1 = a % 100
# res2 = b % 100
# res3 = c % 100
# res4 = d % 100
# res5 = e % 100
# sum = 0
#
# if res1 == 14:
#     sum += 1
# if res2 == 14:
#     sum += 1
# if res3 == 14:
#     sum += 1
# if res4 == 14:
#     sum += 1
# if res5 == 14:
#     sum += 1
#
# print(sum)
#
# Classwork
# 11.01.2026
# 1
# Эта версия лучше чем моя первая!!!
# sum = 0
#
# print('⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘')
# print('⁘      Привет! Рад приветствовать тебя здесь!        ⁘')
# print('⁘       Ты попал на тест - "Какой ты фрукт?"         ⁘')
# print('⁘          Пожалуйста введи своё имя ниже            ⁘')
# print('⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘')
# print('')
# print('Имя : ', end = '')
# name = input()
# print('')
# print('⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘')
# print('⁘       Отлично!',  name,'ты готов начать тест?       ⁘')
# print('⁘        Да - 1                   Нет - 2            ⁘')
# print('⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘⁘')
# print('')
# print('Введите число : ', end = '')
# b = int(input())
# print('')
# if b == 2:
#     print('Хорошо. Завершаем тест.')
# elif b == 1:
#     print('Хорошо. Начианаем тест.')
#     print('')
#     print('⌜┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄⌝')
#     print('|                    Вопрос 1                       |')
#     print('|           Какой цвет тебе нравится больше?        |')
#     print('|   Красный - 1               оранжевый - 2         |')
#     print('|   Желтый - 3                Зеленый - 4           |')
#     print('⌞┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄⌟')
#     print('')
#     print('Введите число : ', end = '')
#     c = int(input())
#     if c == 1:
#         sum += 0
#     elif c == 2:
#         sum += 5
#     elif c == 2:
#         sum += 15
#     elif c == 2:
#         sum += 30
#     print('')
#     print('⌜┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄⌝')
#     print('|                    Вопрос 2                       |')
#     print('|             Кого ты любишь больше?                |')
#     print('|         Собаки - 1             Кошки - 2          |')
#     print('⌞┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄⌟')
#     print('')
#     print('Введите число : ', end = '')
#     d = int(input())
#     if d == 1:
#         sum += 0
#     elif d == 2:
#         sum += 10
#     print('')
#     print('⌜┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄⌝')
#     print('|                    Вопрос 3                       |')
#     print('|            Какую погоду ты любишь больше?         |')
#     print('|          теплую - 1            холодную - 2       |')
#     print('⌞┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄⌟')
#     print('')
#     print('Введите число : ', end='')
#     e = int(input())
#     if e == 1:
#         sum += 0
#     elif e == 2:
#         sum += 10
#     print('')
#     print('⌜┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄⌝')
#     print('|                Последний вопрос                   |')
#     print('|            Какой вкус тебе нравится больше?       |')
#     print('|       сладкий вкус - 1        кислый вкус - 2     |')
#     print('|               кисло-сладкий вкус - 3              |')
#     print('⌞┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄⌟')
#     print('')
#     print('Введите число : ', end='')
#     f = int(input())
#     if f == 1:
#         sum += 0
#     elif f == 2:
#         sum += 10
#     elif f == 3:
#         sum += 20
#     print('')
#
#     if 0 < sum <= 10:
#         sum = 'яблоко'
#     elif 10 < sum <= 30:
#         sum = 'манго'
#     elif 30 < sum <= 50:
#         sum = "банан"
#     elif sum == 0 or sum > 50:
#         sum = 'киви'
#
#     print('✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦')
#     print('✦                                                 ✦')
#     print('✦          Поздравляю,', name,'! Вы прошли тест!    ✦')
#     print('✦        Данные показали, что вы', sum,'!            ✦')
#     print('✦                  {｡^◕‿◕^｡}                        ✦')
#     print('✦                                                 ✦')
#     print('✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦')
#
# 1
# 14.01
# sum = 0
#
# print("Привет! Ты попал на тест - Какой ты смайлик?")
# print('В этом тесте всего 3 вопроса!')
# print('')
# print('Давай начнем!')
# print('')
# print('Вопрос1 :')
# print('Ты грустишь иногда?')
# print('1 - да, 2 - нет, 3 - конечно нет')
# print('')
# print('Твой вариант ответа: ', end = '')
#
# a = int(input())
#
# if a == 1:
#     sum += 0
# elif a == 2:
#     sum += 5
# elif a == 3:
#     sum += 10
#
# print('Вопрос 2:')
# print('Ты любишь лето?')
# print('1 - ДААА, 2 - нет, 3 - да, но нет')
# print('')
# print('Твой вариант ответа: ', end = '')
#
# b = int(input())
#
# if b == 2:
#     sum += 0
# elif b == 3:
#     sum += 5
# elif b == 1:
#     sum += 10
#
# print('Вопрос 3:')
# print('Ты любишь учиться?')
# print('1 - да, 2 - нет, 3 - НЕЕТ')
# print('')
# print('Твой вариант ответа: ', end = '')
#
# c = int(input())
#
# if c == 1 or c == 2:
#     sum += 5
# elif c == 3:
#     sum += 10
#
# if 0 <= sum < 10:
#      sum = ':('
# elif 10 <= sum < 20:
#     sum = '-_-'
# elif 20 <= sum <= 30:
#     sum = ':)'
#
# print('')
# print('Итааак......')
# print('Ваш смайлик - ', sum)

# n = int(input())
#
# n1 = n % 100
# n2 = n % 10
#
# if 11 <= n1 <= 14:
#     print(n, "bochek")
# elif n2 == 1:
#     print(n, "bochka")
# elif 2 <= n1 <= 4:
#     print(n, "bochki")
# else:
#     print(n, "bochek")
#
# Homerwork
# 21.01
# 1
s = int(input())

if s == 3:
    print('WIN')
elif s == 1:
    print('DRAW')
elif s == 0:
    print('LOSE')

# 2
sum = 0
a, b, c = int(input()), int(input()), int(input())

if a > 0:
    sum += a
if b > 0:
    sum += b
if c > 0:
    sum += c

print(sum)

# 3
a, b, c = int(input()), int(input()), int(input())
max = a

if b >= max:
    max = b
if c >= max:
    max = c

if max == a:
    a -= 5
elif max == b:
    b -= 5
elif max == c:
    c -= 5

print(a, b, c)




















































































