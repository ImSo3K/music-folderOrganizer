import os
import re
import shutil
import glob
import operator
from tinytag import TinyTag


def get_music_in_directory(path):
    return glob.glob(path + '*.mp3') + glob.glob(path + '*.m4a')


def add_artist_album_info():
    for i, file in enumerate(music_file_names):
        tag = TinyTag.get(music_file_names[i])
        music_file_names[i] = (tag.artist, tag.album, file)


def sort_list_by_album():
    music_file_names.sort(key=operator.itemgetter(1, 2))


def move_to_folder():
    i = 0
    while i < len(music_file_names):
        tag = TinyTag.get(music_file_names[i][2])
        folder_name = f'{tag.artist} - {tag.album} ({tag.year.split("-",1)[0]})'
        folder_name = re.sub('[!@#$/]', '', folder_name)

        if os.path.isdir(folder_name):
            continue
        else:
            os.mkdir(folder_name)
            while tag.album == music_file_names[i][1] and i < len(music_file_names):
                shutil.move(music_file_names[i][2], folder_name)
                i += 1


# testing purposes
def extract_from_directories():
    directories = glob.glob("*/")
    for directory in directories:
        files_to_extract = get_music_in_directory(directory)
        for file in files_to_extract:
            shutil.move(file, os.getcwd())


os.chdir('/home/sharon/Music/')
music_file_names = get_music_in_directory('')
#print(music_file_names)
# add_artist_album_info()
extract_from_directories()
# sort_list_by_album()
# move_to_folder()
