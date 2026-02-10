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
# 1. Lösungsvariante
vokale_liste = ["e", "a", "i", "o", "u", "ü", "ö", "ä"]

# 2. Variante 
vokale_dict = {
    "e": "elewe",
    "a": "alewa",
    "i": "ilewi",
    "o": "olewo",
    "u": "ulewu",
    "ü": "ülewü",
    "ö": "ölewö",
    "ä": "älewä"
}

def loeffel_liste(eingabe):
    
    eingabe = eingabe.lower() # in Kleinbuchstaben umwandeln

    ausgabe = "" # Das ist eine Variable vom Datentyp String
    for buchstabe in eingabe: # in buchstabe steht dann der Reihe nach, z.B. "H", "a", "l"
        if buchstabe in vokale_liste: # Prüfen, ob mein aktueller Buchstabe in der Liste steht (obs ein Vokal ist)
            ausgabe += buchstabe + "lew" + buchstabe # Buchstabe "konvertieren"
        else:
            ausgabe += buchstabe # Buchstabe nicht verändern, sondern einfach anhängen

    return ausgabe # Also der konvertierte String wird hier zurückgegeben.


def loeffel_dict(eingabe):
    
    eingabe = eingabe.lower() # in Kleinbuchstaben umwandeln

    ausgabe = "" # Das ist eine Variable vom Datentyp String
    for buchstabe in eingabe: # in buchstabe steht dann der Reihe nach, z.B. "H", "a", "l"
        if buchstabe in vokale_dict:
            ausgabe += vokale_dict[buchstabe] # Wert an der Stelle buchstabe zurückliefern
        else:
            ausgabe += buchstabe

    return ausgabe # Also der konvertierte String wird hier zurückgegeben.

def loeffel_zusatzaufgabe(eingabe):
    
    eingabe = eingabe.lower()
    
    loeffelsprache = str()
    
    index = 0
    while index < len(eingabe) - 1:
        
        buchstabe = eingabe[index] # Buchstabe anhand von Index aus Eingabe-Zeichenkette extrahieren
        
        # Leerzeichen und andere Buchstaben einfach hinzufügen.
        if buchstabe not in vokale:
            loeffelsprache += buchstabe
            
        # Doppelte Vokale haben Vorrang und müssen zuerst überprüft werden.
        elif eingabe[index] == "e" and eingabe[index+1] == "i":
            loeffelsprache += "eilewei"
            index += 1
                
        elif eingabe[index] == "a" and eingabe[index+1] == "u":
            loeffelsprache += "aulewau"
            index += 1
            
        elif eingabe[index] == "i" and eingabe[index+1] == "e":
            loeffelsprache += "ielewie"
            index += 1
        
        elif eingabe[index] == "e" and eingabe[index+1] == "u":
            loeffelsprache += "euleweu"
            index += 1
                
        elif buchstabe in vokale: # Einfache Vokale übersetzen
            loeffelsprache += buchstabe + "lew" + buchstabe
            
        index += 1
            
    # Letztes Zeichen nochmal separat überprüfen (könnte ja ein einfacher Vokal sein)
    if eingabe[-1] in vokale:
        loeffelsprache += eingabe[-1] + "lew" + eingabe[-1]
            
    return loeffelsprache

print(loeffel_liste("Hallo"))
print(loeffel_dict("Hallo"))
#print(loeffel("Verstehst du Deutsch?"))               
      
            


    
        