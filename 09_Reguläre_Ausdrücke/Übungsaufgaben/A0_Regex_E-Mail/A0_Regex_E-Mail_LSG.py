"""
Übungsaufgabe: E-Mail-Adresse erkennen
======================================
Ziel dieser Aufgabe ist das Herausfiltern von bestimmten E-Mail-Adressen aus einem korrupten Textdokument.

Gegeben ist das Textdokument mail_addresses.txt mit E-Mail-Adressen. 
Leider haben sich ein paar fehlerhafte Zeilen eingeschlichen. 
Sie müssen herausfinden, welche Zeilen überhaupt eine E-Mail-Adresse darstellen… 

Die gesuchten E-Mail-Adressen haben immer das folgende Format: 
- Für die drei Zeichen vor dem Klammeraffen @ soll folgendes gelten: 
    - Das erste der drei Zeichen, das keine Ziffer (0-9) ist 
    - Die folgenden zwei Zeichen, die entweder Buchstabe, Ziffer oder der Unterstrich sind
- Es folgt der Klammeraffe @
- Die E-Mail-Adressen sollen alle mit der Domain bsz-neumarkt.de enden

HINWEIS: Nutzen Sie als Hilfestellung Tabelle 7-1 im Kapitel "Character Classes" der folgenden Website:
https://automatetheboringstuff.com/2e/chapter7/

Speichern Sie die relevanten E-Mail-Adressen in einer separaten Datei ab.

ZUSATZAUFGABE:
Geben Sie den Inhalt vor dem Klammeraffen @ während des Programmablaufs zusätzlich auf der Konsole aus.

Zeit: 20 Minuten, Einzelarbeit
"""
import re

eingabe_zeilen = list()
gefilterte_zeilen = list()

# Funktion zum Prüfen einer Zeile 
def ist_email_ok(zeile):
    
    # Wir brauchen erstmal die Compile-Funktion, also unser Muster:
    email_muster = re.compile(r"(\D\w\w)@bsz-neumarkt.de")
    gefundes_muster = email_muster.search(zeile)
    
    if gefundes_muster != None: # Muster wurde gefunden in dieser Zeile
        print(gefundes_muster.group(1)) # 1 liefert die 1. Gruppe
        return True
    else:
        return False

# Öffnen und lesen eines Dokuments
with open("mail_addresses.txt", "r") as doc:
    zeilen = doc.readlines()
    
    for zeile in zeilen:
        eingabe_zeilen.append(zeile)
        
        if ist_email_ok(zeile.strip()): # strip() löscht unnötige Zeichen am Ende einer Zeile
            gefilterte_zeilen.append(zeile)
        else:
            # Das wäre eine nicht korrekte Zeile: überspringen
            pass
            
# Ausgabedatei öffnen und beschreiben
with open("korrekte_emails.txt", "w") as doc: # Name für doc ist frei wählbar
    for zeile in gefilterte_zeilen:
        doc.write(zeile + "\n")
        
        
        

