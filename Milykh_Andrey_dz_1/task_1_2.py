# Задание 2
"""
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000
   (куб X - третья степень числа X):

   Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

   Например, число `19 ^ 3 = 6859` будем включать в сумму,  так как
   `6 + 8 + 5 + 9 = 28` – делится нацело на `7`.

   Внимание: использовать только арифметические операции!

b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
   списка, сумма цифр которых делится нацело на 7.

*c) Решить задачу под пунктом b, не создавая новый список.
   (если будете решать - либо создайте доп. функцию, либо перепишите существующую sum_list_2)
"""


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    # место для написания кода
    sum_result = 0
    for value in dataset:
        number_list = str(value)
        digits_sum = 0
        for digit_str in number_list:
            digits_sum += int(digit_str)
        if digits_sum % 7 == 0:
            sum_result = sum_result + value
    return sum_result  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    modified_list = []
    for value in dataset:
        modified_list.append(value + 17)
    sum_result = sum_list_1(modified_list)
    return sum_result  # Верните значение полученной суммы


def sum_list_3(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
            сумма цифр которых делится нацело на 7"""
    # Решить задачу под пунктом b, не создавая новый список.
    # место для написания кода
    sum_result = 0
    for value in dataset:
        value_new = value + 17
        number_list = str(value_new)
        digits_sum = 0
        for digit_str in number_list:
            digits_sum += int(digit_str)
        if digits_sum % 7 == 0:
            sum_result = sum_result + value_new

    return sum_result  # Верните значение полученной суммы


my_list = []  # Соберите нужный список по заданию
for number in range(1000):
    if number % 2 != 0:
        my_list.append(number**3)

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
result_3 = sum_list_3(my_list)
print(result_3)
