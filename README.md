# Modular Gas Sensor

## Table of Contents
* [Summary](#Summary)
* [Setup](#Setup)
* [Installation](#Installation)


## Summary
The Modular Gas Sensor uses 17 gas sensors that consist of:
<li>DFRobot CO2 Sensor V1.2</li>
<li>DHT22 Temperature and Humidity Sensor</li>
<li>DFRobot Ozone Sensor (0-10ppm) v1.0 (I2C)</li>
<li>DFRobot Gravity Formaldehyde (HCHO) Sensor (DAC)</li>
<li>SGP40 VOC (Volatile Organic Compound) Sensor (I2C)</li>
<li>Figaro TGS2611 Air Contaminants Sensor with drive board module</li>
<li>CJMCU-1100 MS-1100 VOC Gas Sensor Module Formaldehyde Benzene Gas Induction</li>
<li>MH-Z14 NDIR CO2 Infrared Sensor Module MH-Z14A Carbon Dioxide Sensor for CO2 (0-5000ppm, Serial Spot PWM)</li>
<li>MQ-2, MQ-3, MQ-4, MQ-5, MQ-6, MQ-7, MQ-8, MQ-9, MQ-135 Smoke Detection liquefied Methane Gas Sensor Module</li>

The data gathered from the sensors listed above during the cooking process will constitute a chemical signature which will be used to analyze the cumulative gas concentration with respect to time. The gas sensor shell stores these sensors, and the hardware which extracts and processes data which includes a custom PCB and a Raspberry Pi Zero 2W. All components of the gas sensor shell are modular, meaning it can be modified to store any amount of gas sensors if the necessary parts are made. More visual explanation can be found [here](https://selim-emir-can.github.io/GasSensor.html).

## Setup

### SGP40 VOC Sensor and DFRobot Ozone Sensor (0-10ppm) v1.0
* enable I2C connection from settings using sudo raspi-config
* connect SDA to GPIO 2, SCL to GPIO 3

### DHT22 Digital Temperature and Humidity Sensor
* connect GPIO 4 pin to DAT pin

Note: The temperature sensor does not work according to specification if measurements are taken within a time interval less then 3 seconds.

### Other Gas Sensors
* connect rest of the gas sensors to MCP3008 ADC Converter channels

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

### DFRobot_Ozone Library
sudo apt-get update <br />
sudo apt-get upgrade <br />
git clone https://github.com/DFRobot/DFRobot_OzoneSensor <br />

### Adafruit_DHT Library
sudo pip3 install Adafruit_DHT

### smbus Library
sudo apt-get install python-smbus

### bcm2835 Library
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz <br />
tar zxvf bcm2835-1.60.tar.gz <br />
cd bcm2835-1.60/ <br />
sudo ./configure <br />
sudo make <br />
sudo make check <br />
sudo make install <br />

### wiringpi Library
sudo apt-get install wiringpi <br />
cd /tmp <br />
wget https://project-downloads.drogon.net/wiringpi-latest.deb <br />
sudo dpkg -i wiringpi-latest.deb <br />
gpio -v <br />
