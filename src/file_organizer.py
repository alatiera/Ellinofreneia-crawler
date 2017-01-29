import shutil
from renamer import getYear
from os import path, mkdir, getcwd
from os import listdir


def test_dir(src):
    if path.exists(src) is True:
        pass
        # print('path {} alrdy exists'.format(src))
    else:
        mkdir(src)
        print('folder {} created'.format(src))


def move_file(fil, dest):
    filepath = path.realpath(fil)
    shutil.move(filepath, dest)


def organize(fil):
    year = getYear(fil)
    destination = path.join(getcwd(), year)
    print('file set to move to: ', destination)
    test_dir(destination)
    try:
        move_file(fil, destination)
    except shutil.Error as serr:
        print('Shutil Error: {}'.format(serr))


def main():
    ls = listdir(path='.')
    for i in ls:
        if '.mp3' in i:
            organize(i)
        else:
            print('file error')


# TODO remove all the main() calls and make a seperate launcher
main()

# test_dir(path.join(getcwd(), '2017'))
