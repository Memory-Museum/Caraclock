import tkinter as tk
from datetime import datetime

class DigitalClock: 
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        
        self.canvas = tk.Canvas(self.root, width=800, height=300, bg="white")
        self.canvas.pack()
        
        self.draw_clock()

    def draw_clock(self): 
        self.canvas.delete("all")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        current_time = datetime.now().strftime("%H:%M:%S")
        today_date = datetime.now().strftime("%Y-%m-%d")
        # bible_verse = "John 3:16: For God so loved the world, that he gave his only Son,that whoever believes in him should not perish but have eternal life."

        self.canvas.create_text(width//2, height//2, text=current_time, font=("Arial", 70, "bold"), fill="black")

        # Display the date below the time
        self.canvas.create_text(width//2, height//2 + 50, text=today_date, font=("Arial", 20), fill="black")

        # self.canvas.create_text(width//2, height//2 -50, text=bible_verse, font=("Arial", 10, "bold"), fill="black")

        self.root.after(1000, self.draw_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
