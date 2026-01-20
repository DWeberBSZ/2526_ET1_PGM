'''
Übungsgaufgabe: Durchschnittspunktzahl mit Dictionary berechnen.
================================================================

*** INFORMIEREN: ***
1. Durchlaufen von Dictionaries: Weber erklärt's!
 
2. Für die Bearbeitung der Aufgabe informieren Sie sich zunächst, 
wie Einträge zu einem Dictionary hinzugefügt werden können:
https://www.python-kurs.eu/python3_dictionaries.php (nur Kapitel "Einführung")

Gegeben ist ein Dictionary mit Schülern und den jeweiligen 
Punktzahlen ihrer Prüfungen.

Schreiben Sie ein Programm, das die Durchschnittspunktzahl 
für jeden Schüler berechnet und in einem neuen Dictionary abspeichert.

Geben Sie anschließend für jeden Schüler den Namen und die zugehörige 
Durchschnittspunktzahl auf der Konsole aus.

HINWEIS: Greifen Sie für die Berechnung des Durchschnitts auf die
Funktionen sum() und len() zurück.
'''

# Das Dictionary mit Schülern und ihren Noten
noten = {
    'Max': [85, 90, 92],
    'Anna': [78, 85, 80],
    'Tom': [90, 88, 94],
    'Lisa': [82, 75, 88]
}

# Berechnung des Durchschnitts für jeden Schüler
durchschnittsnoten = {}

for schueler, notenliste in noten.items():
    durchschnitt = sum(notenliste) / len(notenliste)
    durchschnittsnoten[schueler] = durchschnitt

print("Durchschnittsnoten der Schüler:")
for schueler, durchschnitt in durchschnittsnoten.items():
    print(f"{schueler}: {durchschnitt}")
