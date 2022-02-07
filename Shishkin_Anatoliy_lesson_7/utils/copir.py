"""
|    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
"""
import os


def files_in_dir(path_dir) -> list:
    """Функция получения списка файлов в директории"""
    try:
        _, _, _files = next(os.walk(path_dir))
        return _files
    except StopIteration:
        raise OSError(f'Файлы в директории {path_dir} не найдены')


def search_file_in_dir(path_file):
    """
    Функция проверки наличия файла в директории
    :param path_file: путь до файла
    :return: str - имя файла
    """
    path_dir, file_name = os.path.split(path_file)
    if not os.path.exists(path_dir):
        raise NotADirectoryError(f'{path_dir} - директория отсутствует')
    if not os.path.exists(path_file):
        raise FileNotFoundError(f'{path_file} - файла НЕТ')
    return file_name
