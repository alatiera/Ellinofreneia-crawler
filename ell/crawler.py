import urllib.request
import re
import youtube_dl
import ytdl
from sys import argv


def get_radio_show(url):
    """ Extract the urls as a list of the radio shows"""
    html = urllib.request.urlopen(url).read()
    shows = re.findall(b'meta\sproperty="og:url".*content="(.*)"', html)
    for i in shows:
        radioshows.append(i.decode())
        # print(i.decode())


def get_tv_show(url):
    """Gets the a url list of the episodes in the page"""
    # might also get the tittle and bind them with a Dict for later use
    html = urllib.request.urlopen(url).read()
    # print(html.decode())
    shows = re.findall(b'href="/(television/tv-shows/video/\S+)"', html)
    # title = re.findall(b'data-title="(.*?)"', html)
    for a in shows: tvshows.append(site + a.decode())
    # for b in title: tit.append(b.decode())


def get_tv_episode(url):
    """takes url and find the youtube url"""
    html = urllib.request.urlopen(url).read()
    episode = re.findall(b'src="(.+youtube\.com/watch.+)"', html)
    # print(episode[0].decode())
    return episode[0].decode()


def dl(url, opt):
    """Takes url as content location and opt as youtube_dl options"""
    with youtube_dl.YoutubeDL(opt) as ydl:
        try:
            print('downloading from: {}'.format(url))
            ydl.download([url])
        except KeyboardInterrupt:
            print('cancelling')
            exit()


def multidl(list, limit):
    """iterates a list of urls and passes them to dl()"""
    for i in list[:limit]:
        # figure what dl options to use
        if re.search('video', i):
            # yt_dl defaults to what it wants with empty {}
            ydl_opts = {}
            dl(get_tv_episode(i), ydl_opts)
        else:
            dl(i, ytdl.ydl_opts)


def getshow(stype):
    if stype == 'radio':
        get_radio_show(radiourl)
        return radioshows
    elif stype == 'tv':
        get_tv_show(tvurl)
        return tvshows
    elif stype == 'both':
        pass
    else:
        print('unkown argument, exiting')
        exit()


def media(stype, amount):
    multidl(getshow(stype), int(amount))


# TODO proper dl options listing
# TODO auto navigation for full backlog download
site = 'http://ellinofreneianet.gr/'
radiourl = site + 'radio/radio-shows-2.html'
tvurl = site + 'television/tv-shows.html'
radioshows = []
tvshows = []
# tit = []
# test = {}
# media('radio', '3')


def main():
    print(argv)
    if len(argv) <= 1:
        stype = input("What type of content do you want: radio or tv? ")
        amount = input('Great! And how many episodes? ')
        if amount == 'a' or 'all': amount = -1
    else:
        stype = argv[1]
        amount = argv[2]
    media(stype, amount)


main()
