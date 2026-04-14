""" 
24.02.26
╔═════════════════════════════════════╗
║      VERTIEFUNG ZU FUNKTIONEN       ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 9

# >>> Variablen in Funktionen

# Beispiel 1:

def print_var_x():
    print(x) # LESENDER Zugriff auf GLOBALE Variable x ist möglich. 
    # Optional:
    # return

x = 3 # GLOBALE Variablen, wurde außerhalb einer Funktion definiert
print_var_x()
x = 5
print_var_x()

# Beispiel 2:
def print_var_y():
    y = 5 # LOKALE Variable in der Funktion
    print(y)

print_var_y()
#print(y) # Das 

# Beispiel 3:
def print_var_z():
    z = 5 # LOKALE Variable angelegt
    print(z) # Zugriff auf die lokale Variable z

z = 3
print_var_z() # 5
print(z) # 3

# Beispiel 4:
def print_var_z2():
    global z
    z = z + 3 # In einer Funktion kann NICHT SCHREIBEND auf GLOBALE Variablen zugegriffen werden
    print(z)

z = 3
print_var_z2()


