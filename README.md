# Ellinofreneia-crawler
dler of ellinofreneianet.gr website

## Info:
Unoficial crawler meant for offline content consumption.

There also 2 hidden rss feeds on the site but they link to soundcloud/youtube.

[radio](http://www.ellinofreneianet.gr/radio/radio-shows-2.feed?type=rss)

[tv](http://www.ellinofreneianet.gr/television/tv-shows.feed?type=rss)


## Dependancies:
[youtube_dl](https://github.com/rg3/youtube-dl/)
[requests](http://docs.python-requests.org/en/master/)

##Usage:
`./launcher.py [dl] [rename] [organize]`

####Examples:

`./launcher.py dl 5 -a`

Downloads the last 5 radioshows:

`./launcher.py dl 3`

Downloads the last 3 radio and last 3 tv shows

`./launcher.py dl 4 -v`

Downloads the last 4 tv shows:

###Audio files specific:

###Rename:
`./launcher.py rename`

Rename the mp3 files based on their title.

`./launcher.py rename -r`
If passed with `-r` it will be performed recursivly

###Organize:
`./launcher.py organize`

Organizes mp3s in a folder structure based on date extracted from the file

## ./launcher.py --help :
```
usage: launcher.py [-h] {download,dl,crawl,rename,sort,organize} ...

positional arguments:
  {download,dl,crawl,rename,sort,organize}
    download (dl, crawl)
                        Downloads the shows
    rename              Renames radio shows to sort properly
    sort (organize)     Organizes mp3s in a folder structure based on date
                        extracted from the file

optional arguments:
  -h, --help            show this help message and exit
```
