"""
Урок 6. Работа с файлами
"""
# файлик hello.txt
# import io
file_1 = open('hello.txt', 'r', encoding='utf-8')
# print(type(file_1))
# print(dir(file_1))
"""
'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 
'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 
'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines'
"""
content = file_1.read()
# print(content)
file_1.close()
# print(content)
# content = file_1.read()
# print(content)

file_2 = open('hello.txt', 'r', encoding='utf-8')
# print(file_2.readline(), 'новая строка')
# print(file_2.readline(), 'новая строка')
# print(type(file_2.readline()), 'новая строка')
# print(file_2.readline() == '', 'новая строка')
# print(type(file_2.readline()), 'новая строка')
file_2.close()

file_3 = open('hello.txt', 'r', encoding='utf-8')
# for line in file_3:
#     print(line.strip(), end='')
file_3.close()

file_4 = open('hello.txt', 'r', encoding='utf-8')
lines = file_4.readlines()
print(lines)
file_4.close()

print('\n\n')

# with open('trash/qwerty.txt', 'w+', encoding='utf-8') as fw:
#     print('Здесь какие-то букашки, супер нинзя черепашки!', file=fw)
#     fw.write('qwe\nzxc\nasd\n')
#     fw.seek(0)
#     print(fw.read())

# with open('trash/qwerty_2.txt', 'a+', encoding='utf-8') as fa:
#     from datetime import datetime
#
#     current_time = datetime.now()
#     fa.write(f'{type(current_time)} - {current_time}\n')


# summator
import random


# tasks = [f'{random.randrange(1, 10)} {random.randrange(1, 10)}\n' for _ in range(10)]

# формируем тестовые данные для разбора
# with open('trash/tasks_summator.txt', 'w', encoding='utf-8') as fw:
#     # fw.write(str(tasks))
#     fw.writelines(tasks)


def send_sum(value_1: int, value_2: int):
    """Простейшая функция суммирования двух значений"""
    return value_1 + value_2


result_sum = 0
with open('trash/tasks_summator.txt', 'r', encoding='utf-8') as fr:
    for row in fr.readlines():
        v1, v2 = row.split(' ')
        result_sum += send_sum(*map(int, [v1, v2]))

print('1 - Результат рассчитанной суммы:', result_sum)


result_2 = 0
with open('trash/tasks_summator.txt', 'r', encoding='utf-8') as fr:
    while True:
        row = fr.readline()
        if not row:
            break
        v1, v2 = row.split(' ')
        result_2 += send_sum(*map(int, [v1, v2]))

print('2 - Результат рассчитанной суммы:', result_2)


# json
import json


my_dataset = [
    {'name': 'Светлана', 'level': 115},
    {'name': 'Иван', 'level': 33}
]

# with open('trash/tasks_json.json', 'w', encoding='utf-8') as fjson:
#     # str_json = json.dumps(my_dataset, ensure_ascii=False, indent=2)
#     # fjson.write(str_json)
#     json.dump(my_dataset, fjson, ensure_ascii=False, indent=2)
#
# with open('trash/tasks_json.json', 'r', encoding='utf-8') as fr:
#     # str_json = fr.read()
#     # import_dataset = json.loads(str_json)
#     import_dataset = json.load(fr)
#     print(import_dataset)


# pickle
import pickle


data = {
    1: [random.randrange(1, 10) for _ in range(5)],
    2: ('Я какая-то строка', b'binary data'),
    3: {None, True, False}
}

with open('trash/data.pickle', 'wb') as fw:
    pickle.dump(data, fw)
    # data_bytes = pickle.dumps(data)

with open('trash/data.pickle', 'rb') as fr:
    data_new = pickle.load(fr, encoding='utf-8')
    # dataset = pickle.loads(data_bytes)

print(type(data_new), data_new)


# Профилируем создания файла в байтах и текстового, проверяем размер
from time import perf_counter


# nums = [random.random() * 10 ** 6 for _ in range(10 ** 6)]
#
# start = perf_counter()
# with open('trash/random_million.json', 'w', encoding='utf-8') as f:
#     json.dump(nums, f)
# print(f'json saved: {perf_counter() - start}')
#
# start = perf_counter()
# with open('trash/random_million.pickle', 'wb') as f:
#     pickle.dump(nums, f)
# print(f'pickle saved: {perf_counter() - start}')
#
#
# # профилируем считываение файла в байтах и текстового
# start = perf_counter()
# with open('trash/random_million.json', 'r', encoding='utf-8') as f:
#     nums = json.load(f)
# print(f'json loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}')
#
# start = perf_counter()
# with open('trash/random_million.pickle', 'rb') as f:
#     nums = pickle.load(f)
# print(f'pickle loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}')


# Чтение файлов порциями
chunk_size = 256
with open('trash/random_million.json', 'r') as f:
    str_data = []
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        str_data.append(chunk)
    nums = json.loads(''.join(str_data))
print(f'{type(nums)}, {len(nums)}')

with open('trash/random_million.pickle', 'rb') as f:
    binary_data = bytearray()
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        binary_data.extend(chunk)
    nums = pickle.loads(binary_data)
print(f'{type(nums)}, {len(nums)}')

# encode и decode
hello_text = 'Привет мир'
txt_binary = hello_text.encode(encoding='utf-8')
txt_origin = txt_binary.decode(encoding='utf-8')
print(txt_binary)
print(txt_origin)


print('end lesson 6')
