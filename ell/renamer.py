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


def getDate(a):
    try:
        year = re.findall('\s([0-9]{4})', a)[0]
        date = re.findall('\s(\d{1,2})\D{2}', a)[0]
        month = a.split()[5]
        if len(date) == 1:
            date = '0' + date
        # a at the end can be replaced with '.mp3')
        os.rename(a, year + '-' + months[month] + '-' + date + ' ' + a)
    except IndexError:
        print('Non matching file')


def main():
    c = os.listdir(path='.')
    for i in c:
        if re.search('^[0-9]+-[0-9]+-[0-9]+', i):
            # name reversing
            # can also be used in opposite to keep only the date
            # os.rename(i, i[10:])

            print('alrdy good')
            continue
        else:
            getDate(i)


main()
