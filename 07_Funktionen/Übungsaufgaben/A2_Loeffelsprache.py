"""
Aufgabe: Löffelsprache
======================

Auch für diejenigen, die bereits aus dem Alter heraus sind, in dem sie sich mit Freunden
gerne in einer Geheimsprache unterhalten, sollte die folgende Aufgabe interessant sein:

Zu schreiben ist eine Funktion, die den String, den sie als Eingabe erhält, 
in die sogenannte Löffelsprache übersetzt.

"Hallo" -> "Halewallolewo"
"Verstehst du Deutsch?" -> "velewerstelewehst dulewu deuleweutsch?"

Die Codierung erfolgt nach folgenden Regeln: 
* Immer, wenn ein Vokal vorkommt, wird dieser verdoppelt und dazwischen ein vorher festgelegter String gesetzt.

Damit sieht die Umsetzung wie folgt aus:

e = elewe
a = alewa
i = ilewi
o = olewo
u = ulewu
ü = ülewü
ö = ölewö
ä = älewä

Der Einfachheit halber wandeln wir den String vor der Kodierung in Kleinbuchstaben um, 
damit wir keine Großbuchstabenvokale behandeln müssen.

ZUSATZAUFGABE (SCHWIERIG)
===========================

* Verbindungen von zwei Vokalen (z.B. "au") sollen wie ein einziger Vokal betrachtet werden:

ei = eilewei
au = aulewau
ie = ielewie
eu = euleweu

Zeit: 15 Minuten

"""



vokale_liste = ["e", "a", "i", "o", "u", "ü", "ö", "ä"]

def loeffel(eingabe):
    pass

print(loeffel("Hallo"))
#print(loeffel("Verstehst du Deutsch?"))               
      
            


    
        