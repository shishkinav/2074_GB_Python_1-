from abc import ABC, abstractmethod
from exceptions import UserError


class Product(ABC):
    """
    Абстрактный класс для техники. Включает только атрибуты 'производитель', 'модель' и 'состояние (новый или б/у)'
    """
    manufacturer: str = 'no information'
    model: str = 'no information'
    condition: str = 'no information'

    def __init__(self, manufacturer: str = None, model: str = None, condition: str = None):
        if manufacturer:
            self.manufacturer = manufacturer
        if model:
            self.model = model
        if condition:
            self.condition = condition
        self.check_attributes()

    def check_attributes(self):
        """Проверка, что в атрибуты переданы данные строкового типа."""
        for attribute, value in self.__dict__.items():
            if not isinstance(value, str):
                raise UserError(UserError.detail)

    @abstractmethod
    def get_info(self) -> dict:
        return {
            'Производитель': self.manufacturer,
            'Модель': self.model,
            'Состояние': self.condition
        }

    def set_tag(self, tag: str):
        """
        Метод используется для присваивания дополнительного атрибута объекту класса.
        Дополнительный атрибут применяется в последующем как метка, указывающая куда передана складская позиция.
        """
        setattr(self, 'tag', tag)
        return self


class OfficeEquipment(Product):
    """
    В классе вводятся атрибуты subclass_name (принтер, ксерокс, сканер) и артикульный номер складской позиции.
    """
    subclass_name: str = None
    _article: str = 'no information'

    def __init__(self, _article: str = None, *args, **kwargs):
        super(OfficeEquipment, self).__init__(*args, **kwargs)
        if _article:
            self._article = _article

    def get_info(self) -> dict:
        """
        Метод объединяет словарь вида {Название подкласса: артикульный номер} и словарь из метода get_info класса-родителя.
        Возвращает результирующий словарь.
        """
        out_dict = {self.subclass_name: self._article}
        out_dict.update(Product.get_info(self))
        return out_dict

    def get_article(self) -> str:
        """Метод возвращает артикульный номер объекта."""
        return self._article


class Printer(OfficeEquipment):
    """
    Класс Принтер. Переопределен атрибут subclass_name.
    Значение атрибута применяется в последующем для вывода информации.
    """
    subclass_name: str = 'Принтер'


class Scanner(OfficeEquipment):
    """
    Класс Сканер. Переопределен атрибут subclass_name.
    Значение атрибута применяется в последующем для вывода информации.
    """
    subclass_name: str = 'Сканер'


class Xerox(OfficeEquipment):
    """
    Класс Ксерокс. Переопределен атрибут subclass_name.
    Значение атрибута применяется в последующем для вывода информации.
    """
    subclass_name: str = 'Ксерокс'

