def get_uniq_numbers(src: list) -> list:
    """
    Функция возвращает список неповторяющихся элементов согласно условию задачи
    """
    tmp = set()
    user_list = []
    for i in range(len(src)):
        for k in range(i + 1, len(src)):
            if src[i] == src[k]:
                tmp.add(src[i])
        if src[i] not in tmp:
            user_list.append(src[i])
    return user_list


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))






