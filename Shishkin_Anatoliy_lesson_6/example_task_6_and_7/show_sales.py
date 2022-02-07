

def main(start: int, finish: int):
    file_name = 'bakery.csv'
    with open(file_name, 'r', encoding='utf-8') as f1:
        line = f1.readline()
        line_count = 1
        while (line_count <= finish) or (finish == 0 and line):
            if line_count >= start:
                print(line.strip())
            line = f1.readline()
            line_count += 1


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        exit(main(1, 0))
    elif len(sys.argv) == 2:
        prog, start = sys.argv
        exit(main(int(start), 0))
    elif len(sys.argv) == 3:
        prog, start, finish = sys.argv
        exit(main(int(start), int(finish)))
    else:
        raise TypeError("Ожидались параметры вывода")
