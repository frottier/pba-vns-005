#!/usr/bin/env python3

# quick and dirty script to get the set of characters used in text files
# expects the target folder as positional parameter

import sys
import os

target_folder = sys.argv[1]

files = os.listdir(target_folder)

charlist = set()

for file in files:
    if file.endswith('txt'):
        with open(os.path.join(target_folder, file)) as txt:
            for line in txt:
                for char in line:
                    charlist.add(char)

for char in sorted(charlist):
    print(char, end='')

print()
