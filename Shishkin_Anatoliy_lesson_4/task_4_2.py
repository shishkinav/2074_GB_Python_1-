import requests

def currency_rates(code: str) -> float:

    web_data = requests.api.get('http://www.cbr.ru/scripts/XML_daily.asp')
    # user_cur = code
    web_list = web_data.text.split('><')
    my_list = []
    aux_list = []
    val = ''
    currency = ''
    result = 0.0


    for i in range (0, len(web_list), 1):
        if web_list[i].split(' ')[0] == 'Valute':
            aux_list = []
            aux_str = ''
            aux_list.append(web_list[i + 2][9])
            aux_list.append(web_list[i + 2][10])
            aux_list.append(web_list[i + 2][11])
            aux_list.append(' ')
            aux_list.append(web_list[i + 5][6])
            aux_list.append(web_list[i + 5][7])
            aux_list.append('.')
            aux_list.append(web_list[i + 5][9])
            aux_list.append(web_list[i + 5][10])
            aux_list.append(web_list[i + 5][11])
            val = aux_list[0] + aux_list[1] + aux_list[2]
            currency = aux_list[4] + aux_list[5] + aux_list[6] +aux_list[7] + aux_list[8] + aux_list[9]
            aux_list.clear()
            aux_list.append(val)
            aux_list.append(currency)
            my_list.append(aux_list)

    for i in range(0, len(my_list), 1):
        if my_list[i][0] == code:
            result = result + float(my_list[i][1])

    return(result)

print(currency_rates('USD'))
print(currency_rates("noname"))