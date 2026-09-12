# Quantencomputing mit MicroQiskit

## Willkommen @showdialog

**Tutorial-Version 0.0.2, Stand 12.09.2026**

Wenn du diese Zeile siehst, ist die aktuell überarbeitete Version des Tutorials geladen.

In diesem Tutorial programmierst du selbst einen einfachen Quantencomputer mit **MicroQiskit** und dem **Calliope mini**.

Dabei geht es nicht nur um Theorie. Jede wichtige Gate-Operation wird direkt im MakeCode-Editor ausprobiert und das Messergebnis wird mit **Taste A** auf der LED-Matrix angezeigt.

Die MicroQiskit-Erweiterung wird für dieses Tutorial automatisch geladen.

## Quantencomputing in Kürze @showdialog

Ein klassischer Computer arbeitet mit **Bits**, die entweder `0` oder `1` sind.

Ein Quantencomputer arbeitet mit **Qubits**. Ein Qubit besitzt ebenfalls die Grundzustände

* `|0⟩`
* `|1⟩`

kann sich aber auch in einer **Superposition** aus beiden Zuständen befinden.

Quantencomputer nutzen dafür Eigenschaften der Quantenphysik wie **Superposition**, **Verschränkung** und **Interferenz**.

Sie sind nicht für jede Aufgabe schneller als klassische Computer. Für bestimmte Problemklassen ermöglichen sie aber andere Rechenverfahren.

## Der Aufbau eines Qiskit-Programms @showdialog

Ein einfaches Qiskit-Programm folgt fast immer demselben Ablauf:

**Circuit erstellen → Qubits verändern → Qubits messen → Circuit ausführen → Job auslesen**

Ein **Circuit** enthält die Qubits und die Operationen, die auf ihnen ausgeführt werden.

**Gates** verändern den Zustand eines Qubits.

Eine **Messung** wandelt den Quantenzustand in ein klassisches Ergebnis um. Das Messergebnis wird in einem **klassischen Bit** gespeichert.

Wird der Circuit ausgeführt, entsteht ein **Job**. Aus diesem Job können wir anschließend die Messergebnisse auslesen.

Genau diesen Ablauf bauen wir jetzt einmal vollständig auf. Danach verändern wir nur noch die Gates und beobachten, was passiert.

## Die Bloch-Kugel @showdialog

Die **Bloch-Kugel** ist eine geometrische Darstellung des Zustands eines einzelnen Qubits.

Der Nordpol entspricht `|0⟩`. Dort erhalten wir bei einer Messung sicher `0`.

Der Südpol entspricht `|1⟩`. Dort erhalten wir sicher `1`.

Auf dem Äquator liegen Zustände, bei denen `0` und `1` bei einer Messung jeweils mit 50 % Wahrscheinlichkeit auftreten.

Bei allen anderen Punkten hängt die Wahrscheinlichkeit von der Höhe des Zustands auf der Kugel ab. Die Position um die Z-Achse beschreibt zusätzlich die **Phase**. Diese Phase kann spätere Gate-Operationen beeinflussen, ist bei einer direkten Messung in `0` oder `1` aber nicht allein sichtbar.

Quantengatter können wir uns auf der Bloch-Kugel als Drehungen vorstellen.

## MicroQiskit im Werkzeugkasten @showdialog

Die Erweiterung **MicroQiskit** ist in diesem Tutorial bereits geladen.

Im Werkzeugkasten findest du:

* **MicroQiskit → Qiskit Grundlagen → Circuits**
* **MicroQiskit → Qiskit Grundlagen → Gatter**
* **MicroQiskit → Qiskit Grundlagen → Messung**
* **MicroQiskit → Qiskit Grundlagen → Simulation**
* **MicroQiskit → Qiskit Grundlagen → Ergebnisse**
* **MicroQiskit → Qiskit Erweitert** für zusätzliche Operationen

In einem eigenen MakeCode-Projekt kannst du MicroQiskit später über **Erweiterungen** mit dieser Adresse importieren:

`https://github.com/heini208/makecode-qiskit`

## 1. Circuit erstellen

Wir beginnen mit einem Circuit aus **einem Qubit** und **einem klassischen Bit**.

1. Öffne **MicroQiskit**.
2. Öffne **Qiskit Grundlagen**.
3. Öffne **Circuits**.
4. Ziehe **Circuit mit 1 Qubits und 1 klassischen Bits erstellen** in den Arbeitsbereich.

Der erste Wert ist die Anzahl der Qubits. Der zweite Wert ist die Anzahl der klassischen Bits für Messergebnisse.

```blocks
// @highlight
let circuit = microQiskit.createCircuit(1, 1)
```

## 2. Qubit messen

Noch verändern wir das Qubit nicht. Ein neu erstelltes Qubit startet im Zustand `|0⟩`.

Jetzt fügen wir die Messung hinzu.

