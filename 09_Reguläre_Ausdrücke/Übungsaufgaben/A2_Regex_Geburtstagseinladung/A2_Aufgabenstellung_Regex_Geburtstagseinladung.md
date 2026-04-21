# Übungsaufgabe: Geburtstagseinladung

Sie erhalten eine Textdatei Anmeldung.txt mit dem vollständigen Namen und dem Geburtstag von Personen, die zu einer Geburtstagsfeier eingeladen werden sollen. Allerdings scheinen einige der Personen noch nicht volljährig (18 Jahre) zu sein. 

Ziel der Aufgabe ist es, die Namen der Personen herauszufinden, die bereits volljährig sind und diese in einer separaten Textdatei abzuspeichern. 

**HINWEIS:** Eine Person gilt im Rahmen dieser Aufgabe als volljährig, wenn sie vor dem Jahr 2008 geboren ist. 

Bearbeiten Sie hierfür die nachfolgenden Teilaufgaben in einem Python-Skript.

1. Definieren Sie im Programm zwei separate, zunächst leere Listen: 
	- Liste `anmeldungen`: Alle unveränderten Einträge (Zeilen) der Textdatei
	- Liste `erwachsene`: Die vollständigen Namen der zugelassenen Gäste
 
2. Öffnen Sie die Textdatei Anmeldung.txt in Python und lesen Sie alle Zeilen aus der Datei aus. Speichern Sie die Einträge zeilenweise in der Liste `anmeldungen`. 

3. Finden Sie mithilfe von regulären Ausdrücken und geeigneten if-Anweisungen heraus, wer für den Geburtstag zugelassen ist, also bereits volljährig ist. Speichern Sie die vollständigen Namen der zugelassenen Gäste in der Liste `erwachsene` ab.

4. Speichern Sie die Inhalte der Liste `erwachsene` zeilenweise in einer separaten Datei Erlaubte_Anmeldungen.txt ab.

**HINWEIS:** Gehen Sie davon aus, dass alle Einträge in der Datei Anmeldung.txt immer in der nachfolgenden Form vorliegen. Der Geburtstag liegt im amerikanischen Format vor:

Vorname\[LEERTASTE]Nachname,\[LEERTASTE]MM/TT/JJJJ

z.B.
Emily Johnson, 07/15/2006  
Michael Brown, 02/23/2007
…

**HINWEIS:** Eine Person gilt im Rahmen dieser Aufgabe als volljährig, wenn sie vor dem Jahr 2008 geboren ist. 
