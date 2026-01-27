'''
Übungsaufgabe: Längstes Wort (keine Dictionaries, nur Listen)
=========================

Ermitteln Sie die Länge und den Inhalt des längsten Worts in der definierten Zeichenkette
und geben Sie beide Informationen auf der Konsole aus.

* ZEIT: 
=======
15 Minuten
'''

loremipsum = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

aktuelles_wort = ""
aktuelle_laenge = 0

laengstes_wort = ""
laenge_laengstes_wort = 0

for buchstabe in loremipsum:
    
    if buchstabe != " ":
        aktuelles_wort += buchstabe
        aktuelle_laenge += 1
    else:
        if aktuelle_laenge > laenge_laengstes_wort:
            laengstes_wort = aktuelles_wort
            laenge_laengstes_wort = aktuelle_laenge
            
        aktuelles_wort = ""
        aktuelle_laenge = 0
        
print(f"Längstes Wort \"{laengstes_wort}\" der Länge {laenge_laengstes_wort}")