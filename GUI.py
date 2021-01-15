import tkinter as tk
from tkinter import Tk, Label, Button, Entry
from boards import board_states
import numpy as np
from SudGame import possible
# tk._test()


grid = board_states[0]
print(np.matrix(grid))
window = tk.Tk()
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black", # Set the background color to black
    width = 15,
    height = 15
)
label.pack()
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
entry = tk.Entry()
entry.pack()

name = entry.get()
print(name)
# run Tkinter event loop
window.mainloop()

class SudokGUI:
    def __init__(self):
        pass
