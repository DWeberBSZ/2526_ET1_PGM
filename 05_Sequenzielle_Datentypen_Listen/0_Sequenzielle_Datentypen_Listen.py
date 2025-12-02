""" 
18.11.25
╔═════════════════════════════════════╗
║  SEQUENZIELLE DATENTYPEN (LISTEN)   ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 7.1


""" 
╔═════════════════════════════════════╗
║        ERGÄNZUNG ZU STRINGS         ║
╚═════════════════════════════════════╝
""" 
# Einen sequenziellen Datentypen (Sequenz) kennen wir schon:
txt = "Hello World" # Das ist ein sequenzeller Datentyp!!!

# Mithilfe einer FOR-SCHLEIFE kann man durch SEQUENZEN durchlaufen.
for buchstabe in txt:
    print(buchstabe)

# Auch die range-Funktion liefert eine SEQUENZ:
# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
# Weitere Beispiele mit Strings:
txt = "Hello \nWorld"           # Escapezeichen, Sonderzeichen, \n ist Zeilenumbruch
txt = "Hello World \\ World"    # Mit \ werden Sonderzeichen eingeleitet
txt = R"Hello \nWorld"          # raw-String -> keine Interpretation von Sonderzeichen!!!

print(txt.lower())              # String wird hierbei nicht verändert, müsste in einer separaten Variable abgelegt werden!
print(txt.upper())
print(txt)          

""" 
╔═════════════════════════════════════╗
║        EINFÜHRUNG IN LISTEN         ║
╚═════════════════════════════════════╝
""" 

# Man kann Informationen auch zusammenhängend (nacheinander) abspeichern.
# Eine LISTE sind mehrere Variablen "hintereinander".
# Definition einer Liste durch die Verwendung von ECKIGEN KLAMMERN.

x = [3, 99, "Ein Text"]     # In einer Liste können beliebige Datentypen stehen!

# FRAGE: Wie viele Elemente hat diese Liste?
y = [42, 65, [45, 89], 88]  # ANTWORT: Die Liste hat vier Elemente. Das dritte Elemente ist eine weitere Liste.

# LISTEN ANPASSEN.
# Mit append() können Elemente an eine Liste NACH der Definition angehängt werden.

print(x)
x.append(12)    # WICHTIG: Die Liste wird hierbei verändert! (Bei den obigen Stringfunktionen war das nicht der Fall!)
print(x)

# Tupel: wie Listen, allerdings UNVERÄNDERBAR!!! Runde klammern, statt eckige Klammern!
tupel = (3, 99, "Ein Text") # Nach Definition nicht mehr veränderbar!
tupel = 3, 99, "Ein Text"   # Geht auch ohne Klammern, ist das gleiche wie oben!!!

# Deswegen Vorischt bei Fließkommadefinitionen: a = 3,5 <- das ist ein Tupel, keine Kommazahl mehr!
