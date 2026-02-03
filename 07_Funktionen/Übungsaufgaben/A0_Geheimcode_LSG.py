"""
Aufgabe: Geheimcode
===================

Schreiben Sie eine Funktion, die einen Text aufnimmt und mit einer Caesar-Chiffre verschlüsselt. 

Dies ist eine der einfachsten und am häufigsten bekannten Verschlüsselungstechniken. 

Jeder Buchstabe im Text wird durch einen Buchstaben ersetzt, der eine feste Anzahl von Stellen weiter im Alphabet enthält.
"""

geheimcode = {
    "A": "X", "B": "Y", "C": "Z",
    "D": "A", "E": "B", "F": "C",
    "G": "D", "H": "E", "I": "F",
    "J": "G", "K": "H", "L": "I",
    "M": "J", "N": "K", "O": "L",
    "P": "M", "Q": "N", "R": "O",
    "S": "P", "T": "Q", "U": "R",
    "V": "S", "W": "T", "X": "U",
    "Y": "V", "Z": "W"
}


def caesar_chiffre(unverschluesselt):
    
    verschluesselt = list()
    
    for buchstabe in unverschluesselt:
        if buchstabe in geheimcode:
            verschluesselt.append(geheimcode[buchstabe])
        else:
            print("Die Zeichenkette enthält ungültige Zeichen!")
            return "!!!UNGÜLTIGE ZEICHENKETTE!!!"
            # Alternative: break (verlässt Schleife)
        
    return ''.join(verschluesselt) # Wandelt eine Liste von Buchstaben in eine Zeichenkette um.

# Alternative: 
def caesar_chiffre_ASCII_offset(unverschluesselt):
    verschluesselt = list()
    ASCII_OFFSET = -26 # WICHTIG: Darf nicht über Alphabet hinaus gehen, maximal -25 oder +25

    for buchstabe in unverschluesselt:

        ascii_code = ord(buchstabe) # Funktion ord() liefert den ASCII-Code eines Buchstaben zurück!

        if ascii_code >= 65 and ascii_code <= 90: # Begrenzung auf Großbuchstaben
        
            neuer_ascii_code = ascii_code + ASCII_OFFSET # vorher: Zuordnung über Dictionary, hier Zuordnung über Offset.

            # ASCII-Code auf Wertebereich 65 bis 90 beschränken (Großbuchstaben)
            if neuer_ascii_code < 65:
                neuer_ascii_code = 90 - (64 - neuer_ascii_code) # Test: ASCII Code 64 muss 90 ergeben, check!

            elif neuer_ascii_code > 90:
                neuer_ascii_code = 65 + (neuer_ascii_code - 91) # Test: ASCII Code 91 muss 65 ergeben, check!

            neuer_buchstabe = chr(neuer_ascii_code) # Funktion chr() liefert Buchstabe zum ASCII-Code
            verschluesselt.append(neuer_buchstabe)

        else:
            print("Die Zeichenkette enthält ungültige Zeichen!")
            return "!!!UNGÜLTIGE ZEICHENKETTE!!!"
        
    return ''.join(verschluesselt) # Wandelt eine Liste von Buchstaben in eine Zeichenkette um.

# 3x Testen
for _ in range(3):
    eingabe = input("Geben Sie eine zu verschlüsselnde Eingabe ein: ")

    ausgabe = caesar_chiffre(eingabe.upper())
    print("Verschlüsselter Code: ", ausgabe)

    # Alternative:
    ausgabe = caesar_chiffre_ASCII_offset(eingabe.upper())
    print("Verschlüsselter Code: ", ausgabe)


