# Ellinofreneia-crawler
Crawler of Ellinofreneianet.gr for offline content consumption

## Info:
While making this I found 2 rss feeds you probably will be better off using.

[radio](http://www.ellinofreneianet.gr/radio/radio-shows-2.feed?type=rss)

[tv](http://www.ellinofreneianet.gr/television/tv-shows.feed?type=rss)

## Dependancies:
[youtube_dl](https://github.com/rg3/youtube-dl/)

##Usage:
`./launcher.py [crawl] [rename] [organize]`

###Crawl:
crawl takes 2 arguments:

`./launcher.py crawl <type> <amount>`

####Examples:

`./launcher.py crawl radio 5`

Downloads the last 5 radioshows:

`./launcher.py crawl both 3`

Downloads the last 3 radio and last 3 tv shows

`./launcher.py crawl tv 4')`

Downloads the last 4 tv shows:

###Audio files specific:

###Rename:
`./launcher.py rename`

Rename the mp3 files based on their title.

###Organize:
`./launcher.py organize`

Organizes mp3s in a folder structure based on date extracted from the file
