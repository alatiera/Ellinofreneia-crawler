#!/usr/bin/env python3

import urllib.request
import re
import youtube_dl
import ytdl
from sys import argv


def getRadioShow(pageurl):
    """ Extract the urls as a list of the radio shows"""
    page = urllib.request.urlopen(pageurl).read()
    shows = re.findall(b'meta\sproperty="og:url".*content="(.*)"', page)
    for i in shows:
        showslist.append(i.decode())
        # print(i.decode())


def getTVShow(pageurl):
    """Gets the a url list of the episodes in the page"""
    page = urllib.request.urlopen(pageurl).read()
    # print(page.decode())
    shows = re.findall(b'href="/(television/tv-shows/video/\S+)"', page)
    for a in shows:
        showslist.append(site + a.decode())
        # print(a.decode())


def getTVEpisode(pageurl):
    """takes url and find the youtube url"""
    page = urllib.request.urlopen(pageurl).read()
    episode = re.findall(b'src="(.+youtube\.com/watch.+)"', page)
    return episode[0].decode()


def dl(contenturl, opt):
    """Takes url as content location and opt as youtube_dl options"""
    with youtube_dl.YoutubeDL(opt) as ydl:
        try:
            print('downloading from: {}'.format(contenturl))
            ydl.download([contenturl])
        except KeyboardInterrupt:
            print('\ncancelling')
            exit()


def multidl(list):
    """iterates a list of urls and passes them to dl()"""
    for i in list:
        # figure what dl options to use
        if re.search('video', i):
            # yt_dl defaults to what it wants with empty {}
            ydl_opts = {}
            dl(getTVEpisode(i), ydl_opts)
        else:
            dl(i, ytdl.ydl_opts)


def getshow(stype, limit):
    count = 0
    showslist.clear()
    l = showlimit(stype)
    # print(l)

    # ensures that you dont fetch the whole backlog if not need
    while limit >= len(showslist) and count <= l:
        # print(showslist)
        count = backlog(stype, count)

    multidl(showslist[:limit])


def backlog(stype, count):
    """Points to diff backlogs to fetch"""
    if stype == 'radio':
        getRadioShow(radiourl + radioargs + str(count))
        count += 11
        return count
    elif stype == 'tv':
        getTVShow(tvurl + tvargs + str(count))
        count += 21
        return count
    else:
        print('unkown argument, exiting')
        exit()


def showlimit(stype):
    """Passes the page and the type to limit() """
    if stype == 'radio':
        a = urllib.request.urlopen(radiourl).read()
        page = a.decode()
        return limit(page)
    elif stype == 'tv':
        a = urllib.request.urlopen(tvurl).read()
        page = a.decode()
        return limit(page)


def limit(pageurl):
    """Finds the current '?start=' limit from the page"""
    b = re.findall('Τέλος.*start=([0-9]+)', pageurl)
    slimit = int(b[0])
    # print(type(slimit))
    return slimit


site = 'http://ellinofreneianet.gr/'
radiourl = site + 'radio/radio-shows-2.html'
tvurl = site + 'television/tv-shows.html'

# every page has limit=X elements(shows) and start defines the position
radioargs = '?limit=11&start='
tvargs = '?limit=21&start='

showslist = []
# tit = []
# test = {}


def main():
    if len(argv) != 3 or argv[1] == "-h" or argv[1] == "--help":
        print('Usage:\n'
              '<script> <type> <amount>\n'
              'Example:\n'
              './crawler.py tv 2\n'
              './crawler.py radio 5\n')
    else:
        stype = argv[1]
        amount = argv[2]
        if stype == 'both':
            getshow('radio', int(amount))
            getshow('tv', int(amount))
        else:
            getshow(stype, int(amount))


main()
