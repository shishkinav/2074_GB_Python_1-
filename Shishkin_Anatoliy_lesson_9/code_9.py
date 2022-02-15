"""
Урок 9. Объектно-ориентированное программирование. Введение
"""
from datetime import datetime


class Woman:
    # глобальные атрибуты класса
    name: str = 'Светлана'
    birthday: datetime = datetime(year=2004, month=2, day=20)

    # методы класса
    def introduce_yourself(self):
        print(f"I'm {self.__class__.__name__}")

    def get_info(self):
        print(f'Давай знакомиться: я - {self.name} и я родилась {self.birthday.strftime("%d %B %Y")}')

    def say(self, message: str):
        print(f'{self.name} сказала нам: "{message}"')


girl = Woman()
print(girl)
print(type(girl))
girl.introduce_yourself()
girl.get_info()
girl.say('Ты крутой!')
print('\n')
# girl_2 = Woman()
# girl_2.name = 'Валерия'
# print(girl.name, girl_2.name, Woman.name)
# Woman.name = 'Анастасия'
# print(girl.name, girl_2.name, Woman.name)

print('\n')


class Warehouse:
    """Документирование класса в целом"""
    count: int = 0

    def new_build(self, storage_capasity: float, region: str):
        """Объявляет о постройке нового склада"""
        self.storage_capasity = storage_capasity
        self.region = region
        Warehouse.count += 1  # инкрементируем общее количество складов


warehouse_1 = Warehouse()
warehouse_1.new_build(555.55, 'Москва')
print(warehouse_1.storage_capasity, warehouse_1.region, f'Всего складов: {warehouse_1.count}')
warehouse_2 = Warehouse()
warehouse_2.new_build(150, 'Волгоград')
print(warehouse_2.storage_capasity, warehouse_2.region, f'Всего складов: {warehouse_2.count}')
print('\n')

# Конструктор __init__
class Rabbit:
    auto_count: int = 0

    def __init__(self):
        Rabbit.auto_count += 1


rabbits = [Rabbit() for _ in range(10)]
first_rabbit = rabbits[0]
print(f'Наплодили кроликов - {first_rabbit.auto_count} шт.')
print(f'Наплодили кроликов - {Rabbit.auto_count} шт.')
print('\n')


# Локальные и глобальные переменные
class Cat:
    breed_2 = 'Дурная'

    def her_breed(self):
        breed = 'Породистая'
        return breed


kitty = Cat()
# print(kitty.breed)
print(kitty.breed_2)
print(kitty.her_breed())
print('\n')

"""
Модификаторы доступа

Public (публичный);
Protected (защищённый);
Private (приватный).
"""


class Dog:
    def __init__(self):
        self.voice = 'гав-гав'
        self._color_hair = 'серый'
        self.__place = 'будка во дворе'


dog = Dog()
print(dog.voice)
print(dog._color_hair)
# print(dog.__place)


# Инкапсуляция
class Ant:
    __species: str = 'коричневый'

    def __get_species(self):
        print('Защищенный метод')


ant = Ant()
ant._Ant__get_species()
print(ant._Ant__species)
print('\n')


# Наследование
import time


class People:
    """Так зарождалось всё человечество )))"""
    def __init__(self, name: str, birthday: datetime):
        self.name = name
        self.birthday = birthday

    def introduce_yourself(self):
        return f"I'm {self.__class__.__name__}", self.__get_info()

    def __get_info(self):
        return dict(name=self.name, birthday=self.birthday.strftime("%d %B %Y"))


class Man(People):
    sex: str = 'm'

    def working(self, sleeping: int = 5):
        """Мужик должен уметь работать"""
        while sleeping:
            print(f'Осталось спать секунд: {sleeping}')
            time.sleep(1)
            sleeping -= 1
        print('Поработали, теперь можно и домой!')


worker = Man('Данила', datetime(year=2001, month=11, day=17))
introduce_message, worker_info = worker.introduce_yourself()
print(f' {3 * "-//-"} '.join(map(str, [introduce_message, worker_info, type(introduce_message), type(worker_info)])))
# worker.working()
print('\n')


class Woman2(People):
    sex: str = 'w'

    def __init__(self, name: str, birthday: datetime, secret: str):
        super().__init__(name, birthday)
        self.secret = secret


girl_3 = Woman2('Юлия', datetime(year=2003, month=10, day=25), 'Секретное слово - "Пароль"')
introduce_message, girl_info = girl_3.introduce_yourself()
print(f' {3 * "-//-"} '.join(map(str, [introduce_message, girl_info, type(introduce_message), type(girl_info)])))
# girl_3.working()
print('\n')


# Множественное наследование
# class Father:
#     def send_money(self):
#         print('Деньги перечислены')
#
#     def my_dream(self):
#         print('Я стану космонавтом')


class Mother:
    def be_happy(self):
        print('Не в деньгах счастье!')

    def my_dream(self):
        print('Где спрятаться от этого всего!')


# class Child(Mother, Father):
#     pass


# Полиморфизм / Перегрузка методов
class Father:
    def send_money(self, empty: bool = False):
        if not empty:
            print('Деньги перечислены')
        else:
            print('Я иду заработать')

    def my_dream(self):
        print('Я стану космонавтом')


class Child(Mother, Father):
    def my_dream(self):
        super().my_dream()
        print('Закончу школу и жизнь изменится ^_^')


baby = Child()
baby.send_money()
baby.send_money(True)
baby.be_happy()
baby.my_dream()
print('\n')

print('end lesson 9')
