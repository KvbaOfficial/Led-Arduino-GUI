# RGB LED Arduino Gui

A simple project to control led lights using arduino and a gui interface in python.

## Introduction

This project allows you to control the colors of led lights using an arduino. the colors are sent via the serial port and set to the appropriate pwm values.

## Requirements

- Arduino (e.g., arduino uno)
- RGB led light (e.g., hw-479)
- [Arduino ide](https://www.arduino.cc/en/software)
- Python 3.x
- Required python libraries:
  - `pyserial`
  - `tkinter`
  - `ttkthemes`

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/kvbaofficial/led-arduino-gui.git
   cd led-arduino-gui
   ```

2. Install the required python libraries:

```sh
pip install pyserial ttkthemes
```

3. Open the `led.ino` file in the arduino ide.

4. Connect the led lights to the appropriate arduino pins:

   - red: pin 9
   - green: pin 10
   - blue: pin 11

5. Upload the code to the arduino.

## Usage

1. open the serial monitor in the arduino ide.
2. set the baud rate to 115200.
3. enter rgb values separated by commas (e.g., `255,0,0` for red) and press enter.

## License

This project is licensed under the mit license. see the [license](license.md) file for more details.
