def main(argv):
    program, price = argv
    line_len = 10
    price = price.replace(",", ".")
    price = price.ljust(line_len, ' ')
    file_name = 'bakery.csv'
    with open(file_name, 'a', encoding='utf-8') as f1:
        f1.write(f'{price}\n')


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        exit(main(sys.argv))
    else:
        raise TypeError("Ожидалась цена продажи")
