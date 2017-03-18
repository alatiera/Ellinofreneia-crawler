import json
from os import path


def load_config():
    """Loads configuration file"""
    with open('config.json') as conf:
        config = json.load(conf)
        return config


def config_existance():
    if not path.exists('config.json'):
        template = """{ "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192"
    }],
    "quiet": "true",
    "outtmpl": "%(title)s.%(ext)s"
    }"""
        with open('config.json', 'w') as conf:
            conf.write(template)
        return load_config()
    else:
        return load_config()
