def main(argv):
    program, *args = argv
    result = sum(map(int, args))
    print(f'результат: {result}')
    return 0


if __name__ == '__main__':
    import sys

    print(type(sys.argv), sys.argv)
    sys.exit(main(sys.argv))
