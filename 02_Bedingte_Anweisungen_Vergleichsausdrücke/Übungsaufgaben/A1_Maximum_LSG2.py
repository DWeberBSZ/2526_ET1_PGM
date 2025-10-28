'''
Aufgabe: Maximum von drei Zahlen
=================================

Arbeitsauftrag:

- Erstellen Sie ein Programm, welches nacheinander drei Ganzzahlen von der Konsole einliest
  und in drei Variablen abspeichert.
  
- Unterscheiden Sie mithilfe von bedingten Anweisungen, welche der drei Zahlen die größte ist
  und geben Sie die größte der drei Zahlen in folgender Form auf der Konsole aus:

  "Das Maximum der drei Zahlen ist xx."

Zeit: 20 Minuten, Einzelarbeit.
'''


zahl1 = int(input("Bitte gebe Zahl 1 ein: "))
zahl2 = int(input("Bitte gebe Zahl 2 ein: "))
zahl3 = int(input("Bitte gebe Zahl 3 ein: "))

maximum = 0 # für positive Zahlen

if zahl1 > zahl2:
    if zahl1 > zahl3:
        maximum = zahl1
    else:
        maximum = zahl3
else:
    if zahl2 > zahl3:
        maximum = zahl2
    else:
        maximum = zahl3
        
print(f"Das Maximum der drei Zahlen ist {maximum}.")

    

