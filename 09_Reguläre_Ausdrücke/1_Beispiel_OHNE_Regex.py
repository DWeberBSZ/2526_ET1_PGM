
# 3. Schritt: Funktion definieren, die zurück gibt, ob ein Text ein Gewinncode ist.
def is_win_code(text):
    # return True, falls Zeile ein Gewinncode ist
    # return False, falls Zeile keinem Gewinncode entspricht

    # Idee: 
    # Wir überprüfen, was dazu führt, dass ein Text NICHT einem Gewinncode entspricht (return False).
    # Trifft nichts davon zu, ist der Text ein Gewinncode (return True).
    
    # Prüfen, ob der Text ungleich 12 lang ist.
    if len(text) != 12:
        return False

    # Prüfen, ob die ersten drei Zeichen keine Ziffer sind. 
    for i in range(0, 3):
        if not text[i].isdecimal() # text, z.B. 434-5678-978
            return False
        
    # Prüfen, ob das vierte Zeichen kein Minus ist.
    if text[3] != "-":
        return False
    
    # Prüfen, ob die nächsten Zeichen keine 3 Ziffern sind.
    for i in range(4, 7):
        if not text[i].isdecimal() # text, z.B. 434-5678-978
            return False

    # Prüfen, ob das achte Zeichen kein Minus ist.
    if text[7] != "-":
        return False
    
     # Prüfen, ob die nächsten Zeichen keine 4 Ziffern sind.
    for i in range(8, 12):
        if not text[i].isdecimal() # text, z.B. 434-5678-978
            return False    
 
    # An dieser Stelle: Hat alles gepasst -> return True
    return True

# 2. Schritt: Datei öffnen und Zeilen einlesen.
# 1. Schritt: Liste definieren, welche alle Zeilen mit Gewinncodes enthält.
win_codes = list()


with open("win_codes.txt", "r") as f:
    
    zeilen = f.readlines() # Liefert uns eine Liste aller Zeilen
    
    for zeile in zeilen:
         if is_win_code(zeile):
             win_codes.append(zeile)
        
    

# 4. Schritt: Gefundene Gewinncodes in separater Datei abspeichern.
# OPTIONAL: Zusätzlich in separater Datei abspeichern:
with open("win_codes_cleaned.txt", "w") as file:
    pass