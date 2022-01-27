# получим разницу в днях
# обратите внимание на то, что в модуле datetime есть класс datetime
from datetime import datetime, date, timedelta

date_1 = datetime(year=2020, month=12, day=5)
date_2 = datetime(year=2019, month=12, day=5)
date_delta = date_1 - date_2
print(type(date_1), type(date_2))
print(type(date_delta))
print(date_delta.days)

date_3 = date(year=2020, month=12, day=5)
date_4 = date(year=2019, month=12, day=5)
date_delta_2 = date_3 - date_4
print(type(date_3), type(date_4))
print(type(date_delta_2))


# к примеру, если хотим разницу в секундах
"""
import datetime


datetime_1 = datetime.datetime(year=2020, month=12, day=5,
                               hour=18, minute=57, second=30)
datetime_2 = datetime.datetime(year=2020, month=1, day=1,
                               hour=0, minute=0, second=0)
datetime_delta = datetime_1 - datetime_2
print(datetime_delta.seconds)
"""


# имитируем проверку периода активации
"""
from datetime import datetime, timedelta

user_created = datetime(year=2020, month=12, day=4, hour=15, minute=25, second=32)
activation_period = timedelta(days=1, hours=12)

datetime_now = datetime.now()
if datetime_now < user_created + activation_period:
   print('еще можно активировать аккаунт: {time_before}'.format(
       time_before=datetime_now - user_created
   ))
else:
   print('не хватило {time_after}'.format(
       time_after=datetime_now - (user_created + activation_period)
   ))
"""