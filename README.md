# (NOT FINISHED) Modular Gas Sensor

## Table of Contents
* [Summary](#Summary)
* [Setup](#Setup)
* [Installation](#Installation)


## Summary
The Modular Gas Sensor uses 17 gas sensors that consist of:
li>DHT22 Temperature and Humidity Sensor</li>
<li>SGP40 VOC (Volatile Organic Compound) Sensor (I2C)</li>
<li>DFRobot Ozone Sensor (0-10ppm) v1.0 (I2C)</li>
<li>DFRobot Gravity Formaldehyde (HCHO) Sensor (DAC)</li>
<li>MQ-2, MQ-3, MQ-4, MQ-5, MQ-6, MQ-7, MQ-8, MQ-9, MQ-135 Smoke Detection liquefied Methane Gas Sensor Module</li>
<li> TO BE FINISHED</li>

## Setup

### First MCP3008 ADC Converter
* connect the GPIO 18 pin to Clock (CLK)
* connect the GPIO 23 pin to Master Input Slave Output (MISO)
* connect the GPIO 24 pin to Master Output Slave Input (MOSI)
* connect the GPIO 25 pin to Chip Select (CS)

### Second MCP3008 ADC Converter
* connect the GPIO 18 pin to Clock (CLK)
* connect the GPIO 23 pin to Master Input Slave Output (MISO)
* connect the GPIO 24 pin to Master Output Slave Input (MOSI)
* connect the GPIO 26 pin to Chip Select (CS)


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
