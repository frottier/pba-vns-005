#!/bin/bash

# positional parameters: input folder should contain text files that no longer
# contain any hyphenations. output of this script is the vocabulary file, an
# uncurated list of words from the input text files.

input_folder=$1
voc_file=$2

for textfile in "$input_folder"/*.txt; do
  cat "$textfile" | tr ' ' '\n' | tr -d '[:punct:]' | sort -u >> "$voc_file"
done

