from gpiozero import Button
from time import sleep

reedswitch1 = Button(13)  # theactual GPIO number
reedswitch2 = Button(19)
 
while True:
    if reedswitch1.is_pressed:
        print("magnet 1detected     ", end="\r")
    elif reedswitch2.is_pressed:
	print ("magnet 2 detected")
		
    else:
        print("boh released         ", end="\r")
    
    sleep(0.1) 
