import requests
import sys
import typing
from pyquery import PyQuery as pq
from lxml import etree
from pprint import pprint


URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def send_request() -> requests.Response:
    """Выполняет запрос данных с ЦБР"""
    response = requests.get(URL, timeout=2)
    if not response.ok:
        print(f'Запрос не успешен: {response.status_code}')
        sys.exit(0)
    return response


def extract_data(tag: str) -> typing.List:
    """Извлекает данные из соответствующего тега и возвращает список string значений"""
    res = send_request()
    main_root = pq(etree.fromstring(res.content))
    curs_val = main_root.pop()
    return curs_val.xpath(f'//Valute/{tag}/text()')


if __name__ == '__main__':
    # пример использования
    name_valutes = extract_data('Name')
    pprint(name_valutes)
