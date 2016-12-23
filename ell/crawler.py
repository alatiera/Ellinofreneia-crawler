import urllib.request
import re
import youtube_dl
import ytdl


def get_radio_show(url):
    """ Extract the urls of the radio shows"""
    html = urllib.request.urlopen(url).read()
    shows = re.findall(b'meta\sproperty="og:url".*content="(.*)"', html)
    for i in shows:
        radioshows.append(i.decode())
        # print(i.decode())


def get_tv_show(url):
    html = urllib.request.urlopen(url).read()
    # print(html.decode())
    # TODO extract episode title also
    shows = re.findall(b'href="/(television/tv-shows/video/\S+")', html)
    for i in shows:
        tvshows.append(site + i.decode())
        # print(i.decode())


# TODO +tv link
site = 'http://ellinofreneianet.gr/'
radiourl = 'http://www.ellinofreneianet.gr/radio/radio-shows-2.html'
tvurl = 'http://ellinofreneianet.gr/television/tv-shows.html'
radioshows = []
tvshows = []


def main():
    get_radio_show(radiourl)
    get_tv_show(tvurl)

    # TODO proper dl options listing
    # TODO fix tvdl in ydl_opts
    with youtube_dl.YoutubeDL(ytdl.ydl_opts) as ydl:
        ydl.download([radioshows[0]])

    # # testing
    # for i in tvshows:
    #     print(i)



main()
