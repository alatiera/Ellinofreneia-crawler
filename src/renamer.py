#!/usr/bin/env python3

import re
from os import listdir, rename


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
    """Extracts and returns the date from file's title"""
    year = re.findall('\s([0-9]{4})', fil)[0]
    day = re.findall('\s(\d{1,2})\D{2}', fil)[0]
    month = fil.split()[5]
    if len(day) == 1:
        day = '0' + day
    date = year + '-' + months[month] + '-' + day
    return date


def getTitle(fil):
    """Extracts and returns a stripped tittle from file's dates"""
    if re.search('^[0-9]+', fil):
        title = fil[13:-4].split('-')[0]
        # print(title.lstrip())
        return title.lstrip()
    else:
        title = fil[:-4].split('-')[0]
        return title.lstrip()


def getYear(fil):
    """Extracts the year from the file"""
    if re.search('^[0-9]+', fil):
        year = fil[:4]
        # print(year)
        return year
    else:
        try:
            year = getDate(fil)[:4]
            # print(year)
            return year
        except IndexError:
            pass


def renamer(date, fil):
    rename(fil, getDate(fil) + ' - ' + getTitle(fil) + '.mp3')
    print('done!')


def main():
    ls = listdir(path='.')
    for i in ls:
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


# main()
