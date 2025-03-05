
from time import sleep
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gpiozero import Button 
from gpiozero import LED


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)

button1 = Button(5)  # theactual GPIO number
button2 = Button(6)


reedswitch1 = Button(13)  # theactual GPIO number
reedswitch2 = Button(19) 

led = LED(26)
print("{:>5}\t{:>5}".format('raw', 'v'))


while True:
    if button1.is_pressed and button2.is_pressed:
        print("Both buttons are pressed      ", end="\r")
    elif button1.is_pressed:
        print("Button 1 is pressed          ", end="\r")
    elif button2.is_pressed:
        print("Button 2 is pressed          ", end="\r")
    else:
        print("No button is pressed         ", end="\r")
    
    #led
    sleep(0.1) 
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    
   

    print("__________________")

    print("Knobs:")
    print("{:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage))
    print("{:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
    print("{:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
    print("____________________")
    time.sleep(0.5)
    
    print("Reed Switch")
    
    if reedswitch1.is_pressed:
        print("magnet 1detected     ", end="\r")
    elif reedswitch2.is_pressed:
        print ("magnet 2 detected")
		
    else:
        print("both released         ", end="\r")
    
    sleep(0.1) 

