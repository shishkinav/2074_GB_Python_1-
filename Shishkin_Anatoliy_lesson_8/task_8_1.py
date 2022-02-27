import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(?:^[0-9a-zA-Z+_.-]+)|(?:[0-9a-zA-Z+_.-]+\.\w{2,3}$)')
    pass  # пишите реализацию здесь

    values = RE_MAIL.findall(email)
    if len(values) == 2:
        dict_out = dict()
        dict_out['username'] = values[0]
        dict_out['domain'] = values[1]
    else:
        msg = 'Wrong email: ' + email
        raise ValueError(msg)

    return dict_out


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))