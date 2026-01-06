import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)

# Function to update time
def update_time():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)  # update every 1 second

# Clock label
label = tk.Label(
    root,
    font=("Arial", 40),
    background="black",
    foreground="cyan"
)
label.pack(expand=True)

# Start the clock
update_time()

# Run GUI
root.mainloop()
