# информация по Git http://git-scm.com/book/ru/v2
# python - https://www.python.org/
# JetBrains PyCharm CE - https://www.jetbrains.com/ru-ru/pycharm/

print('Hello world!')

# Арифметические операции
print(37 + 6)
print(37 - 6)
print(37 * 6)
print(37 / 6)
print(37 // 6)  # 6
print(37 % 6)  # 1
print(36 // 6)  # ?
print(36 % 6)  # ?
"""
37 // 6 = 6 * 6 + 1
"""
print(37 ** 6)

# Логические операции
print(5 > 6)
print(5 < 6)
print(5 == 6)
print(5 != 6)
print(5 >= 6)
print(5 <= 6)

x = 0
print(x + 1)

snake_case = 5
per_1 = 'test'
per_2 = "test"
print(per_1 == per_2)

print('\n\n')

# name = input("Введите своё имя:\n")
# print(f'Вас зовут: {name}')

# int
my_int = 50
print(type(my_int))

# float
my_float = 95.654
print(type(my_float))

# bool
my_bool = True  # False
print(type(my_bool))

a = 0
b = 5
c = -9

out = b > a and c < 0
print(out)

out_2 = not((b > a and c < 0) and b == 5)
#                True -> False
print(out_2)

print('\n\n')

user_pass = '1234'
admin_pass = 'admin'
# if user_pass == input('Введите пароль входа в систему:\n'):
#     print('Авторизован успешно')
#     if admin_pass == input('Введите пароль админа:\n'):
#         print('rooted')
#     else:
#         print('not rooted')
# else:
#     print('Пароль не верен')


# color = 'blue'
color = 'green'
if color == 'green':
    print('зеленый')

if color == 'red':
    print('красный')

if color == 'blue':
    print('синий')
else:
    print('цвет неизвестный')


# Список (ознакомительно)
my_list = [100, 'qwe', 540.1, True]
print(my_list[1])  # 'qwe'
my_list.append(1)  # [100, 'qwe', 540.1, True, 1]
print(my_list)


# Циклы
nums = [10, 20, 30, 40]
indx = 0

# while True: - бесконечный цикл (нужно будет обязательно останавливать через break)

while indx < len(nums):
    print(nums[indx] + 1 + indx)
    indx += 1  # indx = indx + 1
    # indx -= 1

print(f'\nцикл for in')
for num in nums:
    print(num)

print(f'\nцикл for in - 2 реализация')
for idx, num in enumerate(nums, start=1):
    print(idx, num)

print(f'\nцикл for in - 3 реализация')
# for num in range(<значение с которого начинаем>=0, <значение до которого перебираем - НЕВКЛЮЧИТЕЛЬНО>, <шаг>=1):
for n in range(1, 10, 2):
    print(n)
print('отрицательный шаг')
for n in range(10, 1, -2):
    print(n)
print('с использованием списка')
for n in range(len(nums), 1, -2):
    print(n)


def my_func(a: int, b: int) -> int:
    c = a + b
    return c  # None


d = 5
f = 6
print(my_func(d, f))
