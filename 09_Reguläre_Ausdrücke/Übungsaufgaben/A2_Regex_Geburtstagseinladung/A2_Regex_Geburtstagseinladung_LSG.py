"""
HINWEIS: 
Eine Person gilt als volljährig, wenn sie vor dem Jahr 2008 geboren ist.
"""
import re

# Teilaufgabe a)
entries = list() # 1P
adults = list() # 1P

# Teilaufgabe b)
with open("Anmeldung.txt", "r") as file: # 2P
    for line in file: # Schleife: 1P
        entries.append(line.strip()) # Hinzufügen der richtigen Einträge: 1P

# Teilaufgabe c)
pattern = re.compile(r"(\w* \w*), (\d\d)/(\d\d)/(\d\d\d\d)") # 6P

for entry in entries: # 2P
    mo = pattern.search(entry) # 1P

    if mo != None: # 1P
        # Überprüfen, ob Person bereits 18 ist.
        if int(mo.group(4)) < 2008: # 2P
            adults.append(mo.group(1)) # 2P
                    
# Teilaufgabe d)
with open("Erlaubt.txt", "w") as file: # 1P
    for adult in adults: # 2P
        file.write(adult + "\n") 