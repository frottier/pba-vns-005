
# Tesseract

Benutzt wird Tesseract 4.

Befehl:

~~~

for file in *.tif; do tesseract -l deu --psm 6 --dpi 400 $file "$file""_ocr"; done

~~~


