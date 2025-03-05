from gpiozero import LED
from time import sleep
# from time import sleep
led = LED(26)

while True:

 #button = Button(26)
   
    led.on()
    sleep(1)
    led.off()
    sleep(1)

#button 

