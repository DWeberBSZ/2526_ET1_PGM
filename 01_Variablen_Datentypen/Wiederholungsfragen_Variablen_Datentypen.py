# WIEDERHOLUNGSFRAGEN:
# ====================
# W1: Der folgende Code löst einen Fehler aus. Warum?
x = 1
y = 2
print(x+y+z)
# Antwort: Weil die Variable z nicht definiert ist.

# W2: Welchen Datentyp hat die Variable i nach der Zuweisung i = 3?
# Antwort: Integer, Ganzzahl

# W3: Welche Werte gibt das folgende Programm aus?
a = "abcde" # a: abcde
b = a # b: abcde, a: abcde
a = a + "fg" # a: abcdefg, b: abcde
print(b)

# Antwort: 'abcde'

# W4: Der folgende Code ist fehlerhaft. Was könnte der Grund sein?
n = 22.7
msg = "Die Temperatur beträgt " + n + " Grad."

# Antwort: n ist ein float, Umwandlung in str()
# Richtig: msg = "Die Temperatur beträgt " + str(n) + " Grad."
# Float: Kommazahl, 

# W5: Welche der Folgenden sind Operatoren, welche sind Werte?
# * # kein Wert, Operator
# 'hello' # Wert
# -88.8 # Wert
# - # Operator
# / # Operator
# + # Operator
# 5 # Wert

# W6: Welche der Folgenden ist eine Variable, welcher ist ein String?
spam    # Variable, Name frei wählbar
'spam'  # Zeichenkette, Wert


# W7: Nennen Sie drei Datentypen.
# str(), float(), bool(), int()

# W8: Welchen Wert enthält die Variable bacon nach diesen Anweisungen?
bacon = 20
bacon + 1

# Antwort: 20
# für 21 müsste da stehen: bacon = bacon + 1, Kurzschreibweise: bacon += 1


# W9: Was ergeben die folgenden Anweisungen?
'spam' + 'spamspam'
'spam' * 3

# Antwort: 
# 'spamspamspam'
# 'spamspamspam'

# W10: Welche drei Funktionen können verwendet werden, 
# um die Ganzzahl-, Gleitkommazahl- oder Zeichenfolgenversion eines Werts zu erhalten?
# int(), float(), str()