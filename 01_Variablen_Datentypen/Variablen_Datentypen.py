"""
30.09.25
╔══════════════════════════════════╗
║    VARIABLEN UND DATENTYPEN      ║
╚══════════════════════════════════╝
"""

# s. Buch, Kapitel 
# - 2.1, 2.2 (Variablen)
# - 3.1 (Operatoren)
# Das ist einzeiliger Kommentar!
"""
Das ist
mehrzeiliger
Kommentar
"""

'''
Das ist auch ein 
mehrzeiliger 
Kommentar
'''

# DEFINITION von VARIABLEN
a = 5 # Jede Variable benötigt einen STARTWERT
# a ist eine Variable, Variablennamen sind frei wählbar
# eine Variable ist ein Platzhalter für Informationen
# Variablen sollten AUSSAGEKRÄFTIGE Namen haben
x = 8 # = ist der Zuweisungsoperator

# beim Zuweisen an Variable wird von 
# "rechts" nach "links" gelesen
# Der Wert 8 wird in die Variable x kopiert

print(a + x)
a = a + 5 # Vorschläge: Fehler, 10, immer wieder + 5
print(a)
a = a + 5 # Vorschläge: Fehler, 10, immer wieder + 5
print(a)
a = a + 5 # Vorschläge: Fehler, 10, immer wieder + 5
print(a)
# Kurzschreibweise:
a += 5 # entspricht a = a + 5
print(a)

c = 5 / 3 # 1.666666666666666666
c = c % 2 # Rest: 1.6666666
c += 10   # 11.66666
print(c) # Was wird auf der Konsole ausgeben?

d = 5

d = d - x
d -= x # Kurzschreiweise von Zeile oben

d = d / x
d /= x # Kurzschreiweise von Zeile oben

d = d * x
d *= x # Kurzschreiweise von Zeile oben

# Ein paar Infos zu DATENTYPEN 
# Datentyp ist die "Art" der Information einer Variable
ganze_zahl = 3 # Datentyp: Ganzzahl, engl. Integer
hoehe = 5.5 # Datentyp: Kommazahl, Float, KOMMA ist der PUNKT!!!
temperatur = -3.8 # Datentyp: Float, aber ebene negativ
name = "Weber" # Vorschlag: Text, Fachbegriff: ZEICHENKETTE, engl. String
stimmt_das = False # Datentyp: Wahrheitswert, engl. Bool, 
das_ist_richtig = True








