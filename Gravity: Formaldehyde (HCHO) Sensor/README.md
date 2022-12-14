# Gravity: Formaldehyde (HCHO) Sensor

## Table of Contents
* [Summary](#Summary)
* [Setup](#Setup)
* [Installation](#Installation)


## Summary
The Gravity: Formaldehyde (HCHO) Sensor has a VCC pin, GND pin, and a data pin. The sensor has a DAC mode and a UART mode. Setting the Formaldehyde (HCHO) Sensor to DAC mode, using an MCP3008 ADC converter, a Raspberry Pi Zero 2W, and DFRobotHCHOSensor.py voltage data corrolated to ozone concentration can be displayed in real time. More documentation can be found [here](https://www.dfrobot.com/product-1574.html).

## Setup

### MCP3008 ADC Converter
* connect the GPIO 18 pin to Clock (CLK)
* connect the GPIO 23 pin to Master Input Slave Output (MISO)
* connect the GPIO 24 pin to Master Output Slave Input (MOSI)
* connect the GPIO 25 pin to Chip Select (CS)
* connect the data pin to Channel 0 input

## Installation
DFRobotHCHOSensor.py file uses the Adafruit_GPIO and Adafruit_MCP3008 libraries which can be downloaded using:

### Adafruit_GPIO Library
sudo apt-get update <br />
sudo apt-get install build-essential python-pip python-dev python-smbus git <br />
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git <br />
cd Adafruit_Python_GPIO <br />
sudo python setup.py install <br />

### Adafruit_MCP3008 Library
sudo apt-get update <br />
sudo apt-get install build-essential python-dev python-smbus git <br />
cd ~ <br />
git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git <br />
cd Adafruit_Python_MCP3008 <br />
sudo python setup.py install <br />
