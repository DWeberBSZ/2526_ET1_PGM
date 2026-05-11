# =============================================================================
# AUFGABE: Objektorientierte Programmierung – Klasse Student
# =============================================================================
#
# Erstelle eine Klasse Student mit folgenden Eigenschaften:
#
# Konstruktor (__init__):
#   - name     (str)  : Name des Studenten
#   - fach     (str)  : Studienfach
#   - noten    (list) : Liste von Noten (wird als leere Liste initialisiert,
#                       NICHT als Parameter übergeben)
#
# Methode note_hinzufuegen(self, note):
#   - Nimmt eine Note (float) als Parameter entgegen
#   - Fügt diese Note der Notenliste hinzu
#   - Berechnet den aktuellen Notendurchschnitt und gibt ihn zurück
#   - Gibt None zurück, falls noch keine Noten vorhanden sind
#
# Hinweise:
#   - self ist der Verweis auf das eigene Objekt und muss als erster
#     Parameter jeder Methode angegeben werden
#   - Attribute werden im Konstruktor mit self.name = name usw. gesetzt
#   - Eine leere Liste als Attribut anlegen: self.noten = []
#   - Durchschnitt berechnen: sum(self.noten) / len(self.noten)
#
# Nach der Klassendefinition:
#   1. Lege mindestens zwei Student-Objekte an
#   2. Füge jedem Studenten mehrere Noten hinzu und gebe den aktuellen 
#      Durchschnitt aus
# =============================================================================


class Student:
    def __init__(self, name, fach):
        self.name  = name
        self.fach  = fach
        self.noten = []

    def note_hinzufuegen(self, note):
        
        self.noten.append(note)
        durchschnitt = sum(self.noten) / len(self.noten)
        
        return durchschnitt


# --- Objekte anlegen ---
s1 = Student("Anna Müller", "Informatik")
s2 = Student("Ben Schmidt", "Mathematik")

# --- Noten hinzufügen ---
print(s1.note_hinzufuegen(1.3))
print(s1.note_hinzufuegen(2.0))
print(s1.note_hinzufuegen(1.7))

print(s2.note_hinzufuegen(2.3))
print(s2.note_hinzufuegen(3.0))
print(s2.note_hinzufuegen(2.7))
