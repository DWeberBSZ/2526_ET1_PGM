""" 
09.12.25
╔═════════════════════════════════════╗
║ MANIPULATION VON SEQUENZEN (LISTEN) ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 7.1


"""
╔═════════════════════════════════════╗
║         ELEMENTE ANSPRECHEN         ║
╚═════════════════════════════════════╝
"""

meine_liste = [0, 2, 4, 6, 23, 45, 7, 23]

print(meine_liste[2])
print(meine_liste[-1]) # Zugriff auf das letzte Elemente der Liste
print(meine_liste[len(meine_liste)-1]) # Zugriff auf das letzte Elemente der Liste
print(meine_liste[-2]) # Zugriff auf das vorletzte Elemente der Liste
print(meine_liste[6]) # Ist auch das letzte Element, aber unschön!!!

# Wie finde ich den Index zu einem Element?
# Antwort:
index = meine_liste.index(23)
print(index)

# AUFGABE: Letztes und vorletztes Element tauschen
# Ausgangslage: [0, 2, 4, 6, 23, 45, 7, 23]
# Ziel: [0, 2, 4, 6, 23, 45, 23, 7] 

print(meine_liste)

# DREIECKSTAUSCH!!!
tmp = meine_liste[-1]
meine_liste[-1] = meine_liste[-2]
meine_liste[-2] = tmp

print(meine_liste)

"""
╔═════════════════════════════════════╗
║  BEREICHE ANSPRECHEN MIT SLICING    ║
╚═════════════════════════════════════╝
"""

meine_liste = [0, 2, 4, 6, 23, 45, 7, 23]
print(meine_liste[2:5]) # Bereich auswählen von Index 2 bis 5
print(meine_liste[::3]) # Hinter dem zweiten : steht die SCHRITTWEITE
# Wenn keine Grenzen angegeben sind, nimmt er alles
print(meine_liste[2:])
print(meine_liste[::-1]) # Alle Elemente mit negativer Schrittweite
print(meine_liste[0:-1:2]) 






