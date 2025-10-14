"""
07.10.25
╔═════════════════════════════════════════════╗
║     VERTIEFUNG VARIABLEN UND DATENTYPEN     ║
╚═════════════════════════════════════════════╝
"""

# DATENTYP einer Variable abfragen
gewicht = 80 # Datentyp: Integer, Ganzzahl
groesse = 1.83 # Datentyp: Float, Kommazahl
ist_das_wahr = True
name = "Weber"

typ_gewicht = type(gewicht)
typ_groesse = type(groesse)
typ_ist_das_wahr = type(ist_das_wahr)

print(typ_gewicht)
print(typ_groesse)
print(typ_ist_das_wahr)
print(type(name))

# EXPLIZITE Typumwandlung, 
# gebt ihr als Programmerer explizit an, z.B. float(), str(), int(), bool()

exp_int = int(5.6) # Beim Konvertieren nach INT wird NICHT gerundet, sondern abgeschnitten
print(exp_int) # Yannick: 6
print(type(exp_int)) # Sabine: Integer
#print(float("Gummibärenbande")) # Das funktioniert NICHT!!!
print("Hallo, " + "Ich wohne in der Malerstrasse " + str(5))

# IMPLIZITE TYPUMWANDLUNG (AUTOMATISCHE TYPUMWANDLUNG)
operand_1 = 10 # Datentyp: Integer
operand_2 = 4 # Datentyp: Integer
print(operand_1 / operand_2) # Python konvertiert AUTOMATISCH nach Float
print(10 + 4.5)

# OPERATOREN sind abhängig vom Datentyp!!!
vorname = "Dominik"
nachname = "Weber"
print(vorname + " " + nachname)

# Ergänzung:
ist_das_int = isinstance(gewicht, str)
print(ist_das_int)
print(type(ist_das_int))

# Auswertung zu Wahr oder Falsch.
ist_das_bool = bool(False)
print(ist_das_bool)
ist_das_bool = bool(0)
print(ist_das_bool)
ist_das_bool = bool(1)
print(ist_das_bool)
ist_das_bool = bool(2)
print(ist_das_bool)
ist_das_bool = bool(-5)
print(ist_das_bool)
ist_das_bool = bool("")
print(ist_das_bool)
ist_das_bool = bool(" ")
print(ist_das_bool)
ist_das_bool = bool("Hallo")
print(ist_das_bool)

# "Was nicht verboten (False) ist, ist erlaubt (True)
# Verboten (False) ist:
# - Die Zahl 0 bzw. 0.0
# - Eine leere Zechenkette ""
# - False

# Kommazahlen formatieren
f = 12.3456789
g = 1234.56789

print(f)
print(f"{f:.2f}")
print(f"{f:10.3f}") # Variable f
print(f"{g:10.3f}") # Variable g




