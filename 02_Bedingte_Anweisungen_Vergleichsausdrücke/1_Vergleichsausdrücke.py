""" 
21.10.25
╔══════════════════════════════════╗
║       VERGLEICHSAUSDRÜCKE        ║
╚══════════════════════════════════╝
""" 
# VERGLEICHSAUSDRÜCKE werden häufig in Verbindung mit bedingten Anweisungen verwendet.
alter_anton = 25
alter_jonas = 24
alter_herr_weber = 33

if alter_anton == alter_jonas: # == Vergleichsoperator
    print("Anton ist genauso alt wie Jonas")
elif alter_anton > alter_jonas:
    print("Anton ist älter als Jonas")
elif alter_anton < alter_jonas:
    print("Anton ist jünger als Jonas")
else:
    print("Das kann nicht vorkommen!")
    
# besser:
if alter_anton == alter_jonas: # == Vergleichsoperator
    print("Anton ist genauso alt wie Jonas")
elif alter_anton > alter_jonas:
    print("Anton ist älter als Jonas")
else:
    print("Anton ist jünger als Jonas")
    
if alter_herr_weber == alter_jonas: # == Vergleichsoperator
    print("Herr Weber ist genauso alt wie Jonas")
elif alter_herr_weber > alter_jonas:
    print("Herr Weber ist älter als Jonas")
else:
    print("Herr Weber ist jünger als Jonas")
    
# Vergleichsoperatoren
# > größer
# >= größer oder gleich
# < kleiner
# <= kleiner oder gleich
# == ist gleich
# != ist ungleich

