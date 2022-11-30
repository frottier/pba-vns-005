
# Tesseract

Benutzt wird Tesseract 4.

Befehl:

~~~

for file in *.tif; do tesseract -l deu --psm 6 --dpi 400 $file "$file""_ocr" ../skripte/tess_char.conf; done

~~~

Die Config-Datei `tess_char.conf` enthält die Liste der erlaubten Zeichen. Ferner können hier andere Optionen konfiguriert werden. Per Default schreibt _Tesseract_ an jedem Seitenende ein Form-Feed-Steuerzeichen. Das kann mit der Option `page_separator` geändert werden.

Beispielconfig:

~~~
tessedit_char_whitelist !"'(),-./0123456789:;=?ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyzÄÖÜßäöü
page_separator ---
~~~

Ungelöst: Wie übergibt man hier Steuerzeichen wie zB Newline? Geht das in der Config vllt gar nicht?