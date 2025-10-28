paketnummer = 0
fach = 0

paketnummer = int(input("Bitte gebe die Paketnummer ein: "))

if paketnummer % 400 == 0:
    fach = 3
elif paketnummer % 100 == 0:
    fach = 2
elif paketnummer % 4 == 0 or paketnummer % 5 == 0:
    fach = 1
else:
    fach = 4

print(f"Fach: {fach}")
