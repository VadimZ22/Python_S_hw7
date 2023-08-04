import itertools
import string
from random import randint, uniform, sample, shuffle, randbytes
from string import ascii_lowercase, ascii_letters
import os

def input_num(count, filename):
    with open (filename, 'a', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{randint(-1000, 1000)} | {uniform(-1000, 1000)} \n')

# input_num(5, 'example.txt')


vovel = 'йуеыаяиоэ'
consonant = 'цкнгшлрпвфмсчбх'

## string.ascii_lowercase
# a = randint(4,7)
# v = randint(1,a-2)
# x = sample(vovel, v)
# y = sample(consonant,a-v)
# s = x+y
# shuffle(s)
# print(''.join(s).title())
#
# with open('names.txt', 'a', encoding='utf-8') as f:
#     f.write(''.join(s).title() + '\n')

## def gen_name(vovel, consonant):


#_______________________________________________________________________
# names_size = len(list(1 for _ in open('names.txt')))
# ex_size = len(list(1 for _ in open('example.txt')))
# count = max(names_size, ex_size)
#
# with open('names.txt', 'r') as names,\
#         open('example.txt', 'r') as ex, \
#         open('res.txt', 'w') as res:
#     names_str = itertools.cycle(names.readlines())
#     ex_str = itertools.cycle(ex.readlines())
#     # print(next(names_str))
#     # print(next(ex_str))
#
#
#     for i in range(count):
#
#         ex_str1, ex_str2 = next(ex_str).split('|')
#         prod = float(ex_str1) * float(ex_str2)
#         if prod < 0:
#
#             res.write(f'{next(names_str).strip().lower()} {abs(prod)}\n')
#         else:
#             res.write(f'{next(names_str).strip().upper()} {round(prod)}\n')



def makefile(extension, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):

    names = set()
    while len(names) < count:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))
    for name in names:
        with open(f'{name}.{extension}', 'wb') as f:
            temp = randbytes(randint(min_bytes, max_bytes))
            f.write(temp)
            print(len(temp))


def makefiles(extensions):
    for extension, count in extensions.items():
        makefile(extension=extension, count=count)



def makefile_topath(path, extensions):
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    makefiles(extensions)
    os.chdir('../..')



def replace_files():
    for file in os.listdir():
        ext = file.split('.')[-1]
        if not os.path.exists(ext):
            os.mkdir(ext)
        os.replace(file, os.path.join(os.getcwd(), ext, file))


