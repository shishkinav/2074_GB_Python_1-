def thesaurus(*names: str) -> dict:

    key_list = []
    aux_list = []
    names_list = []
    dictionary = {}

    # из входных аргументов получаем лист, состоящий из заглавных букв - key_list
    for i in range(0, len(names), 1):
        key_list.append(names[i][0])
    # удаляем повторы из листа key_list
    i = 0
    while i < len(key_list) - 1:
        if key_list[i] == key_list[i + 1]:
            key_list.remove(key_list[i + 1])
        else:
            i = i + 1
    # по каждой букве из key_list формируем список из фамилий и добавляем его в список names_list, формируем словарь dictionary
    for i in range(0, len(key_list), 1):
        for k in range(0, len(names), 1):
            if key_list[i] == names[k][0]:
                aux_list.append(names[k])
        names_list.append(aux_list)
        aux_list = []
        dictionary.update({key_list[i]: names_list[i]})

    return dictionary


print(thesaurus("Виктор", "Владимир", "Борис", "Братислав", "Марина"))