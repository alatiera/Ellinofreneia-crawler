#!/usr/bin/env python3

import crawler
import renamer
import file_organizer
from sys import argv


# TODO refactor the argv parsing
def main():

    if len(argv) == 1 or len(argv) > 4 or argv[1] == '--help' or argv[1] == '-h':
        print("""
                Usage: ./launcher.py [crawl] [rename] [organize]

                crawl <option> <option>
                example:
                    ./launcher.py crawl tv 4')

                Audio files specific:
                rename
                    ./launcher.py rename
                Renames the mp3 files based on their title.

                organize
                    ./launcher.py organize
                Organizes mp3s in a folder structure based on date extracted from the file

                Before:
                file1.mp3
                file2.mp3

                After
                radio               :folder
                |---year            :folder
                    |--file1.mp3    :file
                |---diffyear        :folder
                    |--file2.mp3    :file
                """)

    # print(argv)
    elif argv[1] == 'crawl':
        if len(argv) == 4:
            # print(argv)
            stype = argv[2]
            amount = argv[3]
            if stype == 'both':
                crawler.getshow('radio', int(amount))
                crawler.getshow('tv', int(amount))
            else:
                crawler.getshow(stype, int(amount))
        else:
            print('Usage:\n'
                  './launcher.py crawl <type> <amount>\n'
                  'Example:\n'
                  '\nDownloads the last 5 radioshows:\n'
                  '\t./launcher.py crawl radio 5\n'
                  '\nDownloads the last 3 radio and last 3 tv shows\n'
                  '\t./launcher.py crawl both 3')

    elif argv[1] == 'rename':
        if len(argv) >= 3 and argv[2] == '-r':
            renamer.main(recursive=True)
        else:
            renamer.main()
        print(argv)

    elif argv[1] == 'organize':
        file_organizer.main()


main()
