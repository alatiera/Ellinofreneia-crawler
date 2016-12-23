import urllib.request
import re

# TODO +tv link
radiourl = 'http://www.ellinofreneianet.gr/radio/radio-shows-2.html'
radiohtml = urllib.request.urlopen(radiourl).read()
# print(radiohtml)
# print(type(radiohtml))

# look for content links
shows = re.findall(b'meta\sproperty="og:url".*content="(.*)"', radiohtml)
for show in shows:
    print(show.decode())
