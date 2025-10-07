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

# IMPLIZITE TYPUMWANDLUNG (AUTOMATISCHE TYPUMWANDLUNG)
operand_1 = 10 # Datentyp: Integer
operand_2 = 4 # Datentyp: Integer
print(operand_1 / operand_2) # Python konvertiert AUTOMATISCH nach Float
print(10 + 4.5)

# OPERATOREN sind abhängig vom Datentyp!!!
vorname = "Dominik"
nachname = "Weber"
print(vorname + " " + nachname)



