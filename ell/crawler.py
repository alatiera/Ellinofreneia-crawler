import urllib.request
import re
import youtube_dl
import ytdl

# TODO +tv link
radiourl = 'http://www.ellinofreneianet.gr/radio/radio-shows-2.html'
radiohtml = urllib.request.urlopen(radiourl).read()
# print(radiohtml)
# print(type(radiohtml))

# look for content links
shows = re.findall(b'meta\sproperty="og:url".*content="(.*)"', radiohtml)
content = []

for i in shows:
    content.append(i.decode())
    print(i.decode())

# print(content)

# TODO proper dl options listing
with youtube_dl.YoutubeDL(ytdl.ydl_opts) as ydl:
    ydl.download([content[0]])
