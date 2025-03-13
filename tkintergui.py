import os
import tkinter as tk
from PIL import Image, ImageTk
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus and ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)

# Load images from folder
photos_path = "/home/caraclock/Desktop/Soon-Photos-Caraclock"
dir_list = sorted(os.listdir(photos_path))  
image_paths = [os.path.join(photos_path, img) for img in dir_list if img.endswith(('.png', '.jpg', '.jpeg'))]
num_images = len(image_paths)

if num_images == 0:
    print("No images found in the folder!")
    exit(1)  # Exit if no images are available

# ADC Setup
operation_knob = AnalogIn(ads, ADS.P0)
voltage_min, voltage_max = 0.0, 4.1  # Adjusted to match your potentiometer
dead_zone = 0.05  # Small threshold to ignore flickering around rest position

# Tkinter setup
root = tk.Tk()
root.title("Soon's Caraclock")

# Variables for tracking last image
last_index = -1  

# Function to update the displayed image
def update_image():
    global last_index

    # Read potentiometer voltage
    voltage = operation_knob.voltage  

    # Ignore small fluctuations when at rest
    if abs(voltage - last_index) < dead_zone and last_index != -1:
        root.after(300, update_image)  # Keep checking without updating image
        return

    # Map voltage to image index
    index = int((voltage - voltage_min) / (voltage_max - voltage_min) * (num_images - 1))
    index = max(0, min(index, num_images - 1))  # Ensure it's in range

    if index != last_index:  # Change only if a new image is selected
        last_index = index  

        # Load and display the new image
        img = Image.open(image_paths[index])
        img = img.resize((600, 400), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        label.config(image=img_tk)
        label.image = img_tk  # Keep reference

    root.after(300, update_image)  # Check every 300ms

# Initial image display
img = Image.open(image_paths[0])
img = img.resize((600, 400), Image.Resampling.LANCZOS)
img_tk = ImageTk.PhotoImage(img)

label = tk.Label(root, image=img_tk)
label.pack()
label.image = img_tk

# Start update loop
root.after(300, update_image)
root.mainloop()
