import re 

win_codes = list()

def is_win_code(text):

    # Anlegen eines Regex-Objekts mit unserem Muster (Pattern).
    # TODO: Muster um Gruppen ergänzen
    win_code_pattern_re = re.compile(r"\d\d\d-(\d\d\d)-(\d\d\d\d)") # Alternativ: r"\d{3}-\d{3}-\d{4}"

    # Variable text auf regulären Ausdruck mit Funktion search() überprüfen.
    mo = win_code_pattern_re.search(text) # Gibt ein Match-Objekt zurück (mo) oder None, wenn nichts gefunden wurde.

    # Prüfen, ob Muster gefunden wurde und ein Gewinn vorliegt.
    if mo != None:
        # TODO: Gruppen hier abfragen
        #print(mo.group()) # Das liefert alle Gruppen zurück
        if int(mo.group(1)) > 500:  # Zugriff auf die erste Gruppe (1) 
            #return True
            if "4" in mo.group(2) or "7" in mo.group(2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


with open("win_codes.txt", "r") as file:

    for line in file: # Alle Zeilen durchlaufen.
        if is_win_code(line.strip()):
            win_codes.append(line.strip())

# print(win_codes) # Den erstmal rausnehmen (bessere Übersicht)

# OPTIONAL: Zusätzlich in separater Datei abspeichern:
with open("win_codes_won.txt", "w") as file:
    for win_code in win_codes:
        file.write(win_code + "\n")


