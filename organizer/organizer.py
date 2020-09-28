import os
import glob
from tinytag import TinyTag


def move_to_folder():
    pass


def get_music_in_directory():
    return glob.glob('*.mp3') + glob.glob('*.m4a')


def sort_list_by_album():
    pass


os.chdir('/home/sharon/Music/')
music_file_names = get_music_in_directory()
music_file_paths = [path for path in music_file_names]
get_music_in_directory()
print(music_file_paths)
tag = TinyTag.get(music_file_names[0])
print(tag.artist)