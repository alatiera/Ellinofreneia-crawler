import shutil
from renamer import getYear
from os import path, makedirs, getcwd, scandir


def move_file(fil, dest):
    filepath = path.realpath(fil)
    shutil.move(filepath, dest)


def test_dir(src):
    """Checks if folder exists and creates it if not"""
    # print(src)
    if path.isdir(src) is True:
        # print('path {} alrdy exists'.format(src))
        pass
    else:
        makedirs(src)
        print('folder {} created'.format(src))
    return src


def organize(fil):
    year = getYear(fil)
    defpath = path.join(getcwd(), 'radio')
    if year is None:
        print("Couldn't extract year")
        pass
    else:
        destination = path.join(test_dir(defpath), year)
        test_dir(destination)
        print('file({}) set to move to: {}'.format(fil, destination))
        try:
            move_file(fil, path.join(destination, fil))
        except shutil.Error as serr:
            print('Shutil Error: {}'.format(serr))


def main():
    ls = scandir(path='.')
    for i in ls:
        if i.is_file() and '.mp3' in i.name:
            organize(i.name)
        else:
            print('invalid file')
