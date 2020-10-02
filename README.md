# music-folderOrganizer
## Introduction
Well I have an old PC and a very large Music folder, which means loading times are through the roof.
So becuase I was too lazy :sweat_smile: to create directories for each album and then move all those songs to that folder, I created this script which does it for me :joy:.
 
 ## Requirements
Developed on Python 3.8.0 but I'm pretty sure it will work on any version >= 3.5
 - I'm using [typing](https://docs.python.org/3/library/typing.html) which was introduced **in version 3.5.**

 - This script uses :clap: @devsnd :clap: library `tinytag` which fetches the meta-data from the media files, check his library out for more functionalities :heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark:

    - Repository Link : https://github.com/devsnd/tinytag

 ## Installation
Well this script uses only 1 package, so you either can `pip install tinytag` or `pip install -r requirements.txt`

## Known Bugs
~~There seems to be a little bug with directory names that have backslashes `\`, it's just about that regex expression which I'll fix.~~ - Fixed :ok_hand:

## Acknowledgments
 - [devsnd](https://github.com/devsnd), creator of tinytag library.
