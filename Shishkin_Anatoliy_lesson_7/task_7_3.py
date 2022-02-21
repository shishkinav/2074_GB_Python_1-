import os
import shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
my_project = os.path.join(BASE_DIR, 'my_project')
# Папка для шаблонов в коде называется result_templates, а в директории - templates
result_templates = os.path.join(my_project, 'templates')
if not os.path.exists(result_templates):
    os.mkdir(result_templates)

for par_dir_name in os.listdir(my_project):
    par_dir = os.path.join(my_project, par_dir_name)
    templates = os.path.join(par_dir, 'templates')

    if os.path.exists(templates):
        sub_dir = os.path.join(templates, par_dir_name)
        # Переопределение переменной par_dir - теперь она хранит путь к my_projects/templates
        par_dir = os.path.join(result_templates, par_dir_name)
        try:
            os.mkdir(par_dir)
        except FileExistsError as e:
            print(f'{e}')
        shutil.copy(os.path.join(sub_dir, 'base.html'), par_dir)
        shutil.copy(os.path.join(sub_dir, 'index.html'), par_dir)



