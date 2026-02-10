"""
Aufgabe: Fakultät
=================
In einer Lagerhalle sollen verschiedene Sorten von Schrauben in eine Reihe von beschrifteten Boxen einsortiert werden.
Da jede Schraubensorte nur einmal vorkommt, spielt die Reihenfolge der Einsortierung eine Rolle.

Die Lagerleitung möchte wissen, wie viele unterschiedliche Anordnungen der Schrauben in den Boxen möglich sind.
Solche Fragestellungen treten in der Logistik, Informatik und Produktionsplanung häufig auf.

Um die Anzahl möglicher Anordnungen zu berechnen, verwendet man die sogenannte Fakultät (!) einer Zahl.
Sie beschreibt, wie viele verschiedene Reihenfolgen für eine bestimmte Anzahl von Objekten existieren.

Formel:
=======
Für n≥1 gilt:
n!=1⋅2⋅3⋅…⋅n

Sonderfall:
0! = 1

Beispiel:
Für 5 verschiedene Schraubensorten gibt es 120 mögliche Anordnungen in den Boxen.

Aufgabenstellung:
=================

Schreiben Sie ein Python-Programm, das berechnet, wie viele unterschiedliche Anordnungen für eine gegebene Anzahl von Schraubensorten möglich sind.

Implementieren Sie eine Funktion fakultaet(n), die:

* eine ganze Zahl n ≥ 0 erhält,
* die Anzahl der möglichen Anordnungen berechnet,
* das Ergebnis zurückgibt.

Verwenden Sie hierfür eine Schleife (for oder while).

Testen Sie Ihr Programm mit verschiedenen Werten, z. B.:

0 Schraubensorten (Ergebnis 1)
5 Schraubensorten (Ergebnis 120)
10 Schraubensorten (Ergebnis 3 628 800)

Zeit: 15 Minuten

"""
