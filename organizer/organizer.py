import os
from tinytag import TinyTag
tag = TinyTag.get('/home/sharon/Music/01 Irresistible.m4a')
print(tag.artist)
print(f'number of tracks: {tag.track_total}')
