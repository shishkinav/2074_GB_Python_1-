class Date:

    def __init__(self, date: str = None):
        self.date = date
        Date.convert(date)  # Вызываю класс-метод, который переводит введенную дату в список.
        # Класс-метод в свою очередь обращается к статик методу

    @classmethod
    def convert(cls, date: str = None) -> list:
        date_list = date.split('-')
        if len(date_list) > 3:
            raise ValueError('Один из элементов даты отрицательный')
        for i in range(len(date_list)):
            val = int(date_list[i])
            date_list[i] = val
        Date.check(date_list)  # Вызываю статик-метод не применительно к объекту класса
        return date_list

    @staticmethod
    def check(date_list: list = None) -> str:
        for val in date_list:
            if not isinstance(val, int):
                raise TypeError('Дата должна быть введена в формате день-месяц-год')
        if date_list[2] == 0:
            raise ValueError('Номер года должен быть больше 0')
        days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        i = 0
        for key, val in days_in_month.items():
            if date_list[1] == key:
                i = 1
                if date_list[0] > val or date_list[0] <= 0:
                    raise ValueError(f'Номер дня должен быть в диапазоне от 1 до {days_in_month[key]}')
            if i:
                break  # Чтобы не делать лишних проверок
        if not i:
            raise ValueError('Номер месяца должен быть в диапазоне от 1 до 12')
        return f'Дата {date_list[0]}-{date_list[1]}-{date_list[2]} введена корректно'


user_date_1 = Date('13-07-2022')
print(user_date_1.convert('12-08-2022'))  # Обращаться к класс-методу можно через экземпляр класса
print(Date.convert('12-08-2022'))  # Обращаться к класс-методу можно по имени класса
print(user_date_1.check([12, 8, 2022]))  # Обращаться к статик-методу можно через экземпляр класса
print(Date.check([12, 8, 2022]))  # Обращаться к статик-методу можно по имени класса
# Контроль предусмотренных проверок
# print(Date.convert('32-08-2022'))
# print(Date.convert('18-18-2022'))
# print(Date.convert('10-10-0000'))
# print(Date.convert('10-10--0000'))
# print(Date.check('10-10--0000'))
# user_date_2 = Date('32-08-2022')
# user_date_3 = Date('18-18-2022')
# user_date_4 = Date('10-10-0000')
# user_date_5 = Date('10-10--0000')
