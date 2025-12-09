import random                
# Teilaufgabe 1: 
# Definieren Sie eine Liste lotto für die Lottozahlen mit sechs Standardwerten (0)
lotto = [] # Notwendig für ZUSATZAUFGABE
#lotto = [0, 0, 0, 0, 0, 0] # Notwendig für eigentliche Aufgabe


# Teilaufgabe 2: Verwenden Sie eine for-Schleife für das Ziehen der Zufallszahlen 
# und das Beschreiben der Liste.

# ZUSATZAUFGABE: Jede Zahl darf nur einmal vorhanden sein.
while len(lotto) < 6:
    zufallszahl = random.randint(1, 6)
    if zufallszahl not in lotto:
        lotto.append(zufallszahl)

# Eigentliche Aufgabe:
#for x in range(len(lotto)):
#    lotto[x] = random.randint(1, 6)


# Zusatzaufgabe:
# Implementieren Sie die Konsolenausgabe ebenfalls innerhalb einer for-Schleife.
print("Folgende Kombination wurde gezogen: ")
print(lotto)