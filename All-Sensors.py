import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import sys
import numpy as np
import csv
import time
sys.path.append("../")
from DFRobot_Ozone import *
import math
import struct
import smbus
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
# import ctypes

COLLECT_NUMBER   = 20              # collect number, the collection range is 1-100
IIC_MODE         = 0x01            # default use IIC1

'''
   The first  parameter is to select i2c0 or i2c1
   The second parameter is the i2c device address
   The default address for i2c is OZONE_ADDRESS_3
      OZONE_ADDRESS_0        0x70
      OZONE_ADDRESS_1        0x71
      OZONE_ADDRESS_2        0x72
      OZONE_ADDRESS_3        0x73
'''
ozone = DFRobot_Ozone_IIC(IIC_MODE ,OZONE_ADDRESS_3)
'''
  The module is configured in automatic mode or passive
    MEASURE_MODE_AUTOMATIC  active  mode
    MEASURE_MODE_PASSIVE    passive mode
'''
ozone.set_mode(MEASURE_MODE_AUTOMATIC)
#####################################################################################################################################################################################
# voc = ctypes.cdll.LoadLibrary('./voclib.so')

SGP40_CMD_FEATURE_SET = [0x20, 0x2F]
SGP40_CMD_MEASURE_TEST = [0X28,0X0E]
SGP40_CMD_SOFT_RESET = [0X00,0X06]
SGP40_CMD_HEATER_OFF = [0X36,0X15]
SGP40_CMD_MEASURE_RAW = [0X26,0X0F]
# SGP40_CMD_GET_SERIAL_ID = [0X36,0X82] #DATASHEET is not written ,but Sensirion have


CRC_TABLE = [
        0, 49, 98, 83, 196, 245, 166, 151, 185, 136, 219, 234, 125, 76, 31, 46,
        67, 114, 33, 16, 135, 182, 229, 212, 250, 203, 152, 169, 62, 15, 92, 109,
        134, 183, 228, 213, 66, 115, 32, 17, 63, 14, 93, 108, 251, 202, 153, 168,
        197, 244, 167, 150, 1, 48, 99, 82, 124, 77, 30, 47, 184, 137, 218, 235,
        61, 12, 95, 110, 249, 200, 155, 170, 132, 181, 230, 215, 64, 113, 34, 19,
        126, 79, 28, 45, 186, 139, 216, 233, 199, 246, 165, 148, 3, 50, 97, 80,
        187, 138, 217, 232, 127, 78, 29, 44, 2, 51, 96, 81, 198, 247, 164, 149,
        248, 201, 154, 171, 60, 13, 94, 111, 65, 112, 35, 18, 133, 180, 231, 214,
        122, 75, 24, 41, 190, 143, 220, 237, 195, 242, 161, 144, 7, 54, 101, 84,
        57, 8, 91, 106, 253, 204, 159, 174, 128, 177, 226, 211, 68, 117, 38, 23,
        252, 205, 158, 175, 56, 9, 90, 107, 69, 116, 39, 22, 129, 176, 227, 210,
        191, 142, 221, 236, 123, 74, 25, 40, 6, 55, 100, 85, 194, 243, 160, 145,
        71, 118, 37, 20, 131, 178, 225, 208, 254, 207, 156, 173, 58, 11, 88, 105,
        4, 53, 102, 87, 192, 241, 162, 147, 189, 140, 223, 238, 121, 72, 27, 42,
        193, 240, 163, 146, 5, 52, 103, 86, 120, 73, 26, 43, 188, 141, 222, 239,
        130, 179, 224, 209, 70, 119, 36, 21, 59, 10, 89, 104, 255, 206, 157, 172
        ]

#Without_humidity_compensation
#sgp40_measure_raw + 2*humi + CRC + 2*temp + CRC
WITHOUT_HUM_COMP = [0X26, 0X0F, 0X80, 0X00, 0XA2, 0X66, 0X66, 0X93] # default Temperature=25 Humidity=50
WITH_HUM_COMP = [0x26, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00] #Manual input

ADDR = 0x59

