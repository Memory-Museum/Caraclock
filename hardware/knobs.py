#source: https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15 

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
#from gpiozero import Button 

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)


print("{:>5}\t{:>5}".format('raw', 'v'))

while True:

    print("__________________")

    print("Knobs:")
    print("{:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage))
    print("{:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
    print("{:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
    print("____________________")
    time.sleep(0.5)
