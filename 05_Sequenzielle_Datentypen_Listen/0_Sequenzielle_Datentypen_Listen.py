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
#txt = "Hello World" # Das ist ein sequenzeller Datentyp!!!

# Mithilfe einer FOR-SCHLEIFE kann man durch SEQUENZEN durchlaufen.
#for buchstabe in txt:
#    print(buchstabe)

# Auch die range-Funktion liefert eine SEQUENZ:
# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
# Weitere Beispiele mit Strings:
#txt = "Hello \nWorld"           # Escapezeichen, Sonderzeichen, \n ist Zeilenumbruch
#txt = "Hello World \\ World"    # Mit \ werden Sonderzeichen eingeleitet
#txt = R"Hello \nWorld"          # raw-String -> keine Interpretation von Sonderzeichen!!!

#print(txt.lower())              # String wird hierbei nicht verändert, müsste in einer separaten Variable abgelegt werden!
#print(txt.upper())
#print(txt)          

""" 
╔═════════════════════════════════════╗
║        EINFÜHRUNG IN LISTEN         ║
╚═════════════════════════════════════╝
""" 

# Man kann Informationen auch zusammenhängend (nacheinander) abspeichern.
# Eine LISTE sind mehrere Variablen "hintereinander".
# Definition einer Liste durch die Verwendung von ECKIGEN KLAMMERN.

meine_liste = [] # Definition einer leeren Liste
meine_liste = list()

eine_nicht_leere_liste = [1, 2, 3, 4, 5, 6, 7]

eine_gemischte_liste = [1, True, "Hallo"] # GEMISCHTE
das_ist_eine_verschachtelte_liste = [1, True, [1, 2, 3, 4]] # VERSCHACHTELTE

print(f"Länge meiner gemischten Liste: {len(eine_gemischte_liste)}")
print(f"Länge meiner verschachtelten Liste: {len(das_ist_eine_verschachtelte_liste)}")

eine_nicht_leere_liste.append(8) # Damit kann man EINZELNE Elemente zur Liste hinzufügen
eine_nicht_leere_liste.append(9)
eine_nicht_leere_liste.append(10)

for x in range(11, 15):
    eine_nicht_leere_liste.append(x)
    
    
liste_1 = [1, 2, 3, 4]
liste_2 = ["Hallo", "mein Name", "ist", "Weber"]

zusammengefügte_liste = liste_1 + liste_2

liste_1.extend(liste_2) # So kann eine Liste um mehrere Elemente erweitert werden
zusammengefügte_liste = liste_1

print(zusammengefügte_liste)

# Es gibt auch "Listen", die man nachträglich nicht mehr verändern kann:
# TUPEL

das_ist_ein_tupel = (1, 2, 3) # Append oder extend funktioniert hier nicht


