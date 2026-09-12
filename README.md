# MakeCode MicroQiskit Tutorial

Interaktives deutschsprachiges MakeCode-Tutorial für die MicroQiskit-Erweiterung auf dem Calliope mini.

**Aktuelle Tutorial-Version: 0.0.3**

## Tutorial starten

Für die Entwicklung wird eine versionierte Tutorial-Datei verwendet, damit MakeCode nicht versehentlich eine ältere gecachte Fassung lädt:

https://makecode.calliope.cc/#tutorial:https://github.com/heini208/makecode_qiskit_tutorial/tutorial-v0-0-3

Im ersten Dialog muss **Tutorial-Version 0.0.3, Stand 12.09.2026** stehen.

Die MicroQiskit-Erweiterung wird vom Tutorial automatisch geladen. Die verwendete Extension-Version ist in der Tutorial-Datei über den MakeCode-`package`-Block festgelegt.

## Dateien

- `tutorial.md`: aktuelle Arbeitsfassung
- `tutorial-v0-0-3.md`: aktuelle versionierte Fassung für MakeCode
- `images/`: Animationen der Bloch-Kugel
- `pxt.json`: MakeCode-Projektkonfiguration
- `main.ts`: bleibt absichtlich leer

## Entwicklung

MakeCode kann GitHub-Tutorials zwischenspeichern. Bei größeren Iterationen wird deshalb eine neue versionierte Tutorial-Datei angelegt und die Versionsnummer in `pxt.json` erhöht.

Extension: https://github.com/heini208/makecode-qiskit
