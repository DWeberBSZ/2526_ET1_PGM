# Definition der Klasse Auto
class Auto:

    # Definition der Attribute.
    def __init__(self):
        self.bezeichnung = ""
        self.baujahr = 2000
        self.verkauft = False
        # TODO (Optional): Ergänzen Sie hier Ihre vorgeschlagenen Attribute aus dem Klassendiagramm.
        

    # Definition der Methoden.
    def daten_anzeigen(self):
        print(f"Die Bezeichnung des Autos ist: {self.bezeichnung}")
        print(f"Das Baujahr des Autos ist: {self.baujahr}")
        print(f"Das Auto wurde bereits verkauft? {self.verkauft}")

          
    def verkaufen(self):
        self.verkauft = True
        
    # TODO: Ergänzen Sie hier Ihre vorgeschlagenen Methoden.

    
    
    
    

# TODO: 
# Erstellen Sie drei Auto-Objekte (eines ist bereits erstellt) und 
# weisen Sie den Attributen der Objekte sinnvolle Werte zu und rufen Sie die Methoden auf.

"""
Erstes Auto erstellen (Beispiel):
    VW Golf mit Baujahr 2018, nicht verkauft.
    Die Fahrzeugdaten sollen angezeigt werden (Methode: daten_anzeigen).
"""
erstesAuto = Auto()

erstesAuto.bezeichnung = "VW Golf"
erstesAuto.baujahr = 2018
erstesAuto.verkauft = False

erstesAuto.daten_anzeigen()

"""
Hier zweites Auto erstellen:
    Opel Corsa mit Baujahr 2019, bereits verkauft.
    Die Fahrzeugdaten sollen angezeigt werden (Methode: daten_anzeigen).
"""






"""
Hier drittes Auto erstellen:
    Tesla Model 3 mit Baujahr 2017, nicht verkauft.
    Die Fahrzeugdaten sollen angezeigt werden (Methode: daten_anzeigen).
    Das Auto wird verkauft (Methode: verlaufen).
    Die Fahrzeugdaten sollen nach dem Verkauf nochmal angezeigt werden.
"""









