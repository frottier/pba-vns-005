
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

### Technische Voraussetzungen und Arbeitsweise

Die Korrektur sollte zunächst in GitHub ausgeführt werden. Dazu muss ein Account angelegt werden. Die gewünschte Textdatei wird einfach im Browser geöffnet.

Für den visuellen Abgleich kann der Scan der Vorlage in einem eigenen Fenster links auf dem Bildschirm platziert werden, der Browser mit dem Text rechts.

Das Ziel der Korrektur ist lediglich die Behebung der Mängel in der Texterkennung. Es geht also darum, dass falsch erkannte Worte und Zeichensalat durch die richtigen Worte ersetzt werden. Fehler der Vorlage werden nicht übernommen. Der Grund für die zurückhaltene Vorgehensweise während dieses frühen Schritts in der Transkription ist der Erhalt der Umbrüche. Eine gleichzeitige Absatzformatierung würde die Möglichkeit des visuellen Abgleichs verbauen.

Was hier nicht zu tun ist: Korrekturschritte, die später viel effizienter mittels teilautomatischer Ersetzungen über den gesamtem Korpus durchgeführt werden können. Dazu zählen z.B. die Ersetzung von Minuszeichen durch Gedankenstriche, von Anführungszeichen durch ihre typographisch korrekten Pendants oder die Korrektur der teilweise als Trennungszeichen verwendeten Gleichheitszeichen. Auch regelmäßig falsch gesetzte Leerzeichen sind später mittels regulärer Ausdrücke sehr viel schneller zu korrigieren als in Handarbeit.

### Regeln für die Korrektur

Die Regeln sind selbstgesetzte Konventionen. Die Liste wird fortlaufend ergänzt, da während der Verarbeitung des Materials neue Fälle entdeckt werden.

* Die originale alte Rechtschreibung wird zunächst beibehalten.
* Offensichtliche Tippfehler in den Abschriften werden stillschweigend korrigiert.
* Offensichtliche Kommafehler in den Abschriften werden stillschweigend korrigiert.
* Offensichtlich fehlende Worte werden in eckigen Klammern ergänzt, z.B. [ist].
* Unterstreichungen in der Vorlage werden in der Regel ignoriert. Sofern damit Betonung (emphasis) gemeint ist, handelt es sich um eine subjektive Interpretation der Person, die das Typoskript erstellte — dies ist für uns nicht normativ, zumal es nicht konsistent in jedem Typoskript vorkommt. Ausnahmen sind als Markierung möglich (s.u.)
* Abkürzungen wie "d.h." etc. werden zunächst ohne trennendes Leerzeichen geschrieben. Dies entspricht überwiegend der Vorlage. Später kann typographisch korrekt ein geschütztes halbes Leerzeichen eingefügt werden.
* Es werden keine Tabulatoren benutzt. Einrückungen in der Vorlage werden als Leerzeichen ausgeführt.
* Per Hand in das Typoskript eingefügte altgriechische Buchstaben werden durch die korrekten Unicode-Zeichen ersetzt. Die OCR erkennt bewusst keine griechischen Zeichen.
* Lateinisch transkribierte altgriechische Terminii bleiben zunächst entsprechend der Vorlage erhalten. Sie werden aber markiert und später mit dem Vorlesungsmanuskript abgeglichen.

### Markierungen

-WIP-

Einige lokale Informationen können nicht direkt als Unicode abgebildet werden. Sofern in der weiteren Verarbeitung relevant, bedarf es definierter Methoden zur indirekten Abbildung.  
Wenn es möglich ist, halten wir uns dabei an Standards aus der Markdown-Syntax.

* Betonung
* Notiz für spätere Überprüfung (z.B. altgriechische Termini)
* Hinweis für Grafik/Bilder
* Transkription von Randnotizen etc.
* ...





