#!/usr/bin/env python3

import os
import re


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
    # fil at the end can be replaced with '.mp3')
    os.rename(fil, date + ' - ' + fil)
    print('done!')


def main():
    ls = os.listdir(path='.')
    for i in ls:
        if re.search('^[0-9]+-[0-9]+-[0-9]+', i):
            # name reversing
            # can also be used in opposite to keep only the date
            # os.rename(i, i[13:])

            print('alrdy good')
        else:
            try:
                renamer(getDate(i), i)
            except IndexError:
                print('Non matching file')
                continue


main()
