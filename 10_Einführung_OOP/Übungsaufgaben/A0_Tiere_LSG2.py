# 1. Klasse definieren
class Tier:
    # Attribute:
    def __init__(self, name, gattung, gewicht, groesse, schlaeft):
        # name, gatting, gewicht, groesse
        self.name = name 
        # self.name gehört zum Objekt
        # name ist ein Übergabeparameter zum Beschreiben des Objekts
        self.gattung = gattung
        self.gewicht = gewicht
        self.groesse = groesse
        self.schlaeft = schlaeft

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
erstesTier = Tier("Timmy", "Buckelwal", 30000.0, 12.35, False)
# WICHTIG!!!! Beim Anlegen des Objekts kein self verwenden!!!!!!

erstesTier.Beschreibung()
erstesTier.Fuettern()
erstesTier.Schlafen()