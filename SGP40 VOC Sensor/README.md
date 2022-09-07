# SPG40 VOC (Volatile Organic Compound) Sensor

## Table of Contents
* [Summary](#Summary)
* [Setup](#Setup)
* [Installation](#Installation)


## Summary
SPG40 VOC Sensor has a VCC pin, GND pin, SDA (Serial Data) pin, SCL (Serial Clock) pin and transmits data to the Raspberry Pi Zero 2W through the I2C communication protocol. The SGP40.py file defines the basic structure of the SGP40 class, the implementation of the basic methods and prints. More documentation can be found [here](https://www.waveshare.com/wiki/SGP40_VOC_Sensor).

## Setup
* enable I2C connection from settings using sudo raspi-config
* connect SDA to GPIO 2, SCL to GPIO 3

## Installation
SGP40.py uses the smbus, bcm2835, and wiringpi libraries which can be downloaded using:

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

