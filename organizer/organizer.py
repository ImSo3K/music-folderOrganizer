# MIT License

# Copyright (c) 2020 Sharon Yaroshetsky

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
A module that takes your music messy music folder with bunch of song files,
and creates directory for each album and then moves them there.
"""

import os
import re
import shutil
import glob
import operator
from pathlib import Path
from tinytag import TinyTag


def get_music_in_directory(path) -> list:
    """gets all the music file names in the directory (mp3 and m4a).

    Args:
        path (string): the Music folder path.

    Returns:
        list: a list of strings that represent the file names.
    """
    return glob.glob(path + '*.mp3') + glob.glob(path + '*.m4a')


def add_artist_album_info() -> None:
    """
    organizes the raw list of string (raw_file_names) as a raw list of tuples
    that consist (song.artist, song.album, file_name).
    """
    for i, file in enumerate(raw_file_names):
        tag = TinyTag.get(raw_file_names[i])
        raw_file_names[i] = (tag.artist, tag.album, file)


def sort_raw_data() -> None:
    """
    sorts the raw list of tuples (raw_file_names) in an ascending order
    with priority to album, and then file name.
    """
    raw_file_names.sort(key=operator.itemgetter(1, 2))


def initialize_sorted_list() -> None:
    """
    takes the raw list of tuples (raw_file_names) and extracts each album data to a list
    which is added to the sorted_music_info list.
    """
    album = []
    for file in raw_file_names:
        album_name = file[1]

        if raw_file_names.index(file) + 1 == len(raw_file_names):
            album.append(file)
            sorted_music_info.append(album)

        elif album_name == raw_file_names[raw_file_names.index(file) + 1][1]:
            album.append(file)

        else:
            album.append(file)
            sorted_music_info.append(album)
            album = []


def move_to_directory() -> None:
    """
    creates a directory to each album by the format of : "artist + album + year"
    and then moves each song to its album directory.
    """
    for album in sorted_music_info:
        tag = TinyTag.get(album[0][2])
        folder_name = f'{tag.artist} - {tag.album} ({tag.year.split("-",1)[0]})'
        folder_name = re.sub('[!@#$%^&*/?"<:>|\\\\]', '', folder_name)

        if os.path.isdir(folder_name) is False:
            os.mkdir(folder_name)
            for song in album:
                shutil.move(song[2], folder_name)


def extract_from_directories():
    """
    does the exact opposite job from move_to_directory() (with directory removal)
    mainly for testing purposes.
    """
    directories = glob.glob("*/")
    for directory in directories:
        files_to_extract = get_music_in_directory(directory)
        for file in files_to_extract:
            shutil.move(file, os.getcwd())
        os.rmdir(directory)


os.chdir(f'{Path.home()}/Music/')
raw_file_names = get_music_in_directory('')
sorted_music_info = []
add_artist_album_info()
sort_raw_data()
initialize_sorted_list()
move_to_directory()
# extract_from_directories()
