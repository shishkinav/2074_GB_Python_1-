class UserError(Exception):
    """
    Класс UserError включает все exceptions, возникающие или генерируемые принудительно по ходу решения задачи.
    Меняется только сообщение
    """
    detail: str = 'Информация об оборудовании должна вводиться в текстовом формате'

    def __init__(self, detail: str = None):
        if detail:
            self.detail = detail
