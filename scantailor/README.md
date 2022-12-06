# ScanTailor XMLs

In diesem Ordner befinden sich ScanTailor-Projekt-Dateien. Darin sind die Einstellungen gespeichert, mit denen die jeweiligen Vorlagen bearbeitet wurden.

Sie werden in der Regel nach der OCR nicht mehr benötigt. Falls es dennoch nötig sein sollte: Bevor die Dateien lokal geöffnet werden können, müssen jeweils zwei Pfade darin per Hand angepasst werden.

Beispiel:

~~~
==> 01.ScanTailor <==
<project outputDirectory="[DURCH ZIELPFAD ERSETZEN]/01" layoutDirection="LTR" version="3">
  <directories>
    <directory id="1" path="[DURCH QUELLPFAD ERSETZEN]/VNS-005"/>
  </directories>
~~~

Als _outputDirectory_ kann ein beliebiges lokales Verzeichnis gesetzt werden. Dorthin werden die gerenderten Seiten als Tiff exportiert. Außerdem legt ScanTailopr ein _cache_-Verzeichnis an.

Als _path_ im Element _directory_ muss der Archivordner VNS-005 entpsrechend der lokalen Gegebenheiten lokalisiert werden. Die ScanTailor-Dateien beziehen sich auf die unkomprimierten Archivmaster und ergeben nur im Zusammenspiel mit diesen Sinn.

Leider sind ScanTailor-Projekt-Dateien nicht portabel konzipiert. Es gibt als Trostpflaster ein schwer durchschaubares Relinking-Tool, das sich automatisch öffnet, wenn die Pfade nicht mehr existieren.
