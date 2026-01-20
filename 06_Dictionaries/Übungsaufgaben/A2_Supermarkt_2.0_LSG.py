'''
Übungsaufgabe: Supermarkt 2.0
=========================

Gegeben ist ein kleiner Supermarkt mit folgenden Produkten. 
Der Inhaber des Supermarktes möchte gerne wissen, wie hoch der Verkaufswert aller seiner Produkte zusammengerechnet beträgt. 

* AUFGABENSTELLUNG:
===================
Schreibe Sie ein Python-Prgramm, welches den gesamten Verkaufswert aller Produkte im Supermarkt berechnet und ausgibt.


* ZEIT: 
=======
20 Minuten
'''
supermarket = {"milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}

gesamtpreis = 0

for artikel, info_dict in supermarket.items():
    anzahl = info_dict["quantity"] 
    preis = info_dict["price"]
    gesamtpreis += anzahl * preis
    
print(gesamtpreis)
    
