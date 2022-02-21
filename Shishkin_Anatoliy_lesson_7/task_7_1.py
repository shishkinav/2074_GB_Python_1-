import os


def make_dir(curr_dir: str, new_dir: str):
    '''
    Функция принимает названия текущей и новой директорий в качестве аргументов и создает новую директорию при условии,
    что отсутствует директория с таким названием.
    '''
    new_dir = os.path.join(curr_dir, new_dir)
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

src = {
    BASE_DIR: ['my_project'],
    'my_project': ['settings', 'adminapp', 'adminapp', 'adminapp']

}
for key, value in src.items():
    for i in range(len(value)):
        make_dir(key, value[i])
