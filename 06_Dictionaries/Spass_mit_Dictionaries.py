# Definition eines Dictionaries
artikel_preis_eur = {}
artikel_preis_eur = dict() # Bei Listen war das list()

# Zum Vergleich: Bei Listen war das so:
einkaufswagen = [ ]
einkaufswagen = list()


artikel_preis_eur["Apfel"] = 0.30 # Werte zu einem Dict hinzufügen
artikel_preis_eur["Birne"] = 0.45
artikel_preis_eur["Schokoloade"] = 2.50

#print(artikel_preis_eur["Ramensuppe"]) # das geht NICHT!

#einkaufswagen[0] = "Schokolade" # das funktioniert NICHT bei Listen

for artikel in artikel_preis_eur:
    print(artikel)
    
for artikel, preis in artikel_preis_eur.items():
    print(artikel, preis)
    
for preis in artikel_preis_eur.values():
    print(preis)
    
print(artikel_preis_eur)