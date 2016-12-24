import urllib.request
import re
import youtube_dl
import ytdl


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
    title = re.findall(b'data-title="(.*?)"', html)
    for a in shows: tvshows.append(site + a.decode())
    for b in title: tit.append(b.decode())


site = 'http://ellinofreneianet.gr/'
radiourl = site + 'radio/radio-shows-2.html'
tvurl = site + 'television/tv-shows.html'
radioshows = []
tvshows = []
tit = []
test = {}


def main():
    get_radio_show(radiourl)
    get_tv_show(tvurl)

    # TODO proper dl options listing
    # TODO fix tvdl in ydl_opts
    # TODO make it so it will iterate a list and dl all of them
    with youtube_dl.YoutubeDL(ytdl.ydl_opts) as ydl:
        ydl.download([radioshows[0]])

    # # testing
    # print(tvshows)
    # print(tit)
    for i in range(len(tvshows)):
        test[tvshows[i]] = tit[i]
    # print(test.keys(), test.values())


main()
