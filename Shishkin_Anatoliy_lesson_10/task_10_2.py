from abc import ABC, abstractmethod


class Clothes(ABC):
    '''Абстрактный класс Clothes, регламентирует обязательное переопределение метода calculate'''
    @abstractmethod
    def calculate(self) -> float:
        pass


class Coat(Clothes):
    def __init__(self, size: float):
        self.size = size
    '''Декоратор @property позволяет обращаться к методу calculate в качестве атрибута'''
    @property
    def calculate(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, height: float):
        self.height = height

    @property
    def calculate(self):
        return 2 * self.height + 0.3


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3