# Grade9-Temperature-Alert

A Smart Temperature Monitoring System built with an Arduino Uno and a DHT22 sensor, simulated in Wokwi. An LED turns on when the temperature reaches the warning threshold of **38°C**.

## Wokwi Simulation

🔗 [Open the project in Wokwi](https://wokwi.com/projects/478633842103770113)

## Components

- Arduino Uno
- DHT22 temperature sensor
- Red LED
- 220Ω resistor
- Jumper wires

## Circuit Connections

| Component | Arduino Connection |
|---|---|
| DHT22 VCC | 5V |
| DHT22 SDA | Pin 2 |
| DHT22 GND | GND |
| LED anode (+) | Pin 8 (through 220Ω resistor) |
| LED cathode (−) | GND |

## Warning Threshold: 38°C

The sketch reads the temperature from the DHT22 and compares it to a threshold in an `if` statement:

- **Below 38°C** → temperature is normal, so the LED stays **OFF**.
- **38°C and above** → temperature is dangerously high, so the LED turns **ON** as a warning.

The threshold was changed to 38°C from the previous version of the project. The condition uses "greater than or equal to" (`>=`), so exactly 38°C triggers the warning.

```cpp
if (temperature >= 38) {
  digitalWrite(8, HIGH);   // LED ON
} else {
  digitalWrite(8, LOW);    // LED OFF
}
```

## Test Results

| Temperature | Expected LED | Result |
|---|---|---|
| 30°C | OFF | ✅ |
| 37°C | OFF | ✅ |
| 38°C | ON | ✅ |
| 42°C | ON | ✅ |


## How to Run

1. Open the Wokwi link above.
2. Make sure the **DHT sensor library** is installed (it appears in `libraries.txt`).
3. Click **Start the simulation**.
4. Click the DHT22 sensor and move the temperature slider.
5. Watch the LED switch on at 38°C and above.

## Files

- `sketch.ino`: Arduino code
- `README.md`: project documentation

## Author

Alex G. Alcantara, Grade 9
