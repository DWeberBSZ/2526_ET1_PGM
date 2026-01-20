# Wir möchten eine Liste kopieren
a = [1, 2, 3]
b = a
print(a)
print(b)

b[0] = 4 
# 1. Erkenntnis: Hier wird nicht kopiert, 
# sondern nur eine Referenz hinterlegt
print(f"a={a}")
print(f"b={a}")

# 2. Erkenntis: Mit id() könnt ihr überprüfen, 
# ob Variablen im Speicher identisch sind.
print(id(a))
print(id(b))

# FLACHES KOPIEREN: Kopiert Liste, aber verschachtelte Listen bleiben das Original
c = [1, 2, 3]
d = c.copy() # eine komplett neue Kopie
d[0] = 78
print(c)
print(d)
print(id(c))
print(id(d))

# TIEFES KOPIEREN: Kopiert AUCH Listen in Listen in Listen....
import copy
e = [1, 2, [3, 4]]
f = copy.deepcopy(e)

e[2][0] = 1234567890

print(e)
print(f)
print(id(e))
print(id(f))


