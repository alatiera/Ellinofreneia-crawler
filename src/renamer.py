#!/usr/bin/env python3

import re
from os import listdir, path, rename


months = {
        'Ιανουαρίου': '01',
        'Φεβρουαρίου': '02',
        'Μαρτίου': '03',
        'Απριλίου': '04',
        'Μαΐου': '05',
        'Ιουνίου': '06',
        'Ιουλίου': '07',
        'Σεπτεμβρίου': '09',
        'Οκτωβρίου': '10',
        'Νοεμβρίου': '11',
        'Δεκεμβρίου': '12'
        }


def getDate(fil):
    """Extracts the date from file's title"""
    year = re.findall('\s([0-9]{4})', fil)[0]
    day = re.findall('\s(\d{1,2})\D{2}', fil)[0]
    month = fil.split()[5]
    if len(day) == 1:
        day = '0' + day
    date = year + '-' + months[month] + '-' + day
    return date


def renamer(date, fil):
    rename(fil, getDate(fil) + ' - ' + getTitle(fil) + '.mp3')
    print('done!')


def getTitle(fil):
    if re.search('^[0-9]+', fil):
        title = fil[13:-4].split('-')[0]
        # print(title.lstrip())
        return title.lstrip()
    else:
        title = fil[:-4].split('-')[0]
        return title.lstrip()


def main():
    ls = listdir(path='.')
    for i in ls:
        # print(path.realpath(i))
        if re.search('^[0-9]+-[0-9]+-[0-9]+', i):
            # name reversing
            # can also be used in opposite to keep only the date i[:13]
            # rename(i, i[13:])

            print('alrdy good')
        else:
            try:
                renamer(getDate(i), i)
            except IndexError:
                print('Non matching file')
                continue


main()
