# Quantencomputing mit MicroQiskit

## Willkommen @showdialog

In diesem Tutorial lernst du die Grundlagen des Quantencomputings direkt mit dem **Calliope mini** und **MicroQiskit**.

Du lernst zuerst, was Qubits und Quantengatter sind. Danach baust du eigene Quantenschaltkreise und erzeugst Quantenzufall.

## Was sind Quanten? @showdialog

In der Quantenphysik können bestimmte physikalische Größen nur in **diskreten Portionen** auftreten. Solche Portionen nennt man Quanten.

Quantenmechanische Systeme zeigen Eigenschaften, die wir aus dem Alltag nicht kennen. Für das Quantencomputing sind besonders **Superposition**, **Verschränkung** und **Interferenz** wichtig.

Diese Begriffe untersuchen wir Schritt für Schritt anhand eigener Quantenschaltkreise.

## Warum Quantencomputer? @showdialog

Klassische Computer arbeiten mit Bits und sind für sehr viele Aufgaben hervorragend geeignet.

Quantencomputer verwenden zusätzlich quantenmechanische Effekte. Für bestimmte Problemklassen können daraus neue Rechenverfahren entstehen, die sich von klassischen Verfahren grundlegend unterscheiden.

Ein Quantencomputer ist deshalb kein allgemein schnellerer Ersatz für einen klassischen Computer.

## Vom Bit zum Qubit @showdialog

Ein klassisches **Bit** hat den Wert **0** oder **1**.

Ein Quantencomputer verwendet **Qubits**. Ein Qubit besitzt ebenfalls zwei Grundzustände:

* `|0⟩`
* `|1⟩`

Zusätzlich kann sich ein Qubit in einer **Superposition** dieser beiden Zustände befinden.

Erst bei einer Messung erhalten wir einen klassischen Wert, also `0` oder `1`.

## Die Bloch-Kugel @showdialog

Die **Bloch-Kugel** ist eine geometrische Darstellung der Zustände eines einzelnen Qubits.

Der Nordpol steht für `|0⟩`, der Südpol für `|1⟩`. Andere Punkte auf der Oberfläche stellen Superpositionszustände dar.

Quantengatter verändern den Zustand des Qubits. Auf der Bloch-Kugel können wir uns diese Veränderungen als Drehungen vorstellen.

![Bloch-Kugel mit Qubit im Zustand 0](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/x_gate.gif)

## MicroQiskit @showdialog

Für die Übungen verwenden wir die MakeCode-Erweiterung **MicroQiskit**.

Die Erweiterung wird für dieses Tutorial **automatisch geladen**.

Wenn du sie später in einem eigenen MakeCode-Projekt verwenden möchtest:

1. Öffne ein neues Projekt im Calliope MakeCode-Editor.
2. Öffne unter **Fortgeschritten** den Bereich **Erweiterungen**.
3. Suche nach `https://github.com/heini208/makecode-qiskit`.
4. Wähle die Erweiterung aus.

Danach erscheint links im Werkzeugkasten die Kategorie **MicroQiskit**.

## Unser erster Circuit

Erstelle jetzt einen Quantenschaltkreis mit **einem Qubit** und **einem klassischen Bit**.

- :mouse pointer: Öffne links im Werkzeugkasten **MicroQiskit**.
- :mouse pointer: Öffne **Qiskit Grundlagen**.
- :mouse pointer: Suche im Bereich **Circuits** den Block zum Erstellen eines Circuits.
- :mouse pointer: Ziehe den Block in den Arbeitsbereich und lasse beide Werte auf `1`.

Der erste Wert legt die Anzahl der Qubits fest. Der zweite Wert legt die Anzahl der klassischen Bits fest, in denen später Messergebnisse gespeichert werden.

```blocks
// @highlight
let circuit = microQiskit.createCircuit(1, 1)
```

## Das X-Gatter

Das Qubit startet im Zustand `|0⟩`.

Das **X-Gatter** dreht den Zustand um 180° um die X-Achse. Dadurch wird aus `|0⟩` der Zustand `|1⟩`.

![X-Gatter auf der Bloch-Kugel](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/x_gate.gif)

- :mouse pointer: Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
- :mouse pointer: Ziehe den Block zum Anwenden eines Grundgatters unter die Circuit-Erstellung.
- :mouse pointer: Wähle **X** und lasse **Qubit 0** eingestellt.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.X, 0)
```

## Das Y-Gatter

Auch das **Y-Gatter** entspricht einer Drehung um 180°. Diesmal erfolgt die Drehung um die Y-Achse.

![Y-Gatter auf der Bloch-Kugel](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/y_gate.gif)

Ändere im Gatter-Block **X** zu **Y**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.Y, 0)
```

## Freie Drehungen mit RX

Nicht jede Drehung muss 180° groß sein.

Mit **RX** kannst du einen frei wählbaren Winkel um die X-Achse drehen. Der Winkel wird in **Grad** angegeben.

![RX mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/rx_pi_2.gif)

