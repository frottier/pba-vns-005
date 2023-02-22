#!/usr/bin/env python3

import os
import sys
import re


# input and output
input_file = sys.argv[1]
if not os.path.isfile(input_file):
    print('Falsche Eingabedatei. Syntax: ./typo_replace.py path/to/inputfile')
    sys.exit(1)

# parameters
context_length = 40
replacements = {'HYPHEN-MINUS': r'\s-\s',
                'QUOTATION MARK open': r'(^|\s)"',
                'QUOTATION MARK close': r'\S"'}

def show_match_context(txt_stream, start, end):

    """Print match and context in text."""
    
    pos_max = len(txt_stream) - 1
    pos_min = 0
    con_start = max(pos_min, start - context_length)
    con_end = min(pos_max, end + context_length)
    print(f'{txt_stream[con_start:start]}'
          f'\033[01m{txt_stream[start:end]}\033[0m'
          f'{txt_stream[end:con_end]}')


# read the text file
with open(input_file, 'r') as input_text:
    text = input_text.read()

for match_case in replacements:
    pattern = replacements[match_case]
    print(f'###  {match_case}  ###\n')

    for occurance in re.finditer(pattern, text):
        start, end = occurance.span()
        the_match = occurance.group(0)
        if match_case == 'HYPHEN-MINUS':
            sub_text = text[:start] + the_match.replace('-', '–') + text[start+3:]
        elif match_case == 'QUOTATION MARK open':
            sub_text = text[:start] + the_match.replace('"', '„') + text[start+2:]
        elif match_case == 'QUOTATION MARK close':
            sub_text = text[:start] + the_match.replace('"', '“') + text[start+2:]
        show_match_context(text, start, end)
        show_match_context(sub_text, start, end)
        
        input('? j/n')


print(text)

