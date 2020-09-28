import os
import glob
import operator
from tinytag import TinyTag


def get_music_in_directory():
    return glob.glob('*.mp3') + glob.glob('*.m4a')


def add_artist_album_info():
    for i, file in enumerate(music_file_names):
        tag = TinyTag.get(music_file_names[i])
        music_file_names[i] = (tag.artist, tag.album, file)


def sort_list_by_album():
    music_file_names.sort(key=operator.itemgetter(1, 2))


def move_to_folder():
    pass


os.chdir('/home/sharon/Music/')
music_file_names = get_music_in_directory()
add_artist_album_info()
sort_list_by_album()
print(music_file_names)
