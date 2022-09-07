# DHT22 Digital Temperature and Humidity Sensor

## Table of Contents
* [Summary](#Summary)
* [Setup](#Setup)
* [Installation](#Installation)

## Summary
The DHT22 Digital Temperature and Humidity Sensor has a DAT (Data) pin, a VCC pin, and a GND pin.
Temp-sensor.py file prints the temperature and humidity readings to the terminal every 3 seconds.
More documentation can be found [here](https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf).


## Setup
* connect GPIO 4 pin to DAT pin

Note: The temperature sensor does not work according to specification if measurements are taken within a time interval less then 3 seconds.


## Installation
Temp-sensor.py file uses the Adafruit_DHT library which can be downloaded using:

sudo pip3 install Adafruit_DHT
