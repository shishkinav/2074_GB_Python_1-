# Задание 1
"""
Задание 1
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:

до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:

> duration = 53
53 сек

> duration = 153
2 мин 33 сек

> duration = 4153
1 час 9 мин 13 сек

> duration = 400153
4 дн 15 час 9 мин 13 сек
"""


def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    if 0 <= duration < 60:  # [0, 60[ - секунды
        seconds = duration
        duration_str = f'{seconds} сек'
    elif 60 <= duration < 60 * 60:  # [60, 60*60[ - минуты
        minutes = duration // 60
        seconds = duration % 60
        duration_str = f'{minutes} мин {seconds} сек'
    elif 60 * 60 <= duration < 60 * 60 * 24:  # [60 * 60,  60 * 60 * 24[ - часы
        hours = duration // (60 * 60)
        duration_minutes = duration % (60 * 60)
        minutes = duration_minutes // 60
        seconds = duration_minutes % 60
        duration_str = f'{hours} час {minutes} мин {seconds} сек'
    else:  # 60 * 60 * 24 сутки
        days = duration // (60 * 60 * 24)
        duration_hours = duration % (60 * 60 * 24)
        hours = duration_hours // (60 * 60)
        duration_minutes = duration % (60 * 60)
        minutes = duration_minutes // 60
        seconds = duration_minutes % 60
        duration_str = f'{days} дн {hours} час {minutes} мин {seconds} сек'
    return duration_str


# duration = 400153
durations = [53, 153, 4153, 400153]
i = 0
while i < len(durations):
    result = convert_time(durations[i])
    print(result)
    i += 1
