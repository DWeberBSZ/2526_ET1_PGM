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
