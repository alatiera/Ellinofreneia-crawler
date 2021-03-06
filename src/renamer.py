import re
from os import scandir, rename, getcwd


months = {
        'Ιανουαρίου': '01',
        'Φεβρουαρίου': '02',
        'Μαρτίου': '03',
        'Απριλίου': '04',
        'Μαΐου': '05',
        'Ιουνίου': '06',
        'Ιουλίου': '07',
        'Αυγούστου': '08',
        'Σεπτεμβρίου': '09',
        'Οκτωβρίου': '10',
        'Νοεμβρίου': '11',
        'Δεκεμβρίου': '12'
        }


def getMonth(title):
    for month in months.keys():
        if month in title:
            return months.get(month)
    return None


def getDate(fil):
    """Extracts and returns the date from file's title"""
    year = re.findall('\s([0-9]{4})', fil)[0]
    day = re.findall('\s(\d{1,2})\D{2}', fil)[0]
    if len(day) == 1:
        day = '0' + day
    # date = year + '-' + months.get(month, 'None') + '-' + day
    date = year + '-' + getMonth(fil) + '-' + day
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


def renamer(fil):
    try:
        rename(fil, getDate(fil) + ' - ' + getTitle(fil) + '.mp3')
        # print('done')
    except IndexError:
        print('Error with {}'.format(fil))


def main():
    path = getcwd()

    # TODO os.scandir() changed in python 3.6 and might need refactor
    ls = scandir(path)
    for i in ls:
        if re.search('^[0-9]+-[0-9]+-[0-9]+', i.name) and i.is_file():
            # name reversing
            # can also be used in opposite to keep only the date i[:13]
            # rename(i.name, i.name[13:])

            # print('alrdy good')
            pass
        elif i.is_file() and '.mp3' in i.name:
            renamer(i.name)
