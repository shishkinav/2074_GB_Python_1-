from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        '''Проверка на то, что количество элементов в строках экземпляра объекта matrix одинаковое'''
        for i in range(len(matrix) - 1):
            if not len(self.matrix[i]) == len(self.matrix[i + 1]):
                raise ValueError('fail initialization matrix')
        '''Проверка на то, что в экземпляр объекта matrix входят только математические элементы'''
        for i in range(len(matrix)):
            for k in range(len(matrix[i])):
                if not isinstance(self.matrix[i][k], int):
                    raise ValueError('fail initialization matrix')

    def __str__(self):
        '''Метод обеспечивает вывод матрицы на печать согласно заданию'''
        output = str()
        for i in range(len(self.matrix)):
            row = str()
            for k in range(len(self.matrix[i])):
                row = ' '.join([row, str(self.matrix[i][k])])
            output = output + '|' + row + ' |\n'
        return output

    def __add__(self, other):
        '''Метод обеспечивает сложение матриц и возвращает объект класса Matrix'''
        sum_matrix = [
            [self.matrix[i][k] + other.matrix[i][k] for k in range(len(self.matrix[i]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(sum_matrix)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    print(second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    print(fail_matrix)

    """
    Traceback (most recent call last):
      ...
    # ValueError: fail initialization matrix
    """