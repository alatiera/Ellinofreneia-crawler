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
    return showslist


def getTVShow(pageurl):
    """Gets the a url list of the episodes in the page"""
    # might also get the tittle and bind them with a Dict for later use
    page = urllib.request.urlopen(pageurl).read()
    # print(page.decode())
    shows = re.findall(b'href="/(television/tv-shows/video/\S+)"', page)
    # title = re.findall(b'data-title="(.*?)"', page)
    for a in shows: showslist.append(site + a.decode())
    # for b in title: tit.append(b.decode())
    return showslist


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


# restructure
def getshow(stype, limit):
    if stype == 'radio':
        count = 0
        l = showlimit(stype)
        while count <= l:
            print(radiourl + radioargs + str(count))
            getRadioShow(radiourl + radioargs + str(count))
            count += 11
        multidl(showslist[:limit])

    # elif stype == 'tv':
    #     getTVShow(tvurl)
    #     return tvshows[:limit]
    # elif stype == 'both':
    #     getRadioShow(radiourl)
    #     getTVShow(tvurl)
    #     return radioshows[:limit] + tvshows[:limit]
    else:
        print('unkown argument, exiting')
        exit()


def showlimit(stype):
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


# TODO auto navigation for full backlog download
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
    if len(argv) <= 1:
        stype = input("What type of content do you want:radio or tv or both? ")
        amount = input('Great! And how many episodes? ')
    else:
        stype = argv[1]
        amount = argv[2]
    getshow(stype, int(amount))


main()
