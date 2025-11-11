"""
Aufgabe: Durchschnitt ganzer Zahlen
====================================

- Erstellen Sie ein Python-Skript, das mithilfe einer for-Schleife den Durchschnitt aller 
ganzen Zahlen von 1 bis 30 (inklusiv) bestimmt.

- Verwenden Sie hierfür die range-Funktion mit geeigneten Grenzen.


Zeit: 10 Minuten, Einzelarbeit
"""
summe = 0
anzahl = 0

# 1. Schritt: Summe berechnen
for i in range(1, 31):
    summe += i
    anzahl += 1

# 2. Schritt: Durchschnitt berechnen
durchschnitt = summe / anzahl

print(f"Der Durchschnitt ist: {durchschnitt}")