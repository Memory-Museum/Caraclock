from gpiozero import Button
from time import sleep

button1 = Button(5)  # theactual GPIO number
button2 = Button(6)  

def button_pressed():
    print("A button was pressed!")

while True:
    if button1.is_pressed and button2.is_pressed:
        print("Both buttons are pressed      ", end="\r")
    elif button1.is_pressed:
        print("Button 1 is pressed          ", end="\r")
    elif button2.is_pressed:
        print("Button 2 is pressed          ", end="\r")
    else:
        print("No button is pressed         ", end="\r")
    
    sleep(0.1) 
