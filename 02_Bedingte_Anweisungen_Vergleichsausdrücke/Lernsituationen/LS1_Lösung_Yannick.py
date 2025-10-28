
arbeitszeit = int(input("Wie viele Jahre arbeiten sie schon in der Firma?"))

if arbeitszeit==1:
    print("Ihr gehalt Beträgt 4000$")
else: 
     if arbeitszeit==2:
        print("Ihr gehalt Beträgt 4300$")
     else:
         zusatz=(float(arbeitszeit)-2)*100
         gesamtgehalt=zusatz+4300
         print("Ihr gehalt Beträgt " + str(gesamtgehalt) + "$" )
         