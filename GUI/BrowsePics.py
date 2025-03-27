import os
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# === Initialize I2C and ADC ===
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
operation_knob = AnalogIn(ads, ADS.P0)

# Potentiometer settings
VOLTAGE_MIN, VOLTAGE_MAX = 0.0, 4.1
DEAD_ZONE = 0.05  # Ignore tiny fluctuations when at rest
last_voltage = 0

# === Load Images ===
photos_path = "/home/caraclock/Desktop/Soon-Photos-Caraclock"
image_files = sorted([img for img in os.listdir(photos_path) if img.endswith(('.png', '.jpg', '.jpeg'))])
image_paths = [os.path.join(photos_path, img) for img in image_files]
num_images = len(image_paths)

if not image_paths:
    print("No images found in folder!")
    exit(1)

# === Tkinter Setup ===
root = tk.Tk()
root.title("Clock & Image Viewer")
root.geometry("800x600")

# Canvas for both clock and images
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# === Digital Clock Class ===
class DigitalClock:
    def __init__(self, canvas):
        self.canvas = canvas
        self.running = True  # Track if clock is displayed
        self.update_clock()

    def update_clock(self):
        if not self.running:
            return  # Stop updating if clock is hidden

        self.canvas.delete("all")  # Clear old content
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        
        # Display time & date
        current_time = datetime.now().strftime("%H:%M:%S")
        today_date = datetime.now().strftime("%Y-%m-%d")

        self.canvas.create_text(width // 2, height // 2, text=current_time, font=("Arial", 70, "bold"), fill="black")
        self.canvas.create_text(width // 2, height // 2 + 50, text=today_date, font=("Arial", 20), fill="black")

        self.canvas.after(1000, self.update_clock)  # Refresh every second

# === Image Viewer Class ===
class ImageViewer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.index = 0
        self.photo = None
        self.running = False  # Track if images are displayed

    def show_image(self, index):
        self.canvas.delete("all")  # Clear canvas

        # Load and display the new image
        img = Image.open(image_paths[index])
        img = img.resize((600, 400), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)

        self.canvas.create_image(400, 300, image=self.photo)  # Centered
        self.index = index

# === Initialize Views ===
clock = DigitalClock(canvas)
image_viewer = ImageViewer(canvas)

# === Function to Switch Views Based on Potentiometer ===
def check_potentiometer():
    global last_voltage
    voltage = operation_knob.voltage  

    if abs(voltage - last_voltage) > DEAD_ZONE:  # Potentiometer moved
        if clock.running:  
            # Hide clock and switch to image browsing
            clock.running = False
            image_viewer.running = True
            show_images()
        else:
            # Adjust image index based on voltage
            index = int((voltage - VOLTAGE_MIN) / (VOLTAGE_MAX - VOLTAGE_MIN) * (num_images - 1))
            index = max(0, min(index, num_images - 1))  
            image_viewer.show_image(index)

        last_voltage = voltage

    root.after(300, check_potentiometer)  # Check every 300ms

def show_images():
    image_viewer.running = True
    image_viewer.show_image(0)

# Start monitoring potentiometer
root.after(300, check_potentiometer)

# Run Tkinter main loop
root.mainloop()
