
# Tesseract

Benutzt wird Tesseract 4.

Befehl:

~~~

for file in *.tif; do tesseract -l deu --psm 6 --dpi 400 $file "$file""_ocr" ../skripte/tess_char.conf; done

~~~

Die Config-Datei `tess_char.conf` enthält die Liste der erlaubten Zeichen.