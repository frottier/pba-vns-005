#! /bin/bash

# Dieses Skript ersetzt falsch oder gar nicht gesetzte Leerzeichen in Text-Dateien.
# Input: Positionsparameter mit dem Zielordner, z.B.
#
#     $ ./fix_spaces.sh ../14
#
# Änderungen:
# 
# 1. Satzzeichen zwischen Wörtern ohne Leerzeichen: Leerzeichen wird nach
#    dem Satzzeichen eingefügt.
# 2. Satzzeichen folgt auf Leerzeichen: wird umgekehrt (Satzz./Leerz.)
# 
# Geändert werden alle Dateien in dem angegebenen Ordner. Es werden Backups angelegt.

target_folder=$1

if [ ! -d "$target_folder" ]; then
  echo "Target folder does not exist."
  exit 1
fi

for file in "$target_folder"/*.txt; do
  echo "Working on $file"
  sed -i.bak -E 's/([[:alpha:]])([\.,:;])([[:alpha:]])/\1\2 \3/g;s/ ,/, /g;s/ \./\. /g' "$file"
done

