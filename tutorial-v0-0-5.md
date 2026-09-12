# Quantencomputing mit MicroQiskit

## Willkommen @showdialog

**Tutorial-Version 0.0.5, Stand 12.09.2026**

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

Das **X-Gatter** dreht das Qubit um 180° um die X-Achse. Aus dem Startzustand `|0⟩` wird dadurch `|1⟩`.

![X-Gatter auf der Bloch-Kugel](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/v005_x_gate.gif)

Jetzt probierst du das Gate selbst aus:

1. Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
2. Füge den Block zum Anwenden eines Grundgatters zwischen Circuit-Erstellung und Messung ein.
3. Öffne das Dropdown im neuen Gate-Block.
4. Wähle **X**.
5. Lass **Qubit 0** eingestellt.
6. Drücke **Taste A** mehrmals und beobachte die Anzeige.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.X, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** Das Ergebnis sollte jedes Mal `1` sein, weil X den Zustand von `|0⟩` nach `|1⟩` dreht.

## 6. Das Y-Gatter

Das **Y-Gatter** dreht ebenfalls um 180°, diesmal um die Y-Achse.

![Y-Gatter auf der Bloch-Kugel](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/v005_y_gate.gif)

Probiere es direkt aus:

1. Lass deinen bisherigen Gate-Block stehen.
2. Öffne das Dropdown, in dem gerade **X** ausgewählt ist.
3. Ändere **X** zu **Y**.
4. Drücke **Taste A** mehrmals.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.Y, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** Auch hier sollte immer `1` erscheinen. X und Y führen vom Nordpol zum Südpol, aber über unterschiedliche Drehachsen.

## 7. Das Hadamard-Gatter

Das **Hadamard-Gatter**, kurz **H**, bringt `|0⟩` in eine gleichgewichtete Superposition.

![Hadamard-Gatter](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/v005_hadamard_y90_x180.gif)

Probiere auch dieses Gate selbst aus:

1. Öffne wieder das Dropdown im Gate-Block.
2. Ändere **Y** zu **H**.
3. Drücke **Taste A** mindestens zehnmal.
4. Zähle grob, wie oft `0` und wie oft `1` erscheint.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** `0` und `1` sollten ungefähr gleich häufig erscheinen. Beide Ergebnisse haben eine Wahrscheinlichkeit von 50 %.

## 8. Hadamard zweimal

Ein H-Gatter kann sich selbst wieder rückgängig machen.

![Zweimal Hadamard](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/v005_hadamard_then_hadamard.gif)

Teste das:

1. Füge direkt hinter dem ersten H-Gatter einen zweiten Grundgatter-Block ein.
2. Öffne dessen Dropdown und wähle ebenfalls **H**.
3. Drücke **Taste A** mehrmals.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** Jetzt sollte wieder immer `0` erscheinen. Zwei H-Gatter hintereinander bringen den Zustand zurück zu `|0⟩`.

Entferne danach den zweiten H-Block wieder.

## 9. Das Z-Gatter

Das **Z-Gatter** dreht um 180° um die Z-Achse. Eine Z-Drehung verändert vor allem die Phase.

Teste zuerst Z alleine:

1. Öffne das Dropdown im Gate-Block.
2. Ändere **H** zu **Z**.
3. Drücke **Taste A** mehrmals.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.Z, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** Es erscheint weiterhin immer `0`. Das Qubit startet auf der Z-Achse. Eine Drehung um genau diese Achse ändert die direkte Messwahrscheinlichkeit nicht.

Jetzt machen wir die Phasenänderung sichtbar:

1. Ändere den ersten Gate-Block zu **H**.
2. Füge dahinter einen zweiten Grundgatter-Block ein und wähle **Z**.
3. Füge dahinter einen dritten Grundgatter-Block ein und wähle **H**.
4. Drücke **Taste A**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.Z, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** Jetzt erscheint `1`. Die Phasenänderung durch Z wurde durch das letzte H-Gatter in einen messbaren Unterschied umgewandelt.

Entferne danach die drei Gates, damit du für die Rotationen wieder mit `|0⟩` beginnst.

