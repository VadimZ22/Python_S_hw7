import os
from pathlib import Path
from random import sample
import string
import shutil


def make_dir(name):
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)


def create_name(lenght):
    name = ''.join(sample(string.ascii_lowercase, lenght))
    return name


def create_files(count, name_lenght, extension):
    for i in range(count):
        with open(f'{create_name(name_lenght)}.{extension}', 'w', encoding='utf-8') as f:
            f.write('Hello')


def rename_files(digit_count, ext_original, ext_final, range_of: list, end_name=''):
    # p = Path(Path.cwd())
    number = 1
    for obj in os.listdir():
        name, ex = obj.split('.')
        if ex == ext_original:
            num_str = str(number)
            if len(num_str) < digit_count:
                for i in range(digit_count):
                    num_str = '0' + num_str
            name = name[range_of[0] - 1:range_of[1]] + end_name + num_str
            new_name = f'{name}.{ext_final}'
            os.rename(obj, new_name)
            number += 1


print(Path.cwd())
make_dir('new_dir_1')
create_files(2, 5, 'txt')
create_files(1, 4, 'xls')
print(os.listdir())
rename_files(2, 'txt', 'csv', [1, 3], 'NEW')
print(os.listdir())

# shutil.rmtree('new_dir_1')
#____________________________ВЫВОД___________________________________
# ['suco.xls', 'yagop.txt', 'zgxhc.txt'] - исходные
# ['suco.xls', 'yagNEW001.csv', 'zgxNEW002.csv'] - после обработки