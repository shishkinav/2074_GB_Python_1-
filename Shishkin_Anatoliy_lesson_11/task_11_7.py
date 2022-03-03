import re


class ComplexNumber:

    def __init__(self, value: str):
        self.value = value
        self.parsed = ComplexNumber.parse(value)

    @staticmethod
    def parse(value: str):
        pattern = re.compile(r'\b\d{1,}|[+-]\d{1,}')
        values = pattern.findall(value)
        for i in range(len(values)):
            num = int(values[i])
            values[i] = num
        return values

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError('Оба числа должны быть комплексными')
        true = self.parsed[0] + other.parsed[0]
        image = self.parsed[1] + other.parsed[1]
        if image >= 0:
            result = f'{true}+{image}i'
        else:
            result = f'{true}{image}i'
        return ComplexNumber(result)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError('Оба числа должны быть комплексными')
        true = self.parsed[0] * other.parsed[0] - self.parsed[1] * other.parsed[1]
        image = self.parsed[0] * other.parsed[1] + self.parsed[1] * other.parsed[0]
        if image >= 0:
            result = f'{true}+{image}i'
        else:
            result = f'{true}{image}i'
        return ComplexNumber(result)


a = ComplexNumber('-11+4i')  # Комплексные числа вводить в формате '+/-xx+/-yyi' (строка)
b = ComplexNumber('01-14i')
c = ComplexNumber('-2311-1i')
d = ComplexNumber('2322+1i')
print((a + b).value)  # -10-10i
print((c + d).value)  # 11+0i
print((a + c).value)  # -2322+3i
print((a + d).value)  # 2311+5i
print((a * b).value)  # 45+158i
print((c * d).value)  # -5366141-4633i
print((a * c).value)  # 25425-9233i
print((a * d).value)  # -25546+9277i
# print((a * 3).value)  #  TypeError: Оба числа должны быть комплексными