## 10. RX: Drehung um die X-Achse

Mit dem Rotationsblock kannst du **RX**, **RY** und **RZ** über ein Dropdown auswählen und den Winkel selbst festlegen.

![RX mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/v005_rx_pi_2.gif)

Teste RX:

1. Öffne **MicroQiskit → Qiskit Grundlagen → Gatter**.
2. Füge den Rotationsblock vor der Messung ein.
3. Öffne das Gate-Dropdown und wähle **RX**.
4. Stelle den Winkel auf **90°**.
5. Drücke **Taste A** mehrfach.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyRotationGate(circuit, microQiskit.RotationGate.RX, 90, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** Bei 90° liegt der Zustand auf dem Äquator. `0` und `1` sollten ungefähr 50/50 erscheinen.

## 11. RX mit 45° und 135°

Jetzt veränderst du nur den Winkel und beobachtest, wie sich die Wahrscheinlichkeit verschiebt.

1. Lass im Dropdown **RX** ausgewählt.
2. Ändere den Winkel auf **45°**.
3. Drücke **Taste A** oft.
4. Danach ändere den Winkel auf **135°**.
5. Drücke wieder oft **Taste A**.

Bei **45°** liegt der Zustand näher am Nordpol. Deshalb sollte `0` deutlich häufiger erscheinen.

Bei **135°** liegt der Zustand näher am Südpol. Deshalb sollte `1` deutlich häufiger erscheinen.

Ungefähr gilt:

* RX 45°: 85 % `0`, 15 % `1`
* RX 90°: 50 % `0`, 50 % `1`
* RX 135°: 15 % `0`, 85 % `1`

Probiere danach gern noch einen eigenen Winkel aus.

## 12. RY ausprobieren

![RY mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/v005_ry_pi_2.gif)

Jetzt probierst du die gleiche Idee mit der Y-Achse:

1. Öffne das Dropdown im Rotationsblock.
2. Ändere **RX** zu **RY**.
3. Stelle den Winkel zunächst auf **90°**.
4. Drücke **Taste A** mehrfach.
5. Probiere danach auch **45°** und **135°**.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyRotationGate(circuit, microQiskit.RotationGate.RY, 90, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** Bei 90° ungefähr 50/50. Bei 45° häufiger `0`, bei 135° häufiger `1`.

## 13. RZ ausprobieren

![RZ mit 90 Grad](https://raw.githubusercontent.com/heini208/makecode_qiskit_tutorial/main/images/v005_rz_pi_2.gif)

Jetzt testest du die Rotation um die Z-Achse:

1. Öffne das Dropdown im Rotationsblock.
2. Ändere **RY** zu **RZ**.
3. Stelle den Winkel auf **90°**.
4. Drücke **Taste A** mehrfach.

```blocks
let circuit = microQiskit.createCircuit(1, 1)
microQiskit.applyRotationGate(circuit, microQiskit.RotationGate.RZ, 90, 0)
microQiskit.measureAll(circuit)

input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    let job = microQiskit.runSimulationBasic(circuit)
    basic.showString(microQiskit.getJobResultText(job))
})
```

**Was solltest du sehen?** Weiterhin immer `0`. Das Qubit startet auf der Z-Achse, deshalb ändert eine reine RZ-Drehung seine direkte Messwahrscheinlichkeit nicht.

## Was haben wir bisher gelernt? @showdialog

Du hast jetzt den vollständigen Aufbau eines einfachen Qiskit-Programms verwendet:

**Circuit → Gates → Messung → Job → Ergebnis**

Du hast außerdem jedes wichtige Ein-Qubit-Gate selbst über die Dropdowns ausgewählt und die Auswirkung auf das Messergebnis beobachtet.

Jetzt nutzen wir genau diese Bausteine für ein eigenes Spiel.

## Exkurs: echter IBM-Quantencomputer @showdialog

Bisher wurde jeder Circuit direkt auf dem Calliope mit MicroQiskit simuliert.

Der gleiche Circuit kann auch an einen echten IBM-Quantencomputer geschickt werden. Dafür wird die separate Qiskit-Bridge auf einem Computer benötigt.

Die Einrichtung ist hier beschrieben:

[MicroQiskit: Mit IBM Quantum verbinden](https://github.com/heini208/makecode-qiskit#mit-ibm-quantum-verbinden)

Für unser Spiel verwenden wir weiterhin die lokale Simulation.

## 14. Vier Spielmöglichkeiten mit zwei Qubits

Wir bauen jetzt **Schere, Stein, Papier, Brunnen**.

Dafür brauchen wir vier mögliche Zufallsergebnisse. Mit zwei Qubits bekommen wir genau vier Bitkombinationen:

* `00`
* `01`
* `10`
* `11`

Wir ordnen sie so zu:

* `00` → Stein
* `01` → Papier
* `10` → Schere
* `11` → Brunnen

Erstelle dafür einen neuen Circuit:

1. Ändere den Circuit auf **2 Qubits** und **2 klassische Bits**.
2. Füge einen Grundgatter-Block ein und wähle im Dropdown **H** für **Qubit 0**.
3. Füge einen zweiten Grundgatter-Block ein und wähle ebenfalls **H**, diesmal für **Qubit 1**.
4. Miss danach alle Qubits.

```blocks
let circuit = microQiskit.createCircuit(2, 2)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 0)
microQiskit.applyBasicGate(circuit, microQiskit.BasicGate.H, 1)
microQiskit.measureAll(circuit)
```

Weil beide Qubits mit H in eine gleichgewichtete Superposition gebracht werden, sind `00`, `01`, `10` und `11` gleich wahrscheinlich.

## 15. Ein neues Ergebnis durch Schütteln

Bisher hast du mit Taste A ein Ergebnis erzeugt. Für das Spiel soll jetzt **Schütteln** der Auslöser sein.

1. Lösche den bisherigen **wenn Knopf A geklickt**-Block.
2. Öffne **Eingabe**.
3. Ziehe **wenn geschüttelt** in den Arbeitsbereich.
4. Öffne **Grundlagen** und füge ganz oben im Schüttel-Block **Bildschirm löschen** ein.
5. Öffne **Musik** und füge darunter **spiele Ton** ein.
6. Öffne **MicroQiskit → Qiskit Grundlagen → Simulation** und füge **Circuit lokal ausführen** darunter ein.
7. Speichere den erzeugten Job in der Variable `job`.
8. Öffne **MicroQiskit → Qiskit Grundlagen → Ergebnisse** und lies mit **Bits als Text von Job** ein Ergebnis aus.
9. Speichere dieses Ergebnis in einer neuen Textvariable `result`.

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
})
```

Jetzt passiert bei jedem Schütteln bereits etwas Neues: Das alte Bild wird gelöscht, ein Ton wird abgespielt und ein neues Quantenergebnis wird erzeugt.

## 16. Prüfen, ob das Ergebnis 00 ist

Jetzt bauen wir die erste Zuordnung.

1. Öffne **Logik**.
2. Ziehe einen **wenn ... dann ... sonst**-Block unter die Zeile, in der `result` gesetzt wird.
3. Öffne **Logik** erneut und nimm einen Vergleichsblock mit **=**.
4. Ziehe aus **Variablen** die Variable `result` auf die linke Seite des Vergleichs.
5. Ziehe aus **Text** einen Textblock auf die rechte Seite.
6. Schreibe dort `00` hinein.

Der erste Fall lautet jetzt:

**Wenn result = "00", dann ...**

Für `00` wollen wir **Stein** anzeigen.

## 17. Zeichne dein Symbol für Stein

1. Öffne **Grundlagen**.
2. Ziehe **zeige LEDs** in den `00`-Zweig deines Wenn-Blocks.
3. Im LED-Block siehst du eine 5×5-Matrix.
4. Klicke einzelne Punkte an, bis dein Bild für einen **Stein** so aussieht, wie du ihn darstellen möchtest.

Es gibt kein vorgeschriebenes Bild. Wichtig ist nur, dass du dein Symbol später eindeutig wiedererkennst.

```blocks
let result = "00"
if (result == "00") {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
    `)
}
```

## 18. Füge Papier als zweiten Fall hinzu

Jetzt brauchen wir einen zweiten Vergleich für `01`.

1. Klicke beim Wenn-Block auf das **Plus**, um einen **sonst wenn**-Zweig hinzuzufügen.
2. Kopiere oder baue wieder einen **=**-Vergleich.
3. Vergleiche `result` diesmal mit `01`.
4. Ziehe in diesen Zweig wieder einen **zeige LEDs**-Block.
5. Zeichne ein eigenes Symbol, das für dich wie **Papier** aussieht.

Der zweite Fall lautet jetzt:

**Sonst wenn result = "01", dann Papier anzeigen.**

## 19. Füge Schere als dritten Fall hinzu

Jetzt kommt `10`.

1. Füge mit dem **Plus** noch einen **sonst wenn**-Zweig hinzu.
2. Vergleiche `result` mit `10`.
3. Ziehe wieder **zeige LEDs** in diesen Zweig.
4. Zeichne mit den 25 auswählbaren LEDs ein Symbol, das für dich wie eine **Schere** aussieht.

Der dritte Fall lautet:

**Sonst wenn result = "10", dann Schere anzeigen.**

## 20. Füge Brunnen als letzten Fall hinzu

Es bleibt nur noch die Kombination `11`.

Weil `00`, `01` und `10` bereits geprüft werden, kann der letzte **sonst**-Zweig direkt für `11` verwendet werden.

1. Stelle sicher, dass dein Wenn-Block am Ende einen **sonst**-Zweig besitzt.
2. Ziehe dort wieder **zeige LEDs** hinein.
3. Zeichne ein eigenes Symbol für den **Brunnen**, zum Beispiel einen Kreis.

Jetzt hast du alle vier Ergebnisse abgedeckt:

**00 → Stein, 01 → Papier, 10 → Schere, 11 → Brunnen**

## 21. Setze alles zusammen

Dein Schüttel-Block sollte jetzt diese Reihenfolge haben:

1. Bildschirm löschen.
2. Ton abspielen.
3. Circuit lokal ausführen.
4. Ergebnis als Text lesen.
5. `00`, `01`, `10` und sonst `11` unterscheiden.
6. Das passende selbst gezeichnete LED-Bild anzeigen.

Ein vollständiges Beispiel sieht so aus:

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

Du kannst die Beispielbilder jederzeit durch deine eigenen Symbole ersetzen.

## 22. Teste das Schütteln

Schüttle jetzt den Calliope.

Du solltest hören, dass ein Ton abgespielt wird. Danach erscheint eines deiner vier Symbole.

Schüttle noch einmal. Das alte Symbol wird zuerst gelöscht und danach wird ein neues Quantenergebnis erzeugt.

Probiere das mehrmals aus. Weil alle vier Bitkombinationen gleich wahrscheinlich sind, sollten mit der Zeit alle vier Symbole auftauchen.

## 23. Spiele gegen den Calliope

Jetzt ist dein Spiel fertig.

Du kannst selbst **Schere, Stein, Papier oder Brunnen** wählen. Schüttle gleichzeitig den Calliope und warte auf sein Symbol.

Für diese Variante gelten die Regeln:

* Schere schlägt Papier.
* Stein schlägt Schere.
* Papier schlägt Stein und Brunnen.
* Brunnen schlägt Stein und Schere.

Zeigt ihr dasselbe Symbol, ist es unentschieden.

Der Calliope trifft seine Wahl mit dem Zwei-Qubit-Circuit. Bei jedem Schütteln wird ein neues Ergebnis erzeugt.

## Geschafft! @showdialog

Du hast einen vollständigen Quantenschaltkreis aufgebaut, Gates und Rotationen ausprobiert, Messwahrscheinlichkeiten untersucht und daraus ein eigenes Spiel programmiert.

Du kannst jetzt direkt gegen deinen Calliope **Schere, Stein, Papier, Brunnen** spielen.

```package
qiskit=github:heini208/makecode-qiskit#v0.1.5
```
