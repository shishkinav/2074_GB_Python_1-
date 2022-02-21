import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
my_folder = os.path.join(BASE_DIR, 'my_folder')

dataset = {
    1000: 0,
    10000: 0,
    100000: 0,
    1000000: 0,
    10000000: 0,
    100000000: 0
}

if not os.path.exists(my_folder):
    print('В текущей директории отсутствует папка для анализа')
else:
    for roots, dirs, files in os.walk(my_folder):
        for i in range(len(files)):
            file_size = os.stat(os.path.join(roots, files[i])).st_size
            for key, value in dataset.items():
                if file_size < int(key):
                    dataset[key] += 1
                    break
    print(dataset)
