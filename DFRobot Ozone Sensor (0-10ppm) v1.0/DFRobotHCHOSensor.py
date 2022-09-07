import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import numpy as np
import time

#1st ADC Converter Config
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def PPM_Reading(reading):
    return(3.125*reading - 1.25)

#Convert Analog Data to Digital Data and store it in an np array
print('Reading MCP3008 values, press Ctrl-C to quit...')
try:
        while(True):
            PPM_Reading(mcp.read_adc(0))
            time.sleep(1)

    except KeyboardInterrupt:
        exit()
  

