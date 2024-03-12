#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import argparse


class ObsidianParser:
    prog = re.compile(r'\|(.*)\|(.*)\|')

    def __init__(self, file: str):
        self._file = file

    def parse(self):
        with open(self._file, 'r') as file:
            lines = file.readlines()
        for line in lines:
            result = self.prog.match(line)
            if result:
                ang: str = result.group(1).strip()
                pol: str = result.group(2).strip()
                if ang.lower() == "angielski" or pol.lower == "polski" or ang == "----" or pol == "----":
                    continue
                print(f"{ang};{pol}")


def parse_args():
    parser = argparse.ArgumentParser(description='Parse Obsidian notes')
    parser.add_argument('file', type=str, help='The file to parse')
    return parser.parse_args()


def main():
    args = parse_args()
    parser = ObsidianParser(args.file)
    parser.parse()


if __name__ == '__main__':
    main()
