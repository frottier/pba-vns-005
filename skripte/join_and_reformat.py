#!/usr/bin/env python3

import sys
import os

input_folder = sys.argv[1]
output_folder = sys.argv[2]

print(f'Reading files from {input_folder}')
print(f'Writing output to {output_folder}')

# get the input files (one file per page)
input_files = []
for file in os.listdir(input_folder):
    if file.endswith('.txt'):
        input_files.append(file)
input_files = sorted(input_files)

# join input files in list of lines. start by adding the source id.
# ignore additions at the bottom of the page.
joined_lines = []
for file in input_files:
    with open(os.path.join(input_folder, file), 'r') as textfile:
        current_page = []
        source_id = file.split('.')[0]
        current_page.append(f'[SOURCE_ID:{source_id}]\n')
        for line in textfile:
            current_page.append(line)
        for index, line in enumerate(current_page):
            if line.isspace() and current_page[index + 1] == '———\n':
                break
            else:
                joined_lines.append(line)

# make paragraphs by eliminating newlines when appropriate.
paragraphs = []
paragraph = ''
for index, line in enumerate(joined_lines):
    if line.isspace():
        paragraphs.append('\n')
        paragraph = ''
    elif line.endswith('.\n') or joined_lines[index + 1].isspace():
        paragraph = ' '.join([paragraph, line])
        paragraphs.append(paragraph)
        paragraph = ''
    else:
        if len(paragraph) == 0:
            paragraph = line.rstrip()
        else:
            paragraph = ' '.join([paragraph, line.rstrip()])

for p in paragraphs:
    print(p)

