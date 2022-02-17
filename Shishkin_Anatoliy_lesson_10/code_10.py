"""
Урок 10. Объектно-ориентированное программирование. Продвинутый уровень
"""
# Сегодня обучаемся в режиме игры "БОМЖ" )))

# Перегрузка операторов
from actions.operators import Bottle

our_bottles = set()  # наша коллекция пузырей в карманы

# __init__
bottle_1 = Bottle(1.5, our_bottles)
bottle_2 = Bottle(0.5, our_bottles)
bottle_3 = Bottle(1, our_bottles)
print(f'У нас сейчас есть бутылки: {our_bottles}')
print()

# __del__
bottle_2.trow_away()
del bottle_2
print(f'У нас сейчас есть бутылки: {our_bottles}')
print()

# __str__
print('Ты посчитал свои запасы и увидел:')
for bottle in our_bottles:
    print(f'\t{bottle}')
print()

# __add__
bottle_1 + bottle_3
bottle_3 + bottle_1

print()

# __call__
bottle_1(3)
print()

print()


# Реструктуризация запасов пузырей Warehouse - закупили себе сарай ))
from actions.my_extra import Warehouse


warehouse = Warehouse()
# __setattr__
warehouse.note = 'текст моей записки'
warehouse.title = 'Заначка'
warehouse.title = 6
warehouse.download_bottles(*our_bottles)
bottle_4 = Bottle(0.5, warehouse.our_bottles)
bottle_5 = Bottle(2, warehouse.our_bottles)
print()

# __getitem__
accepted_bottle = warehouse[1]
print('Соответствуют условию объема больше 1 или равного ему:', *accepted_bottle, sep='\n')
print()

# __eq__
warehouse_2 = Warehouse()
if warehouse == warehouse_2:
    print(f'Кол-ва бутылок на складах "{warehouse.title}", "{warehouse_2.title}" РАВНЫ!')
else:
    print(f'Кол-ва бутылок на складах "{warehouse.title}", "{warehouse_2.title}" НЕ РАВНЫ!')
print()

# __lt__
if warehouse < warehouse_2:
    print(f'Название склада "{warehouse.title}" КОРОЧЕ названия "{warehouse_2.title}"')
else:
    print(f'Название склада "{warehouse.title}" ДЛИННЕЕ названия "{warehouse_2.title}"')
print()

# __iadd__
bottle_6 = Bottle(5, warehouse_2.our_bottles)
warehouse_2 += bottle_6
print()
print()


# Интерфейсы
from actions.my_interfaces import VacuumCleaner, VacuumCleaner2


# robot_1 = VacuumCleaner()
robot_2 = VacuumCleaner2()
# robot_1.on_off_action()
robot_2.on_off_action()
robot_2.say()
print()


# Интерфейс итерации
from actions.my_iterators import IterObj, Accumulator, Battery


def energy_consumption(obj: IterObj):
    if not isinstance(obj, IterObj):
        raise TypeError('Нельзя разряжать незаряженное!')
    for remainder in obj:
        print(remainder)
    else:
        print(f'{obj.__class__.__name__} - разряжен')
    print()


# energy_consumption(bottle_6)

acum = Accumulator()
print("Используем энергию нашего аккумулятора:")
energy_consumption(acum)

print('Пробуем повторно использовать энергию аккумулятора:')
energy_consumption(acum)

print()

duracell = Battery()
print("Используем энергию нашей батарейки:")
energy_consumption(duracell)

print('Пробуем повторно использовать энергию батарейки:')
energy_consumption(duracell)

print()


# Декоратор @property
from actions.my_iterators_advance import IterObjAdv, AccumulatorAdv, BatteryAdv
from actions.power_exceptions import PowerMessage, IsNotEnergyObject, PowerEmpty, PowerComplete


def check_energy_object(obj):
    """Проверяем относится объект к заряжаемым или разряжаемым"""
    if not isinstance(obj, IterObjAdv):
        raise IsNotEnergyObject()


def func_charging(obj: IterObjAdv):
    """Заряжаем объекты"""
    try:
        check_energy_object(obj)
        while True:
            obj.charging()
    except PowerMessage as err:
        print(err)


def energy_consumption_adv(obj: IterObjAdv):
    try:
        check_energy_object(obj)
        for remainder in obj:
            print(remainder)
        else:
            raise PowerEmpty(f'{obj.__class__.__name__} - разряжен')
    except PowerMessage as err:
        print(err)


# try:
#     # custom_exception = PowerComplete()
#     # # raise custom_exception
#     # custom_exception_2 = PowerComplete('Я ручное сообщение')
#     raise PowerComplete('Я ручное сообщение')
#     # raise custom_exception_2
# except PowerMessage as error:
#     print(f'{error}')

# energy_consumption_adv(bottle_6)
print()

acum2 = AccumulatorAdv()
acum2.count = 100
print(acum2)
print()

print("Используем энергию нашего аккумулятора:")
energy_consumption_adv(acum2)
print()

print("Пытаемся зарядить аккумулятор:")
func_charging(acum2)
print()

print('Пробуем повторно использовать энергию аккумулятора:')
energy_consumption_adv(acum2)
print()

print()

duracell2 = BatteryAdv()
duracell2.count = 1
print(duracell2)
print()

print("Используем энергию нашей батарейки:")
energy_consumption_adv(duracell2)
print()

print("Пытаемся зарядить батарейку:")
func_charging(duracell2)
print()

print('Пробуем повторно использовать энергию батарейки:')
energy_consumption_adv(duracell2)
print()


# Композиция - сначала прочувствуем логику здесь, потом читаем исходники
from actions.my_compozition import HardDisk, Monitor, Mouse, Computer


disk_1 = HardDisk()
disk_2 = HardDisk()
monitor = Monitor()
mouse = Mouse()
computer = Computer()

for obj in (disk_1, monitor, mouse, disk_2):
    computer.add(obj)

print(monitor.diagnostics())
print(computer.diagnostics())

print()


print('end lesson 10')
