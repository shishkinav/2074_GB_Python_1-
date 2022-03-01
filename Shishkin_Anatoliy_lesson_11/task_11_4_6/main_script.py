from storage_model import Storage


# Первый сет входных данных
input_data_1 = [
    {'Принтер': '', 'Производитель': 'HP', 'Модель': 'DeskJet IA Ultra 4828 AiO', 'Состояние': ''},
    {'Принтер': '', 'Производитель': 'HP', 'Модель': 'LaserJet M111w', 'Состояние': 'б/у'},
    {'Сканер': '', 'Производитель': 'Fujitsu', 'Модель': 'ScanSnap S1100i', 'Состояние': 'новый'},
    {'Ксерокс': '', 'Производитель': 'Canon', 'Модель': 'imageRUNNER 2425i', 'Состояние': 'б/у'}
]

# Второй сет входных данных
input_data_2 = [
    {'Сканер': '', 'Производитель': 'Brother', 'Модель': 'DS-640', 'Состояние': 'новый'}
]

# Инициализация объекта storage класса Storage
storage = Storage()
# Наполнение storage данными из input_data_1
storage.load_storage(input_data_1)
print('')
# Проверка склада
storage.get_info()
print('')
# Удаление единицы оргтехники с арт. № 13094
storage.remove('13094')
# Проверка склада
storage.get_info()
print('')
# Добавление в storage единицы из input_data_2
storage.load_storage(input_data_2)
# Проверка склада
storage.get_info()
print('')
# Проверка наличия техники в подразделениях
storage.check_offices()
print('')
# Передача единицы с арт. № 17249 в подразделение ОВнП
storage.transfer_to(destination='ОВнП', article='17249')
# Передача единицы с арт. № 38774 в подразделение Клиентский отдел
storage.transfer_to(destination='Клиентский отдел', article='38774')
# Проверка наличия техники в подразделениях
storage.check_offices()
print('')
# Проверка склада
storage.get_info()
# Передача единицы с арт. № 17249 из подразделение ОВНП обратно на склад
storage.transfer_from('17249')
print('')
# Проверка наличия техники в подразделениях
storage.check_offices()
print('')
# Проверка склада
storage.get_info()
# Передача единицы с арт. № 17249 в подразделение Бухгалтерия
storage.transfer_to(destination='Бухгалтерия', article='17249')
print('')
# Проверка наличия техники в подразделениях
storage.check_offices()
print('')
# Проверка склада
storage.get_info()
print('')
# Добавление в storage единицы из input_data_2
storage.load_storage(input_data_2)
# Проверка склада
storage.get_info()
