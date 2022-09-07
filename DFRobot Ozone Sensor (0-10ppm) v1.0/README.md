# DFRobot Ozone Sensor (0-10ppm) v1.0

## Table of Contents
* [Summary](#Summary)
* [Setup](#Setup)
* [Installation](#Installation)


## Summary
The DFRobot Ozone Sensor (0-10ppm) v1.0 has a VCC pin, GND pin, SDA (Serial Data) pin, SCL (Serial Clock) pin and transmits data to the Raspberry Pi Zero 2W through the I2C communication protocol.

* DFRobot_Ozone.py defines the basic structure of the DFRobot_Ozone class, the implementation of the basic methods.
* get_ozone_data.py reads ozone concentration of one part per billion (PPB) using UART mode.

More documentation can be found [here](https://wiki.dfrobot.com/Gravity_IIC_Ozone_Sensor_(0-10ppm)%20SKU_SEN0321).

## Setup
* enable I2C connection from settings using sudo raspi-config
* connect SDA to GPIO 2, SCL to GPIO 3

## Installation
get_ozone_data.py uses the DFRobot_Ozone library can be downloaded using:

### DFRobot_Ozone Library
sudo apt-get update <br />
sudo apt-get upgrade <br />
git clone https://github.com/DFRobot/DFRobot_OzoneSensor <br />
