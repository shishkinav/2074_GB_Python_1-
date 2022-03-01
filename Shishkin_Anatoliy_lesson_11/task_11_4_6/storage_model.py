import os
from typing import List
from datetime import date
from exceptions import UserError
from items_model import OfficeEquipment, Printer, Scanner, Xerox


class Storage:
    """
    Класс Склад. В объекте класса хранится информация о позициях техники в наличии на складе и о позициях техники,
    переданных в другие подразделения. Атрибут _articles хранит доступные артикульные номера, которые присваиваются
    складским позициям при первичном поступлении на склад.
    """
    _articles: set = {38774, 13094, 28591, 92659, 17249}

    def __init__(self):
        self.storage: List[OfficeEquipment] = []
        self.in_offices: set = set()

    def add(self, item: OfficeEquipment):
        self.storage.append(item)

    def load_storage(self, data: list):
        """Метод наполняет склад позициями и присваивает артикульные номера."""
        try:
            for item in data:
                manufacturer = item['Производитель']
                model = item['Модель']
                condition = item['Состояние']
                article = str(self._articles.pop())
                if 'Принтер' in item:
                    printer_in = Printer(manufacturer=manufacturer,
                                         model=model,
                                         condition=condition,
                                         _article=article)
                    self.storage.append(printer_in)
                if 'Сканер' in item:
                    scanner_in = Scanner(manufacturer=manufacturer,
                                         model=model,
                                         condition=condition,
                                         _article=article)
                    self.storage.append(scanner_in)
                if 'Ксерокс' in item:
                    xerox_in = Xerox(manufacturer=manufacturer,
                                     model=model,
                                     condition=condition,
                                     _article=article)
                    self.storage.append(xerox_in)
        except KeyError as err:
            raise UserError(f'Ошибка ввода. Неверный ключ: {err}')

    def remove(self, article: str):
        """
        Удаление складской позиции со склада (например, если пришла в негодность).
        Артикульный номер возвращается в _articles.
        """
        for item in self.storage:
            if item.get_article() == article:
                self.storage.remove(item)
                self._articles.add(article)

    def get_info(self):
        if not len(self.storage):
            print('На складе нет оргтехники')
        else:
            print('На складе в наличии:')
            for item in self.storage:
                print(item.get_info())

    def transfer_to(self, destination: str, article: str):
        """
        Метод перемещает складскую позицию с заданным артикульным номером в одно из подразделений организации.
        Операция записывается в лог-файл с указанием даты.
        Наименование подразделения и артикульный номер задаются произвольно. Если тип данных не строковый,
        вызывается исключение.
        При перемещении позиция добавляется в множество self.in_offices и ей присваивается дополнительный
        атрибут-метка со значением наименования подразделения.
        """
        if not len(self.storage):
            print('На складе нет оргтехники')
        else:
            if not isinstance(destination, str):
                raise UserError('Некорректно введено наименование подразделения')
            if not isinstance(article, str):
                raise UserError('Некорректно введен артикульный номер')
            for item in self.storage:
                if item.get_article() == article:
                    item_exp = item.set_tag(destination)
                    self.in_offices.add(item_exp)
                    self.storage.remove(item)
                    with open('log.txt', 'a', encoding='utf-8') as log:
                        log.write(f'{item.get_info()} передан в {destination} {date.today()}\n')
                    break

    def transfer_from(self, article: str):
        """
        Метод перемещает позицию из подразделения на склад по артикульному номеру.
        Операция записывается в лог-файл с указанием даты.
        """
        if not len(self.in_offices):
            print('В подразделениях нет оргтехники со склада')
        else:
            for item_exp in self.in_offices:
                if item_exp.get_article() == article:
                    self.in_offices.remove(item_exp)
                    self.storage.append(item_exp)
                    destination = item_exp.__dict__['tag']
                    with open('log.txt', 'a', encoding='utf-8') as log:
                        log.write(f'{item_exp.get_info()} передан из {destination} на склад {date.today()}\n')
                    break

    def check_offices(self):
        """
        Метод проверяет наличие складских позиций в подразделениях и выводит на печать складские позиции
        с указанием подразделений, где они находятся.
        """
        if not len(self.in_offices):
            print('В подразделениях нет оргтехники со склада')
        else:
            print('В подразделения передана следующая оргтехника со склада:')
            for item_exp in self.in_offices:
                is_stored_at = item_exp.__dict__['tag']
                print(f'{is_stored_at}: {item_exp.get_info()}')
