class MyLogger(object):
    """
    https://github.com/rg3/youtube-dl/blob/19f37ce4b1e4251a3f53f8a5d3d0605d2526bc81/README.md#embedding-youtube-dl
    """

    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


# TODO expose ydl_opts to a config.json file
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