- :mouse pointer: Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
- :mouse pointer: Suche den **RX**-Block.
- :mouse pointer: Stelle den Winkel auf **90°**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyRX(circuit, 90, 0)
```

## Drehungen um die Y-Achse

Für weitere frei wählbare Rotationen gibt es unter **Qiskit Erweitert** einen Rotationsblock.

Wähle **RY** und einen Winkel von **90°**.

![RY mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/ry_pi_2.gif)

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyRotationGate(circuit, microQiskit.RotationGate.RY, 90, 0)
```

## Superposition mit Hadamard

Jetzt kommt eine der wichtigsten Operationen: das **Hadamard-Gatter**, kurz **H**.

Aus dem Startzustand `|0⟩` erzeugt H eine gleichgewichtete Superposition. Bei einer anschließenden Messung erhalten wir `0` und `1` jeweils mit ungefähr gleicher Wahrscheinlichkeit.

In dieser Visualisierung wird H als aufeinanderfolgende Rotation um Y und X dargestellt.

![Hadamard als Y- und X-Rotation](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/hadamard_y90_x180.gif)

- :mouse pointer: Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
- :mouse pointer: Verwende wieder den Block für ein Grundgatter.
- :mouse pointer: Wähle diesmal **H**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
```

## Zweimal Hadamard

Ein Hadamard-Gatter kann auch wieder rückgängig gemacht werden.

Wendest du **H zweimal** direkt hintereinander an, kehrt das Qubit zum ursprünglichen Zustand zurück.

![Zweimal Hadamard](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/hadamard_then_hadamard.gif)

Füge ein zweites H-Gatter hinzu.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
```

## Messen

Bisher haben wir nur den Quantenzustand verändert. Um ein klassisches Ergebnis zu erhalten, müssen wir messen.

- :mouse pointer: Öffne **MicroQiskit → Qiskit Grundlagen → Messung**.
- :mouse pointer: Ziehe **alle Qubits in Circuit messen** unter das H-Gatter.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
// @highlight
microQiskit.measureAll(circuit)
```

Bei der Messung wird das Ergebnis in den klassischen Bits gespeichert.

## Circuit lokal ausführen

Jetzt führen wir den Circuit mit der lokalen MicroQiskit-Simulation auf dem Calliope aus.

- :mouse pointer: Öffne **MicroQiskit → Qiskit Grundlagen → Simulation**.
- :mouse pointer: Ziehe **Circuit lokal ausführen** unter die Messung.

Der Grundlagen-Block verwendet automatisch **1024 Shots**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.measureAll(circuit)
// @highlight
let job = microQiskit.runSimulationBasic(circuit)
```

Ein **Shot** ist eine einzelne Ausführung mit anschließender Messung.

## Ein Ergebnis anzeigen

Das Simulationsergebnis wird in einem **Job** gespeichert.

Mit **Bits als Text** können wir ein Messergebnis als Zeichenkette lesen.

- :mouse pointer: Öffne **MicroQiskit → Qiskit Grundlagen → Ergebnisse**.
- :mouse pointer: Verwende **Bits als Text von Job**.
- :mouse pointer: Stecke diesen Block in **zeige Text** aus der Kategorie **Grundlagen**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.measureAll(circuit)
let job = microQiskit.runSimulationBasic(circuit)
// @highlight
basic.showString(microQiskit.getJobResultText(job))
```

Starte das Programm mehrfach. Durch die Superposition kann als Ergebnis `0` oder `1` erscheinen.

## Mehr als ein Qubit @showdialog

Mit mehreren Qubits wächst die Anzahl möglicher Basiszustände sehr schnell.

Für `n` Qubits gibt es `2^n` mögliche Bitkombinationen.

* 1 Qubit: `2^1 = 2` Zustände
* 2 Qubits: `2^2 = 4` Zustände
* 3 Qubits: `2^3 = 8` Zustände

Zwei Qubits können also die Kombinationen `00`, `01`, `10` und `11` liefern.

## Quantenzufall von 0 bis 3

Erstelle einen neuen Circuit mit **2 Qubits** und **2 klassischen Bits**.

Wende auf beide Qubits ein Hadamard-Gatter an. Danach befinden sich alle vier Basiszustände in einer gleichgewichteten Superposition.

- :mouse pointer: Stelle den Circuit auf **2 Qubits** und **2 klassische Bits**.
- :mouse pointer: Wende **H** auf **Qubit 0** an.
- :mouse pointer: Wende **H** auf **Qubit 1** an.
- :mouse pointer: Miss alle Qubits und führe den Circuit lokal aus.
- :mouse pointer: Zeige das Ergebnis als Text an.

```blocks
let circuit = microQiskit.createCircuit(2, 2)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 1)
microQiskit.measureAll(circuit)
let job = microQiskit.runSimulationBasic(circuit)
basic.showString(microQiskit.getJobResultText(job))
```

Die vier möglichen Ergebnisse können als Zahlen interpretiert werden:

* `00 = 0`
* `01 = 1`
* `10 = 2`
* `11 = 3`

## Nächster Schritt @showdialog

Damit haben wir die Grundlage für ein Spiel geschaffen.

Im nächsten Teil bauen wir aus den Quantenergebnissen **Schere, Stein, Papier** und untersuchen, wie wir die Wahrscheinlichkeiten gezielt verändern können.

```package
qiskit=github:heini208/makecode-qiskit#v0.1.2
```
