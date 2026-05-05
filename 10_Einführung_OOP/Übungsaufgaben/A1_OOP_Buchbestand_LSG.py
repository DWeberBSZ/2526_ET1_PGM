class Buch: # webd: a) 1P

    def __init__(self): # webd: a) 3P
        self.titel = ""
        self.autor = ""
        self.isbn = ""
        self.jahr = 0
        self.pruefsumme = 0

    def anzeigen(self): # webd: b) 3P
        print(f"Titel: {self.titel}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Erscheinungsjahr: {self.jahr}")
        print(f"Prüfsumme: {self.pruefsumme}")

    def alter(self, aktuelles_jahr): # webd: b) 3P
        differenz = aktuelles_jahr - self.jahr
        return differenz     

meinBuch = Buch() # webd: b) 4P

meinBuch.titel = "Die Verwandlung"
meinBuch.autor = "Franz Kafka"
meinBuch.isbn = "123456789"
meinBuch.jahr = 1915
meinBuch.pruefsumme = 45

meinBuch.anzeigen() # webd: b) 1P
differenz = meinBuch.alter(2024) # webd: 3P
print(f"Die Differenz zwischen Erscheinungsjahr und heute beträgt: {differenz}")


