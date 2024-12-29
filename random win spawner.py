import random
from tkinter import *
import threading

# Initialize the root window
root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(True)
root.attributes("-topmost", True)

def place_windows():
    """Creates randomly placed windows on the screen."""
    while True:
        # Create a new window
        win = Toplevel(root)

        # Set the geometry of the window to random positions within the screen bounds
        win.geometry(f"300x60+{random.randint(0, root.winfo_screenwidth() - 300)}+{random.randint(0, root.winfo_screenheight() - 68)}")

        # Update the window to ensure it displays properly
        win.update()

# Run the window creation in a separate thread
thread = threading.Thread(target=place_windows, daemon=True)
thread.start()

# Start the Tkinter event loop
root.mainloop()
