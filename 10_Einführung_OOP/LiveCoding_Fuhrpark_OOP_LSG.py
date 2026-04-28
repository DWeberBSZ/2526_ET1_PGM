# Definition der Klasse Auto -> 1. Phase (Lehrer-SuS-Gespräch)
class Auto:

    def __init__(self):
        self.bezeichnung = ""
        self.baujahr = 2000
        self.verkauft = False
        self.attribut_sus1 = "Attribut der SuS 1"
        self.attribut_sus2 = "Attribut der SuS 2"
    
    def daten_anzeigen(self):
        print(f"Die Bezeichnung des Autos ist: {self.bezeichnung}")
        print(f"Das Baujahr des Autos ist: {self.baujahr}")
        print(f"Das Auto wurde bereits verkauft? {self.verkauft}")
        print(f"SuS-Attribut1 {self.attribut_sus1}")
        print(f"SuS-Attribut2 {self.attribut_sus2}")
        
        
    def verkaufen(self):
        self.verkauft = True
        
        
    def methode_sus_nennung(self):
        print("Konsolenausgaben der SuS-Methode")
        

erstesAuto = Auto()

erstesAuto.bezeichnung = "VW Golf"
erstesAuto.baujahr = 2018
erstesAuto.verkauft = False

erstesAuto.daten_anzeigen()
erstesAuto.methode_sus_nennung()



zweitesAuto = Auto()
zweitesAuto.bezeichnung = "Opel Corsa"
zweitesAuto.baujahr = 2019
zweitesAuto.verkauft = True

zweitesAuto.daten_anzeigen()
zweitesAuto.methode_sus_nennung()



drittesAuto = Auto()
drittesAuto.bezeichnung = "Tesla Model 3"
drittesAuto.baujahr = 2017
drittesAuto.verkauft = False

drittesAuto.daten_anzeigen()
drittesAuto.verkaufen()
drittesAuto.daten_anzeigen()
drittesAuto.methode_sus_nennung()










