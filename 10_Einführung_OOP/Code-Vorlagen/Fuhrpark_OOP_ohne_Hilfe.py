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
# Erstellen Sie drei Auto-Objekte und weisen Sie den Attributen 
# sinnvolle Werte zu und rufen Sie die Methoden auf.








