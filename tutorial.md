# Quantencomputing mit MicroQiskit

## Willkommen @showdialog

**Tutorial-Version 0.0.4, Stand 12.09.2026**

Wenn du diese Zeile siehst, ist die aktuell überarbeitete Version des Tutorials geladen.

In diesem Tutorial programmierst du selbst einfache Quantenschaltkreise mit **MicroQiskit** und dem **Calliope mini**.

Du probierst jedes wichtige Gate direkt aus, beobachtest die Messergebnisse und baust am Ende ein eigenes **Schere-Stein-Papier-Brunnen-Spiel** mit Quantenzufall.

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

**Circuit erstellen → Qubits mit Gates verändern → Qubits messen → Circuit ausführen → Job auslesen**

Ein **Circuit** beschreibt den Quantenschaltkreis. Er enthält Qubits und die Operationen, die auf ihnen ausgeführt werden.

**Gates** verändern den Zustand eines Qubits.

Eine **Messung** wandelt den Quantenzustand in ein klassisches Ergebnis um. Dieses Ergebnis wird in einem **klassischen Bit** gespeichert.

Wird der Circuit ausgeführt, entsteht ein **Job**. Aus diesem Job lesen wir anschließend die Messergebnisse.

Genau diesen Ablauf bauen wir zuerst einmal vollständig auf. Danach verändern wir nur noch die Gates und beobachten, was passiert.

## Die Bloch-Kugel @showdialog

Die **Bloch-Kugel** ist eine geometrische Darstellung des Zustands eines einzelnen Qubits.

Der Nordpol entspricht `|0⟩`. Dort erhalten wir bei einer Messung sicher `0`.

Der Südpol entspricht `|1⟩`. Dort erhalten wir sicher `1`.

Auf dem Äquator liegen Zustände, bei denen `0` und `1` bei einer Messung jeweils mit 50 % Wahrscheinlichkeit auftreten.

Liegt der Zustand näher am Nordpol, erscheint `0` häufiger. Liegt er näher am Südpol, erscheint `1` häufiger.

Die Position um die Z-Achse beschreibt zusätzlich die **Phase**. Diese Phase kann spätere Gate-Operationen beeinflussen, ist bei einer direkten Messung aber nicht allein sichtbar.

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

Jetzt lesen wir ein einzelnes Messergebnis aus dem Job und zeigen es auf dem Calliope an.

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

Damit steht unser vollständiger Ablauf:

**Circuit → Messung → Job → Ergebnis**

Jetzt verändern wir das Qubit mit Gates.

## 5. Das X-Gatter

Das **X-Gatter** dreht das Qubit um 180° um die X-Achse.

Aus `|0⟩` wird `|1⟩`.

![X-Gatter auf der Bloch-Kugel](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/x_gate.gif)

1. Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
2. Ziehe den Block zum Anwenden eines Grundgatters zwischen Circuit-Erstellung und Messung.
3. Öffne das Dropdown im Gate-Block und wähle **X**.
4. Lasse **Qubit 0** eingestellt.
5. Drücke **Taste A** und beobachte das Ergebnis.

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

1. Öffne das Dropdown im vorhandenen Gate-Block.
2. Ändere **X** zu **Y**.
3. Drücke **Taste A** und beobachte das Ergebnis.

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

1. Öffne wieder das Dropdown im Gate-Block.
2. Ändere **Y** zu **H**.
3. Drücke **Taste A** mehrfach und beobachte die Ergebnisse.

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

1. Füge einen zweiten Grundgatter-Block direkt hinter den ersten ein.
2. Öffne auch dort das Dropdown und wähle **H**.
3. Drücke **Taste A**.

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

Entferne danach den zweiten H-Block wieder.

## 9. Das Z-Gatter

Das **Z-Gatter** ist eine 180°-Drehung um die Z-Achse.

Wenn das Qubit direkt in `|0⟩` steht, verändert Z die Messwahrscheinlichkeit nicht. Um den Phaseneffekt sichtbar zu machen, verwenden wir:

**H → Z → H**

1. Lasse das erste **H** stehen.
2. Füge danach einen neuen Grundgatter-Block ein.
3. Öffne dessen Dropdown und wähle **Z**.
4. Füge danach noch einen Grundgatter-Block ein und wähle dort **H**.
5. Drücke **Taste A** und beobachte das Ergebnis.

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

Eine Phase ist bei der direkten Messung nicht sichtbar, kann aber durch spätere Gates in einen messbaren Unterschied umgewandelt werden.

Entferne danach die drei Gates, damit der Circuit wieder leer ist.

## 10. Rotationen mit RX

Bisher haben wir hauptsächlich 180°-Drehungen verwendet. Mit Rotationsgattern kannst du den Winkel selbst festlegen.

![RX mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/rx_pi_2.gif)

1. Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
2. Ziehe den Rotationsblock vor die Messung.
3. Öffne das Gate-Dropdown und wähle **RX**.
4. Stelle den Winkel zuerst auf **90°**.
5. Drücke **Taste A** mehrfach.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyRotationGate(circuit, microQiskit.RotationGate.RX, 90, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

Bei 90° liegt der Zustand auf dem Äquator. Deshalb erscheinen `0` und `1` ungefähr gleich häufig.

## 11. Was passiert bei 45° und 135°?

Jetzt wird die Verbindung zwischen Bloch-Kugel und Messwahrscheinlichkeit sichtbar.

1. Ändere den RX-Winkel von **90° auf 45°**.
2. Drücke **Taste A** viele Male.
3. Beobachte, welche Zahl deutlich häufiger erscheint.
4. Ändere den Winkel danach auf **135°**.
5. Drücke wieder mehrfach **Taste A**.

Bei **45°** liegt der Zustand noch näher am Nordpol. Deshalb erscheint `0` deutlich häufiger als `1`.

Bei **135°** liegt er näher am Südpol. Deshalb erscheint `1` deutlich häufiger als `0`.

Mathematisch gilt für einen Start in `|0⟩`:

* RX 45°: ungefähr **85 % 0** und **15 % 1**
* RX 90°: **50 % 0** und **50 % 1**
* RX 135°: ungefähr **15 % 0** und **85 % 1**

Probiere ruhig noch andere Winkel aus.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
// @highlight
microQiskit.applyRotationGate(circuit, microQiskit.RotationGate.RX, 45, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

## 12. RY ausprobieren

Jetzt drehen wir um die Y-Achse.

![RY mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/ry_pi_2.gif)

1. Öffne das Dropdown im Rotationsblock.
2. Ändere **RX** zu **RY**.
3. Stelle den Winkel wieder auf **90°**.
4. Drücke **Taste A** mehrfach und beobachte das Ergebnis.
5. Probiere danach auch **45°** oder **135°** aus.

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

Wie bei RX verändert der Winkel die Wahrscheinlichkeit für `0` und `1`.

## 13. RZ ausprobieren

Zum Schluss drehen wir um die Z-Achse.

![RZ mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/rz_pi_2.gif)

1. Öffne das Dropdown im Rotationsblock.
2. Ändere **RY** zu **RZ**.
3. Stelle **90°** ein.
4. Drücke **Taste A**.

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

Das Qubit startet auf der Z-Achse selbst. Eine Drehung um diese Achse verändert deshalb die direkte Messwahrscheinlichkeit nicht. Du erhältst weiterhin `0`.

RZ verändert aber die Phase und kann deshalb in Kombination mit anderen Gates einen messbaren Effekt haben.

## Was haben wir gebaut? @showdialog

Du hast jetzt den vollständigen Aufbau eines einfachen Qiskit-Programms verwendet:

1. **Circuit erstellen**
2. **Qubits mit Gates verändern**
3. **Qubits messen**
4. **Circuit ausführen**
5. **Job erhalten**
6. **Ergebnis aus dem Job lesen**

Außerdem hast du gesehen, dass die Position auf der Bloch-Kugel die Messwahrscheinlichkeiten beeinflusst.

Jetzt verwenden wir genau diese Bausteine für ein Spiel.

## Exkurs: echter IBM-Quantencomputer @showdialog

Bisher wurde jeder Circuit direkt auf dem Calliope mit MicroQiskit simuliert.

Der gleiche Circuit kann mit der Erweiterung auch an einen **echten IBM-Quantencomputer** geschickt werden. Dafür wird die separate Qiskit-Bridge auf einem Computer benötigt.

Im Blockbereich **MicroQiskit → Qiskit Grundlagen → Simulation** gibt es dafür **Circuit auf IBM Quantum ausführen**.

Der Ablauf bleibt gleich:

**Circuit → Gates → Messung → IBM-Job → Ergebnis**

Die Einrichtung des IBM-Kontos, des API-Keys und der Qiskit-Bridge ist hier beschrieben:

[MicroQiskit: Mit IBM Quantum verbinden](https://github.com/heini208/makecode-qiskit#mit-ibm-quantum-verbinden)

Für unser Spiel verwenden wir weiterhin die lokale Simulation.

## 14. Zwei Qubits ergeben vier Zustände

Für unser Spiel brauchen wir vier mögliche Ergebnisse:

* Stein
* Papier
* Schere
* Brunnen

Mit **zwei Qubits** erhalten wir genau vier mögliche Bitkombinationen:

* `00`
* `01`
* `10`
* `11`

Denn für `n` Qubits gibt es `2^n` mögliche Basiszustände.

Erstelle jetzt einen neuen Circuit mit **2 Qubits** und **2 klassischen Bits**.

Wende auf beide Qubits ein **H-Gatter** an. Dadurch werden alle vier Messergebnisse gleich wahrscheinlich.

```blocks
let circuit = microQiskit.createCircuit(2, 2)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 1)
microQiskit.measureAll(circuit)
```

## 15. Schütteln statt Taste A

Ein neues Spielergebnis soll jetzt durch **Schütteln** erzeugt werden.

1. Entferne den bisherigen Knopf-A-Block.
2. Öffne **Eingabe**.
3. Ziehe den Block **wenn geschüttelt** in den Arbeitsbereich.
4. Öffne **Grundlagen** und füge als erstes **Bildschirm löschen** ein.
5. Öffne **Musik** und füge danach **spiele Ton** ein.
6. Führe anschließend den Circuit lokal aus und speichere den Job.
7. Lies mit **Bits als Text** das Messergebnis aus dem Job.

Beim nächsten Schütteln wird dadurch zuerst das alte Symbol gelöscht, ein Ton abgespielt und anschließend ein neues Quantenergebnis erzeugt.

```blocks
let circuit = microQiskit.createCircuit(2, 2)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 1)
microQiskit.measureAll(circuit)

input.onGesture(Gesture.Shake, function () {
    // @highlight
    basic.clearScreen()
    music.playTone(262, 100)
    let job = microQiskit.runSimulationBasic(circuit)
    let result = microQiskit.getJobResultText(job)
})
```

## 16. Das Ergebnis auf ein Spielsymbol abbilden

Jetzt ordnen wir jeder Bitkombination ein Spielsymbol zu.

Wir verwenden:

* `00` → **Stein**
* `01` → **Papier**
* `10` → **Schere**
* `11` → **Brunnen**

1. Öffne **Logik**.
2. Ziehe einen **wenn ... dann ... sonst**-Block unter die Ergebnisvariable.
3. Vergleiche `result` mit dem Text `"00"`.
4. Füge weitere **sonst wenn**-Fälle für `"01"` und `"10"` hinzu.
5. Der letzte **sonst**-Fall steht dann für `"11"`.

```blocks
let circuit = microQiskit.createCircuit(2, 2)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 1)
microQiskit.measureAll(circuit)

input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    music.playTone(262, 100)
    let job = microQiskit.runSimulationBasic(circuit)
    let result = microQiskit.getJobResultText(job)

    // @highlight
    if (result == "00") {
    } else if (result == "01") {
    } else if (result == "10") {
    } else {
    }
})
```

## 17. Zeichne deine eigenen Symbole

Jetzt gestaltest du selbst, wie **Stein**, **Papier**, **Schere** und **Brunnen** auf der 5×5-LED-Matrix aussehen sollen.

1. Öffne **Grundlagen**.
2. Ziehe für jeden Fall einen **zeige LEDs**-Block hinein.
3. Klicke im Block die einzelnen LEDs an und zeichne dein eigenes Symbol.
4. Verwende für jede Bitkombination ein anderes Bild.

Hier ist nur ein mögliches Beispiel. Deine Symbole dürfen anders aussehen.

```blocks
let circuit = microQiskit.createCircuit(2, 2)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 1)
microQiskit.measureAll(circuit)

input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    music.playTone(262, 100)
    let job = microQiskit.runSimulationBasic(circuit)
    let result = microQiskit.getJobResultText(job)

    if (result == "00") {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
        `)
    } else if (result == "01") {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
        `)
    } else if (result == "10") {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
        `)
    } else {
        basic.showLeds(`
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
        `)
    }
})
```

## 18. Teste dein Quantenspiel

Dein Spiel ist fertig.

Schüttle den Calliope mehrmals.

Bei jedem Schütteln passiert jetzt Folgendes:

1. Das alte Symbol wird gelöscht.
2. Ein kurzer Ton wird abgespielt.
3. Der Zwei-Qubit-Circuit wird neu ausgeführt.
4. Es entsteht eines der Ergebnisse `00`, `01`, `10` oder `11`.
5. Das Ergebnis wird auf **Stein**, **Papier**, **Schere** oder **Brunnen** abgebildet.
6. Dein selbst gezeichnetes Symbol erscheint auf der LED-Matrix.

Da beide Qubits mit H in eine gleichgewichtete Superposition gebracht werden, sind alle vier Ergebnisse gleich wahrscheinlich.

Jetzt kannst du gegen eine andere Person oder einen zweiten Calliope spielen.

## Geschafft! @showdialog

Du hast einen vollständigen Quantenschaltkreis aufgebaut, verschiedene Gates getestet, Messwahrscheinlichkeiten auf der Bloch-Kugel untersucht und mit zwei Qubits ein eigenes Zufallsspiel programmiert.

Dabei hast du den grundlegenden Qiskit-Ablauf verwendet:

**Circuit → Gates → Messung → Job → Ergebnis**

Und aus einem echten Quantenergebnis wird nun direkt eine Aktion auf dem Calliope.

```package
qiskit=github:heini208/makecode-qiskit#v0.1.5
```
