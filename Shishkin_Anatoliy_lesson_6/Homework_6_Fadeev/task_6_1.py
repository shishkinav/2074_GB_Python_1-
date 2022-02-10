from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    pass  # Ваша реализация здесь
    line_1 = line
    line_1 = line_1.split(' ')
    line_out = (line_1[0], line_1[5].replace('"', ''), line_1[6])
    return line_out
    # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    pass  # передавайте данные в функцию и наполняйте список list_out кортежами
    content = fr.readlines()
    for i in range(0, len(content), 1):
        list_out.append(get_parse_attrs(content[i]))

pprint(list_out)

# выгрузил данные в файл log.txt, так как в PyCharm плохо отображается
with open('log.txt', 'wt') as out:
    pprint(list_out, indent=5, stream=out)