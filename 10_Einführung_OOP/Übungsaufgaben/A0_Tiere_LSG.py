# 1. Klasse definieren
class Tier:
    # Attribute:
    def __init__(self):
        # name, gatting, gewicht, groesse
        self.name = ""
        self.gattung = ""
        self.gewicht = 0
        self.groesse = 0.0
        self.schlaeft = False

    # Methoden:
    def Beschreibung(self):
        print(f"Name: {self.name}")
        print(f"Gattung: {self.gattung}")
        print(f"Gewicht: {self.gewicht}")
        print(f"Groesse: {self.groesse}") 

    def Fuettern(self):
        print(f"Das Tier wiegt vor dem Füttern: {self.gewicht} kg")
        self.gewicht = self.gewicht + 0.5
        print(f"Das Tier wiegt nach dem Füttern: {self.gewicht} kg")

    def Schlafen(self):
        print("Das Tier schläft")
        self.schlaeft = True
        
    def Aufwachen(self):
        print("Das Tier schläft nicht")
        self.schlaeft = False

# 2. Objekt von Klasse anlegen und Methoden aufrufen

erstesTier = Tier()
erstesTier.name = "Tiger"
erstesTier.gattung = "Grosskatze"
erstesTier.gewicht = 230.0
erstesTier.groesse = 1.0

erstesTier.Beschreibung()
erstesTier.Fuettern()
erstesTier.Fuettern()
erstesTier.Schlafen()




