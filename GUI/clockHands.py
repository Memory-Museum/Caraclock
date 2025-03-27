# Tutorial source: https://www.youtube.com/watch?v=vs6uEFpStuY 
# edited by Belen
# we are not using this version anymore as we decided to use a digital clock


import tkinter as tk
from datetime import datetime
import math


class AnalogClockApp:

    def __init__(self,root):
        # Initialize the Tkinter window
        self.root = root
        self.root.title("Analog Clock")
        # Create a canvas for drawing the clock
        self.canvas = tk.Canvas(self.root, width=800,height=300,bg="white")
        self.canvas.pack()

        # Delay the initial drawing
        self.root.after(100, self.draw_clock)
    


    def draw_clock(self):

        self.canvas.delete("all")

        # Get the width and height of the canvas
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Calculate the center coordinates of the canvas
        center_x = width // 2
        center_y = height // 2

        # Get current time
        current_time = datetime.now()
        
        # Get today's date
        today_date = current_time.strftime("%Y-%m-%d")

        # Display the date at the bottom of the canvas
        self.canvas.create_text(center_x, height - 20, text=today_date, font=("Arial", 14), fill="black")

        # Calculate angles for clock hands
        hours_angle = math.radians(360 / 12 * (current_time.hour % 12 - 3))
        minutes_angle = math.radians(360 / 60 * (current_time.minute - 15))
        seconds_angle = math.radians(360 / 60 * (current_time.second - 15))

        # Clock hand lengths
        clock_radius = min(width, height) // 2 - 10
        hour_hand_length = clock_radius * 0.5   
        minute_hand_length = clock_radius * 0.7 
        second_hand_length = clock_radius * 0.9 

        # Calculate and draw hands
        hour_hand_x = center_x + int(hour_hand_length * math.cos(hours_angle)) 
        hour_hand_y = center_y + int(hour_hand_length * math.sin(hours_angle)) 
        self.canvas.create_line(center_x, center_y, hour_hand_x, hour_hand_y, fill="#333", width=6)   

        minute_hand_x = center_x + int(minute_hand_length * math.cos(minutes_angle)) 
        minute_hand_y = center_y + int(minute_hand_length * math.sin(minutes_angle)) 
        self.canvas.create_line(center_x, center_y, minute_hand_x, minute_hand_y, fill="#3498db", width=4)   

        second_hand_x = center_x + int(second_hand_length * math.cos(seconds_angle)) 
        second_hand_y = center_y + int(second_hand_length * math.sin(seconds_angle)) 
        self.canvas.create_line(center_x, center_y, second_hand_x, second_hand_y, fill="#e74c32", width=2)   

        # Update the clock every second
        self.root.after(1000, self.draw_clock)



if __name__ == "__main__":
    root = tk.Tk()
    app = AnalogClockApp(root)
    root.mainloop() 