class FuncAttributeFailError(AttributeError):
    """Возбуждаем при получении некорретных атрибутов функций"""
    pass


class JobDone(Exception):
    """Исключение для демонстрации 4 причины использования raise"""
    pass
