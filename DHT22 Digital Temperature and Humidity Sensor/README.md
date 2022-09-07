## DHT22 Digital Temperature and Humidity Sensor
Temp-sensor.py file uses the Adafruit_DHT library which can be downloaded using:

sudo pip3 install Adafruit_DHT

The temperature sensor uses the GPIO PIN 4, a 5V voltage source, and GND to transmit data to the Raspberry Pi Zero 2W.
Temp-sensor.py file prints the temperature and hmuidity readings to the terminal every 3 seconds.

The temperature sensor does not work according to specification if measurements are taken within less then 3 seconds from the last one.