""" 
14.10.25
╔══════════════════════════════════╗
║       BEDINGTE ANWEISUNGEN       ║
╚══════════════════════════════════╝
""" 

# Mit bedingten Anweisungen kann der PROGRAMMABLAUF gesteuert werden.
# Das Programm arbeitet in Abhängigkeit von BEDINGUNGEN nur bestimmte Anweisungen ab.

"""
Arbeitsauftrag:
===============
Informieren Sie sich zu bedingten Anweisungen mithilfe des Fachbuchs.

- Lesen Sie Kapitel 8.1 "if-Verzweigung" im Fachbuch

Zeit: 8 Minuten
"""

# BEDINGTE ANWEISUNGEN
# =====================
""" Bedingte Anweisung, auch genannt: "if-Anweisung"

Aufbau einer if-Anweisung:

if BEDINGUNG: # : nicht vergessen
    Anweisung 1 # Anweisungen mit TAB einrücken!
    Anweisung 2 # Die Anweisungsfolge innerhalb einer if-Anweisung nennt sich ANWEISUNGSBLOCK
    ...
    
else: # Der else-Zweig ist optional
    Anweisung 1
    Anweisung 2
    ...
    

WICHTIG: Die BEDINGUNG muss sich zu True oder False auswerten lassen!
    - Entweder: Verwendung von True, False oder einer Variable vom Datentyp bool
    - Oder: Vergleichsaudrücke -> machen wir später!

"""

a = 5.4
ist_int = isinstance(a, int) # Datentyp: Bool -> True/False

if ist_int:
    # Anweisungsblock
    # ...
    print("Die Variable ist vom Typ Integer")
    
else:
    # Anweisungsblock
    print("Die Veriable ist NICHT vom Typ Integer")
    
    if isinstance(a, float):
        # ....
    














