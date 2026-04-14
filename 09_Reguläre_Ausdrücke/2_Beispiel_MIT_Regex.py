import re # 1. Schritt Python-Modul importieren für Reguläre Ausdrücke

win_codes = list()

# Reguläre Ausdrücke, kurz Regex genannt, sind Beschreibungen für ein Textmuster. 
# Ein \d in einem Regex steht zum Beispiel für ein Ziffernzeichen, d. h. eine beliebige einzelne Ziffer von 0 bis 9. 
# Der Regex \d\d\d-\d\d\d-\d\d\d wird von Python verwendet, um dasselbe Textmuster zu finden, 
# das auch die vorherige Funktion is_win_code() gefunden hat: 
# eine Zeichenfolge aus drei Zahlen, einem Bindestrich, drei weiteren Zahlen, einem weiteren Bindestrich und vier Zahlen. 
# Jede andere Zeichenfolge würde nicht mit dem Regex \d\d\d-\d\d\d-\d\d\d übereinstimmen.

def is_win_code(text):
    # 2. Schritt: Wir legen ein Regex-Objekt an und teilen dem Programm unser Muster mit:


    # 3. Schritt: Wir überprüfen unseren Text nach diesem Muster.
 

with open("win_codes.txt", "r") as file:

    for line in file.readlines(): # Alle Zeilen durchlaufen.
        if is_win_code(line.strip()):
            win_codes.append(line.strip())

print(win_codes)

# OPTIONAL: Zusätzlich in separater Datei abspeichern:
with open("win_codes_cleaned.txt", "w") as file:
    for win_code in win_codes:
        file.write(win_code + "\n")


