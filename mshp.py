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
x = int(input())
s = x // 100 % 10
c = x // 10 % 10
v = x % 10

print(c * 100 + s * 10 + v)