#!/usr/bin/env python3

import crawler
import renamer
import file_organizer
import argparse


def opts():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    download = subparsers.add_parser('download', help='Downloads the shows',
                                     aliases=['dl', 'crawl'])

    download.add_argument('num', help='Number of backlog you want to download',
                          type=int)

    showtype = download.add_mutually_exclusive_group()
    showtype.add_argument('-v', '--video-only', help='Video only',
                          action='store_true')

    showtype.add_argument('-a', '--audio-only', help='Audio only',
                          action='store_true')

    rename = subparsers.add_parser('rename',
                                   help='Renames radio shows to sort properly')
    rename.add_argument('ren', action='store_true')
    # rename.add_argument('-r', '--recursive', help='Executes recursivly',
    #                     action='store_true')

    org = subparsers.add_parser('sort', aliases=['organize'], help="""Organizes
    mp3s in a folder structure based on date extracted from the file""")
    org.add_argument('sort', action='store_true')

    args = parser.parse_args()
    return args


def main():
    args = opts()
    if 'num' in args:
        if args.audio_only:
            crawler.getshow('radio', args.num)

        elif args.video_only:
            crawler.getshow('tv', args.num)

        else:
            crawler.getshow('radio', args.num)
            crawler.getshow('tv', args.num)

    if 'ren' in args:
        # if args.recursive:
        #     renamer.main(recursive=True)
        # else:
        renamer.main()

    if 'sort' in args:
        file_organizer.main()

if __name__ == '__main__':
    main()
