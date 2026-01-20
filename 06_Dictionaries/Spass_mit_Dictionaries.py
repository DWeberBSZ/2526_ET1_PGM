# Definition eines Dictionaries
artikel_preis_eur = {}
artikel_preis_eur = dict() # Bei Listen war das list()

# Zum Vergleich: Bei Listen war das so:
einkaufswagen = [ ]
einkaufswagen = list()

# Bei Dictionaries könnt ihr Einträge sehr einfach hinzufügen:
artikel_preis_eur["Apfel"] = 0.50 # Preis 
artikel_preis_eur["Banane"] = 0.30
artikel_preis_eur["Orange"] = 0.80
print(artikel_preis_eur)

# Bei Listen geht das NICHT:
#einkaufswagen[0] = "Apfel" # Geht nicht, da der Index 0 noch nicht existiert
#einkaufswagen.append("Apfel") # So geht es

for key in artikel_preis_eur: # Standardmäßig wird über die Schlüssel iteriert
    print(f"Der Preis von {key} ist {artikel_preis_eur[key]} EUR.")

# Wenn ich stattdessen über die Werte iterieren möchte:
for preis in artikel_preis_eur.values():
    print(f"Ein Artikel kostet {preis} EUR.")

# Wenn ich sowohl Schlüssel als auch Werte haben möchte:
for artikel, preis in artikel_preis_eur.items():
    print(f"Der Preis von {artikel} ist {preis} EUR.")

# Was sonst noch wichtig ist:
# - Dictionaries sind ungeordnet (bis Python 3.6). Ab Python 3.7 behalten sie die Einfügereihenfolge bei.
# - Schlüssel in Dictionaries müssen unveränderlich (hashable) sein, z.B. Strings, Zahlen oder Tupel.
# - Werte können beliebige Datentypen sein, einschließlich Listen oder sogar andere Dictionaries.
# - Dictionaries sind sehr effizient für das Nachschlagen von Werten basierend auf Schlüsseln.


