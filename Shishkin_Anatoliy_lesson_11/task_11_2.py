class DivisionError(Exception):
    pass


class Number:

    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def __division(a: int, b: int):
        try:
            return int(a/b)
        except ZeroDivisionError:
            raise DivisionError

    def __truediv__(self, other):
        try:
            result = Number.__division(self.value, other.value)
        except DivisionError:
            result = 'Нельзя делить на ноль, но ладно...'
        return result


c = Number(6)
d = Number(3)
print('6 разделить на 3 будет:')
print(c/d)
c = Number(6)
d = Number(0)
print('6 разделить на 0 будет:')
print(c/d)
