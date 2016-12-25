# Ellinofreneia-crawler
Crawler of Ellinofreneianet.gr for offline content consumption

## Info:
While making this I found 2 rss feeds you probably will be better off using.
[radio] (http://www.ellinofreneianet.gr/radio/radio-shows-2.feed?type=rss)
[tv] (http://www.ellinofreneianet.gr/television/tv-shows.feed?type=rss)

Downloads are powered by [youtube_dl] (https://github.com/rg3/youtube-dl/)

## Dependancies:
[youtube_dl] (https://github.com/rg3/youtube-dl/)

## Usage:
crawler.py is the main executable and take 2 argument or run without and get promted for the arguments.
The 1st is the type of show you want.
The 2nd is how many episodes you want to download.(Currently only supports last X episodes)

    ./crawler.py <showtype> <episodes number>

showtype take either "radio" or "tv" as values
number can be any intiger, negative numbers act as infinity

Filesa re downloaded on the folder the script executes

## Example:
    ./crawler.py tv 2
This will download the 2 latest tv episodes

    ./crawler.py radio 5
Downloads the 5 latest radioshows
