
# Tesseract

## aktuell

Benutzt wird Tesseract 5, derzeit in Ubuntu 22.10. Es hat sich gezeigt, dass die automatische Erkennung und Aufbereitung der Vorlagen oft besser funktioniert als die bisherige manuelle Aufbereitung mit Tesseract. Explizite Vorgaben mit `--psm` oder `--dpi` haben eher negative Auswirkungen auf die Erkennungsrate. 

Beispiel für das Kommando, so lange noch kein Skript existiert:

~~~

for file in ~/PBA/VNS-005/VNS-005_{152..160}.tif; do filename=$(echo $file | rev | cut -d '/' -f1 | rev); tesseract -l deu $file "$filename""_ocr" ../skripte/tess_char.conf; done

~~~

Das ist auszuführen im numerischen Zielverzeichnis des Git-Repos. Der Ordner nach _for file in_ enthält die Digitalisate der Vorlesung aus dem Archiv-Master. In den geschweiften Klammern werden die zum Vorlesungstermin gehörenden Dateien angegeben (hier VNS-005_152.tif bis VNS-005_160.tif).

Die Config-Datei `tess_char.conf` enthält die Liste der erlaubten Zeichen. Ferner können hier andere Optionen konfiguriert werden. Per Default schreibt _Tesseract_ an jedem Seitenende ein Form-Feed-Steuerzeichen. Das kann mit der Option `page_separator` geändert werden.

Beispielconfig:

~~~
tessedit_char_whitelist !"'(),-./0123456789:;=?ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyzÄÖÜßäöü
page_separator ---
~~~

Ungelöst: Wie übergibt man hier Steuerzeichen wie zB Newline? Geht das in der Config vllt gar nicht?

---

## veraltet

Benutzt wird Tesseract 4.

Befehl:

~~~

for file in *.tif; do tesseract -l deu --psm 6 --dpi 400 $file "$file""_ocr" ../skripte/tess_char.conf; done

~~~

