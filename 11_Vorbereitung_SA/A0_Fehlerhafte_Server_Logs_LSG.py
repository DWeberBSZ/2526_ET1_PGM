# =============================================================================
# AUFGABE: Fehlereinträge aus einem Server-Log extrahieren
# =============================================================================
#
# Du hast ein Server-Log (server.log) mit ca. 100 Einträgen verschiedener
# Log-Level: INFO, DEBUG, WARNING und ERROR.
#
# Jede Zeile hat folgendes Format:
#   [DATUM UHRZEIT] LEVEL Nachricht
#   Beispiel: [2024-03-15 08:42:01] ERROR Verbindung zu DB fehlgeschlagen
#
# Deine Aufgabe:
#   1. Öffne die Datei server.log und lies sie zeilenweise ein.
#   2. Filtere mit re.compile() und re.search() ausschließlich die ERROR-Zeilen.
#   3. Extrahiere aus jeder ERROR-Zeile: Datum, Uhrzeit und Nachricht.
#   4. Speichere die gefundenen Einträge formatiert in einer neuen Datei
#      namens errors_only.log.
#   5. Schließe beide Dateien ordnungsgemäß.
#
# Erwartetes Ergebnis in errors_only.log (22 Einträge), z. B.:
#   [2024-03-15 06:04:55] ERROR Verbindung zu Cache-Server redis-01 fehlgeschlagen
#
# Verwende: re.compile(), .search(), .group(1), .group(2), .group(3)
#
# Hinweis zu eckigen Klammern im Muster:
#   [ und ] sind Sonderzeichen in regulären Ausdrücken – sie leiten eine
#   Zeichenklasse ein (z. B. [a-z]). Sollen sie als literale Zeichen im Text
#   gesucht werden, müssen sie escaped werden: \[ und \].
#   Ohne Escaping würde z. B. [2024 als Zeichenklasse interpretiert,
#   die genau ein Zeichen aus {2, 0, 4} matcht – nicht das gewünschte [.
# =============================================================================

import re

# Regulären Ausdruck kompilieren – matcht nur ERROR-Zeilen und
# extrahiert Datum, Uhrzeit und Nachricht als drei Gruppen
pattern = re.compile(r"\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})\] ERROR (.+)")

# oder nur mit Wortzeichen in der Nachrichtenbeschreibung (speichert nur das erste Wort):
# pattern = re.compile(r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] ERROR \w+")

# --- Schritt 1: Einlesen und Verarbeiten ---
fehlereintraege = []

with open("server.log", "r") as eingabe:
    for zeile in eingabe:
        match = pattern.search(zeile)
        if match != None:
            #datum     = match.group(1)
            #uhrzeit   = match.group(2)
            #nachricht = match.group(3)
            #fehlereintraege.append(f"[{datum} {uhrzeit}] ERROR {nachricht}")
            
            # oder ohne Gruppen, ganze Zeile hinzufügen:
            fehlereintraege.append(zeile.strip())

# --- Schritt 2: Schreiben in neue Datei ---
with open("errors_only.log", "w") as ausgabe:
    for eintrag in fehlereintraege:
        ausgabe.write(eintrag + "\n")

print(f"{len(fehlereintraege)} ERROR-Einträge wurden in 'errors_only.log' gespeichert.")