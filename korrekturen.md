
# Korrekturen und Konventionen

Während der Korrektur der Textdateien bleiben die wesentlichen Merkmale der Vorlage erhalten:

* Jeder gescannten Seite entspricht eine Textdatei.
* Die erste Zeile der Vorlage entspricht Zeile 1 in der Textdatei.
* Zeilenumbrüche bleiben erhalten, Vorlage und Textdatei sind konkordant.
* Es werden Unicode-Schriftzeichen verwendet. Damit ist auch die Transkription handschriftlich eingefügter griechischer Termini möglich.
* Was nicht in Textdateien transkribiert werden kann, wird unter dem Haupttext für spätere Arbeitsschritte vermerkt. Gemeint sind z.B. Bilder (Tafelskizzen) oder Hinweise auf später zu klärende Fragen (in Kopien abgeschnittene Wörter oder andere Auffälligkeiten).


## Teilautomatische Korrektur

Vorgeschlagene Wortersetzungen mit einem Texteditor. Derzeit ist das Gedit, das als Rechtschreibkorrektur Enchant/Hunspell benutzt.

Später können aus korrigierten Vorlesungen Wortlisten generiert werden, die dann ihrerseits von Hunspell für bessere Vorschläge benutzt werden können.

##  Manuelle Korrektur

Die Korrektur sollte zunächst in GitHub ausgeführt werden. Dazu muss ein Account angelegt werden. 

Die gewünschte Textdatei wird einfach im Browser geöffnet. Es empfiehlt sich, die Vorlage für den visuellen Abgleich in einem Fenster, den Browser in einem anderen Fenster zu haben.

Das Ziel der Korrektur ist lediglich die Behebung der Mängel in der Texterkennung. Es geht also darum, dass falsch erkannte Worte und Zeichensalat durch die richtigen Worte ersetzt werden. Fehler der Vorlage werden nicht übernommen.

Was hier nicht zu tun ist: Korrekturschritte, die später viel effizienter mittels teilautomatischer Ersetzungen über den gesamtem Korpus durchgeführt werden können. Dazu zählen z.B. die Ersetzung von Minuszeichen durch Gedankenstriche, von Anführungszeichen durch ihre typographisch korrekten Pendants oder die Korrektur der teilweise als Trennungszeichen verwendeten Gleichheitszeichen. Auch regelmäßig falsch gesetzte Leerzeichen sind später mittels regulärer Ausdrücke sehr viel schneller zu korrigieren als in Handarbeit.






