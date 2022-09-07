# DFRobot Ozone Sensor (0-10ppm) v1.0
## Table of Contents

* [Summary](#Summary)
* [Setup](#Setup)
* [Installation](#Installation)


## Summary

The DFRobot Ozone Sensor (0-10ppm) v1.0 has a 5V voltage source pin, GND pin, SDA (Serial Data) pin, SCL (Serial Clock) pin and transmits data to the Raspberry Pi Zero 2W through the I2C communication protocol.

* DFRobot_Ozone.py defines the basic structure of the DFRobot_Ozone class, the implementation of the basic methods.
* get_ozone_data.py reads ozone concentration of one part per billion (PPB) using UART mode.

## Setup
* enable I2C connection from settings using sudo raspi-config
* connect SDA to GPIO 2, SCL to GPIO 3

## Installation

get_ozone_data.py uses the DFRobot_Ozone library can be downloaded using:

### DFRobot_Ozone Library

sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/DFRobot/DFRobot_OzoneSensor