1. Öffne **MicroQiskit → Qiskit Grundlagen → Messung**.
2. Ziehe **alle Qubits in Circuit messen** unter die Circuit-Erstellung.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.measureAll(circuit)
```

Die Messung schreibt den Zustand von Qubit 0 in das klassische Bit 0.

## 3. Mit Taste A ausführen

Der Circuit ist jetzt beschrieben, aber noch nicht ausgeführt.

Wir wollen ihn jedes Mal ausführen, wenn **Taste A** gedrückt wird.

1. Öffne **Eingabe**.
2. Ziehe **wenn Knopf A geklickt** in den Arbeitsbereich.
3. Öffne **MicroQiskit → Qiskit Grundlagen → Simulation**.
4. Ziehe **Circuit lokal ausführen** in den Knopf-A-Block.

Beim Ausführen entsteht ein **Job**. Der Job enthält die Ergebnisse dieser Ausführung.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    // @highlight
    let job = microQiskit.runSimulationBasic(circuit)
})
```

Der Grundlagen-Block führt automatisch 1024 Shots aus. Ein Shot ist eine einzelne Ausführung mit Messung.

## 4. Messergebnis anzeigen

Jetzt lesen wir ein Messergebnis aus dem Job und zeigen es auf dem Calliope an.

1. Öffne **MicroQiskit → Qiskit Grundlagen → Ergebnisse**.
2. Nimm **Bits als Text von Job**.
3. Öffne **Grundlagen**.
4. Ziehe **zeige Text** in den Knopf-A-Block.
5. Stecke **Bits als Text von Job** in **zeige Text**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    // @highlight
    basic.showString(microQiskit.getJobResultText(job))
})
```

Drücke im Simulator oder auf dem Calliope **Taste A**.

Da wir das Qubit noch nicht verändert haben, sollte immer `0` erscheinen.

Damit steht jetzt unser vollständiger Ablauf:

**Circuit → Messung → Job → Ergebnis**

Als Nächstes verändern wir das Qubit mit Gates.

## 5. Das X-Gatter

Das **X-Gatter** dreht das Qubit um 180° um die X-Achse.

Aus `|0⟩` wird `|1⟩`.

![X-Gatter auf der Bloch-Kugel](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/x_gate.gif)

1. Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
2. Ziehe den Block zum Anwenden eines Grundgatters zwischen Circuit-Erstellung und Messung.
3. Wähle im Dropdown **X**.
4. Lasse **Qubit 0** eingestellt.
5. Drücke danach **Taste A**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.X, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Jetzt sollte immer `1` erscheinen.

## 6. Das Y-Gatter

Das **Y-Gatter** dreht ebenfalls um 180°, aber um die Y-Achse.

![Y-Gatter auf der Bloch-Kugel](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/y_gate.gif)

1. Ändere im vorhandenen Grundgatter das Dropdown von **X** auf **Y**.
2. Drücke **Taste A**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.Y, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Auch Y bringt `|0⟩` zum Südpol. Deshalb misst du wieder `1`.

Der Weg auf der Bloch-Kugel und die Phase unterscheiden sich jedoch vom X-Gatter.

## 7. Das Hadamard-Gatter

Das **Hadamard-Gatter**, kurz **H**, bringt `|0⟩` in eine gleichgewichtete Superposition.

In unserer Visualisierung wird H als eine 90°-Drehung um Y und anschließend eine 180°-Drehung um X dargestellt.

![Hadamard-Gatter](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/hadamard_y90_x180.gif)

1. Ändere das Grundgatter von **Y** auf **H**.
2. Drücke **Taste A** mehrfach.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Der Zustand liegt jetzt auf dem Äquator der Bloch-Kugel. Deshalb kann bei jedem Ausführen `0` oder `1` erscheinen.

Beide Ergebnisse haben jeweils 50 % Wahrscheinlichkeit.

## 8. Hadamard zweimal

Ein H-Gatter kann sich selbst wieder rückgängig machen.

Füge ein zweites **H** direkt nach dem ersten ein und drücke **Taste A**.

![Zweimal Hadamard](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/hadamard_then_hadamard.gif)

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Der Zustand kehrt zu `|0⟩` zurück. Das Ergebnis ist wieder immer `0`.

Entferne danach das zweite H-Gatter wieder.

## 9. Das Z-Gatter

Das **Z-Gatter** ist eine 180°-Drehung um die Z-Achse.

Wenn das Qubit direkt in `|0⟩` steht, sehen wir auf der Bloch-Kugel keine Positionsänderung. Z verändert in diesem Fall nur die Phase.

Um diese Phasenänderung messbar zu machen, verwenden wir:

**H → Z → H**

1. Lasse das erste **H** stehen.
2. Füge danach ein Grundgatter **Z** ein.
3. Füge danach ein weiteres Grundgatter **H** ein.
4. Drücke **Taste A**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
// @highlight
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.Z, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Jetzt erhältst du `1`.

Das zeigt einen wichtigen Unterschied: Eine Phase ist bei der direkten Messung nicht sichtbar, kann aber durch spätere Gates in einen messbaren Unterschied umgewandelt werden.

Entferne danach die drei Gates, damit der Circuit wieder leer ist.

## 10. RX mit 90°

Mit **RX** können wir nicht nur um 180°, sondern um einen frei wählbaren Winkel um die X-Achse drehen.

![RX mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/rx_pi_2.gif)

1. Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
2. Ziehe den **RX**-Block vor die Messung.
3. Stelle den Winkel auf **90°**.
4. Drücke **Taste A** mehrfach.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyRX(circuit, 90, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Nach 90° liegt der Zustand auf dem Äquator. Deshalb treten `0` und `1` jeweils mit 50 % Wahrscheinlichkeit auf.

## 11. RY mit 90°

Jetzt testen wir dieselbe Drehgröße um die Y-Achse.

![RY mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/ry_pi_2.gif)

1. Entferne den RX-Block.
2. Öffne **MicroQiskit → Qiskit Erweitert → Gatter**.
3. Ziehe den Rotationsblock vor die Messung.
4. Wähle **RY**.
5. Stelle **90°** ein.
6. Drücke **Taste A** mehrfach.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyRotationGate(circuit, microQiskit.RotationGate.RY, 90, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Auch hier liegt der Zustand nach 90° auf dem Äquator. Die Messwahrscheinlichkeiten sind deshalb wieder 50 % für `0` und 50 % für `1`.

## 12. RZ mit 90°

Zum Schluss drehen wir um die Z-Achse.

![RZ mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/rz_pi_2.gif)

1. Ändere im Rotationsblock **RY** zu **RZ**.
2. Lasse den Winkel auf **90°**.
3. Drücke **Taste A**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyRotationGate(circuit, microQiskit.RotationGate.RZ, 90, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Das Qubit startet auf der Z-Achse selbst. Eine Drehung um diese Achse verändert deshalb seine Messwahrscheinlichkeit nicht. Du erhältst weiterhin `0`.

RZ verändert aber die Phase und kann deshalb in Kombination mit anderen Gates einen messbaren Effekt haben.

## Was haben wir gebaut? @showdialog

Du hast jetzt den vollständigen Aufbau eines einfachen Qiskit-Programms verwendet:

1. **Circuit erstellen**
2. **Qubits mit Gates verändern**
3. **Qubits messen**
4. **Circuit ausführen**
5. **Job erhalten**
6. **Ergebnis aus dem Job lesen**

Die Bloch-Kugel zeigt den Zustand des Qubits vor der Messung.

Die Höhe auf der Kugel bestimmt die Wahrscheinlichkeiten von `0` und `1`. Die Position um die Z-Achse enthält zusätzlich Phaseninformation, die spätere Gates beeinflussen kann.

## Zwei Qubits @showdialog

Mit mehreren Qubits wächst die Anzahl möglicher Basiszustände.

Für `n` Qubits gibt es `2^n` mögliche Bitkombinationen.

* 1 Qubit: `2` Zustände
* 2 Qubits: `4` Zustände
* 3 Qubits: `8` Zustände

Bei zwei Qubits sind die möglichen Messergebnisse:

* `00`
* `01`
* `10`
* `11`

## Quantenzufall von 0 bis 3

Jetzt erzeugen wir mit zwei Qubits vier gleich wahrscheinliche Ergebnisse.

1. Ändere den Circuit auf **2 Qubits** und **2 klassische Bits**.
2. Verwende ein **H-Gatter auf Qubit 0**.
3. Verwende ein **H-Gatter auf Qubit 1**.
4. Miss beide Qubits.
5. Führe den Circuit wieder mit **Taste A** aus.
6. Zeige das Ergebnis mit **Bits als Text** an.

```blocks
let circuit = microQiskit.createCircuit(2, 2)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 1)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Drücke **Taste A** mehrfach.

Die vier Bitfolgen entsprechen vier Zahlen:

* `00 = 0`
* `01 = 1`
* `10 = 2`
* `11 = 3`

Damit haben wir die Grundlage für ein Quanten-Zufallsspiel wie **Schere, Stein, Papier**.

## Exkurs: echter IBM-Quantencomputer @showdialog

Bisher wurde jeder Circuit direkt auf dem Calliope mit MicroQiskit simuliert.

Der gleiche Circuit kann mit der Erweiterung auch an einen **echten IBM-Quantencomputer** geschickt werden. Dafür wird die separate Qiskit-Bridge auf einem Computer benötigt.

Im Blockbereich **MicroQiskit → Qiskit Grundlagen → Simulation** gibt es dafür **Circuit auf IBM Quantum ausführen**.

Der Ablauf des Programms bleibt gleich:

**Circuit → Gates → Messung → IBM-Job → Ergebnis**

Die Einrichtung des IBM-Kontos, des API-Keys und der Qiskit-Bridge ist hier beschrieben:

[MicroQiskit: Mit IBM Quantum verbinden](https://github.com/heini208/makecode-qiskit#mit-ibm-quantum-verbinden)

```package
qiskit=github:heini208/makecode-qiskit#v0.1.2
```