class SGP40:
    def __init__(self, address=ADDR):
        self.i2c = smbus.SMBus(1)
        self.address = address

        # feature set 0x3220
        self.write(SGP40_CMD_FEATURE_SET)
        time.sleep(0.25)
        Rbuf = self.Read()
        print('feature set:%#x'% ((int(Rbuf[0]) << 8) | Rbuf[1]))
        if ((int(Rbuf[0]) << 8) | Rbuf[1]) != 0x3220:
            raise RuntimeError("Self test failed")

        # Self Test 0xD400
        self.write(SGP40_CMD_MEASURE_TEST)
        time.sleep(0.25)
        Rbuf = self.Read()
        print('Self Test  :%#x'% ((int(Rbuf[0]) << 8) | Rbuf[1]))
                if ((int(Rbuf[0]) << 8) | Rbuf[1]) != 0xD400: #0x4B00 is failed,0xD400 pass
            raise RuntimeError("Self test failed")

        # reset
        # self.write(SGP40_CMD_SOFT_RESET)

    def Read(self):
        return self.i2c.read_i2c_block_data(self.address, 0, 3)#last byte is CRC8

    def write(self, cmd):
        self.i2c.write_byte_data(self.address, cmd[0], cmd[1])

    def write_block(self, cmd):
        self.i2c.write_i2c_block_data(self.address, cmd[0], cmd[1:8])

    def raw(self):
        """The raw gas value"""
        # recycle a single buffer
        self.write_block(WITHOUT_HUM_COMP)
        time.sleep(0.25)
        Rbuf = self.Read()
        return ((int(Rbuf[0]) << 8) | Rbuf[1])

    def measureRaw(self, temperature, humidity):
        # 2*humi + CRC
        #paramh = struct.pack(">H", math.ceil(humidity * 0xffff / 100))
        h = humidity * 0xffff // 100
        paramh = (h >> 8, h & 0xff)
        crch = self.__crc(paramh[0], paramh[1])

        # 2*temp + CRC
        #paramt = struct.pack(">H", math.ceil((temperature + 45) * 0xffff / 175))
        t = (temperature + 45) * 0xffff // 175
        paramt = (t >> 8, t & 0xff)
        crct = self.__crc(paramt[0], paramt[1])

        WITH_HUM_COMP[2:3] = paramh
        WITH_HUM_COMP[4] = int(crch)
        WITH_HUM_COMP[5:6] = paramt
        WITH_HUM_COMP[7] = int(crct)
        #print(WITH_HUM_COMP)
        self.write_block(WITH_HUM_COMP)

        time.sleep(0.03)
        Rbuf = self.Read()
        # print(Rbuf)
                return ((int(Rbuf[0]) << 8) | Rbuf[1])

    def __crc(self, msb, lsb):
        crc = 0xff
        crc ^= msb
        crc = CRC_TABLE[crc]
        if lsb is not None:
            crc ^= lsb
            crc = CRC_TABLE[crc]
        return crc
 #######################################################################################################################
system_voltage = 5
resolution = 1024
#1st ADC Converter Config
CLK = 11 # gpio 18 on rpi 3
MISO = 9 # gpio 23 on rpi 3
MOSI = 10 # gpio 24 on rpi 3
CS = 8 # gpio 25 on rpi 3
CS2 = 7 # gpio 26 on rpi 3
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
mcp2 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS2, miso=MISO, mosi=MOSI)
def PPM_Reading(reading):
    return(3.125*reading - 1.25)

def Analog_Read(ADC_Reading):
  return(ADC_Reading*(system_voltage/resolution))

#Convert Analog Data to Digital Data and store it in an np array
print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} | {8:>4} | {9:>4} | {10:>4} | {11:>4} | {12:>4} | {13:>4} | {14:>4} | {15:>4} | {16:>4} | {17:>4} |'.format(*range(18)))
print('-' * 57)
rows, cols = (1, 18) # 1 x 16 vector for two ADC conververters of size 8 and 2 other sensors
arr = np.zeros((rows, cols))

def createCSVfile(arr):
    path_to_csv_file = '/home/pi/DFRobot_OzoneSensor-master/python/raspberrypi/examples/AllSensor.csv' #path to csv file
    f = open(path_to_csv_file, 'w')
    writer = csv.writer(f)
    writer.writerows(arr)
    f.close()
# can also use for ozone sensor print("Raw Gas: ", sgp.raw())
#  print("measureRaw Gas: %d" %arr_voc [np.size(arr)-1])
#  print("Ozone concentration is %d PPB."%arr_oz[np.size(arr) - 1])
#  time.sleep(1)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(23, GPIO.IN)
#############################################################################
if __name__ == '__main__':
    sgp = SGP40()
    while(GPIO.input(23) == 0):
        # Read all the ADC channel values in an np array.
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            # print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity), ozone.get_ozone_data(COLLECT_NUMBER), sgp.measureRaw(25, 50))
            arr = np.append(arr, [
                [PPM_Reading(mcp.read_adc(0)), Analog_Read(mcp.read_adc(1)), Analog_Read(mcp.read_adc(2)),
                 Analog_Read(mcp.read_adc(3)), Analog_Read(mcp.read_adc(4)), Analog_Read(mcp.read_adc(5)),
                 PPM_Reading(mcp2.read_adc(0)), Analog_Read(mcp2.read_adc(1)), Analog_Read(mcp2.read_adc(2)),
                 Analog_Read(mcp2.read_adc(3)), Analog_Read(mcp2.read_adc(4)), Analog_Read(mcp2.read_adc(5)),
                 Analog_Read(mcp2.read_adc(6)), Analog_Read(mcp2.read_adc(7)), ozone.get_ozone_data(COLLECT_NUMBER),
                 sgp.measureRaw(25, 50), temperature, humidity]], axis=0)
            k = np.size(arr, axis=0) - 1
            print('| ', arr[k, 0], ' | ', arr[k, 1], ' | ', arr[k, 2], ' | ', arr[k, 3], ' | ', arr[k, 4], ' | ',
                  arr[k, 5], ' | ', arr[k, 6], ' | ', arr[k, 7], ' | ', arr[k, 8], ' | ', arr[k, 9], ' | ',
                  arr[k, 10], ' | ', arr[k, 11], ' | ', arr[k, 12], ' | ', arr[k, 13], ' | ', arr[k, 14], ' | ',
                  arr[k, 15], ' | ', arr[k, 16], ' | ', arr[k, 17], ' |')  # ,arr[k,18],' |')
        else:
            print("failure");
        time.sleep(3)
    print(np.size(arr))
    arr = np.delete(arr, 0, 0)
    createCSVfile(arr)
