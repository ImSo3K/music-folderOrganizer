import os
import re
import shutil
import glob
import operator
from tinytag import TinyTag


def get_music_in_directory(path):
    return glob.glob(path + '*.mp3') + glob.glob(path + '*.m4a')


def add_artist_album_info():
    for i, file in enumerate(raw_file_names):
        tag = TinyTag.get(raw_file_names[i])
        raw_file_names[i] = (tag.artist, tag.album, file)
    return


def sort_raw_data():
    raw_file_names.sort(key=operator.itemgetter(1, 2))
    return


def initialize_sorted_list():
    album = []
    while raw_file_names:
        album_name = raw_file_names[0][1]

        while album_name == raw_file_names[1][1]:
            album.append(raw_file_names[0])
            raw_file_names.pop(0)
            if len(raw_file_names) == 1:
                break

        album.append(raw_file_names[0]) # special case for last song of each album
        raw_file_names.pop(0)
        sorted_music_info.append(album)
        album = []
    return


def move_to_folder():
    for album in sorted_music_info:
        tag = TinyTag.get(album[0][2])
        folder_name = f'{tag.artist} - {tag.album} ({tag.year.split("-",1)[0]})'
        folder_name = re.sub('[!@#$%^&*/?]', '', folder_name)

        if os.path.isdir(folder_name) is False:
            os.mkdir(folder_name)
            for song in album:
                shutil.move(song[2], folder_name)
    return


# testing purposes
def extract_from_directories():
    directories = glob.glob("*/")
    for directory in directories:
        files_to_extract = get_music_in_directory(directory)
        for file in files_to_extract:
            shutil.move(file, os.getcwd())
        os.rmdir(directory)


os.chdir('/home/sharon/Music/')
raw_file_names = get_music_in_directory('')
sorted_music_info = []
add_artist_album_info()
sort_raw_data()
archive = sorted_music_info
initialize_sorted_list()
move_to_folder()
# extract_from_directories()
