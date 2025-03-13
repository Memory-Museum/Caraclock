import os
import sys
import time
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import QTimer

import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize the potentiometer (ADS1015)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
operation_knob = AnalogIn(ads, ADS.P0)  # Read voltage from potentiometer
max_vol = 3.294  # Maximum voltage

# Load images from folder
photos_path = '/home/caraclock/Desktop/Soon-Photos-Caraclock'
dir_list = sorted(os.listdir(photos_path))  # Ensure sorted order for consistent indexing
image_paths = [os.path.join(photos_path, img) for img in dir_list if img.endswith(('.png', '.jpg', '.jpeg'))]

# Calculate voltage-to-image mapping
num_images = len(image_paths)
rate_per_picture = max_vol / num_images  # Voltage step per image

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Soon's Caraclock")
        
        self.label = QLabel(self)
        self.setCentralWidget(self.label)

        # Start timer to periodically check the potentiometer value
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_image)
        self.timer.start(100)  # Update every 100ms

        self.update_image()  # Show initial image

    def update_image(self):
        """Read potentiometer value and update image accordingly."""
        voltage = operation_knob.voltage
        image_index = min(int(voltage / rate_per_picture), num_images - 1)  # Ensure valid index
        
        pixmap = QPixmap(image_paths[image_index])
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
