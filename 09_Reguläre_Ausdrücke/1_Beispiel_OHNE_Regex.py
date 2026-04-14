# 1. Schritt: Liste definieren, welche alle Zeilen mit Gewinncodes enthält.
win_codes = list()

# 3. Schritt: Funktion definieren, die zurück gibt, ob ein Text ein Gewinncode ist.
def is_win_code(text):

    # Idee: 
    # Wir überprüfen, was dazu führt, dass ein Text NICHT einem Gewinncode entspricht (return False).
    # Trifft nichts davon zu, ist der Text ein Gewinncode (return True).
    
    # Prüfen, ob der Text ungleich 12 lang ist.


    # Prüfen, ob die ersten drei Zeichen keine Ziffer sind. 

        
    # Prüfen, ob das vierte Zeichen kein Minus ist.

    
    # Prüfen, ob die nächsten Zeichen keine 3 Ziffern sind.
 

    # Prüfen, ob das vierte Zeichen kein Minus ist.
 
    
     # Prüfen, ob die nächsten Zeichen keine 4 Ziffern sind.
    
 
    # An dieser Stelle: Hat alles gepasst -> return True
    return True

# 2. Schritt: Datei öffnen und Zeilen einlesen.
with open("win_codes.txt", "r") as file:
    pass

# 4. Schritt: Gefundene Gewinncodes in separater Datei abspeichern.
# OPTIONAL: Zusätzlich in separater Datei abspeichern:
with open("win_codes_cleaned.txt", "w") as file:
    pass