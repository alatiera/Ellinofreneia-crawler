# Ellinofreneia-crawler
Crawler of Ellinofreneianet.gr for offline content consumption

## Info:
While making this I found 2 rss feeds you probably will be better off using.
[radio](http://www.ellinofreneianet.gr/radio/radio-shows-2.feed?type=rss)
[tv](http://www.ellinofreneianet.gr/television/tv-shows.feed?type=rss)

Downloads are powered by [youtube_dl](https://github.com/rg3/youtube-dl/)

## Dependancies:
[youtube_dl](https://github.com/rg3/youtube-dl/)

## Usage:
crawler.py is the main executable and take 2 argumentrs

The 1st is the type of show you want.

The 2nd is how many episodes you want to download.

    python3 crawler.py <showtype> <episodes number>

showtype can be passed "radio" or "tv" or "both" as values
number can be any intiger

Files are downloaded on the folder the script executes

## Example:

    python3 crawler.py tv 2

This will download the 2 latest tv episodes

    python3 crawler.py radio 5

Downloads the 5 latest radioshows
