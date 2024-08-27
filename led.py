import serial
import tkinter as tk
from tkinter import ttk, colorchooser
from ttkthemes import ThemedTk

# Arduino settings
arduino_port = 'COM13'  # Change to the appropriate port
baud_rate = 115200
ser = serial.Serial(arduino_port, baud_rate)

def send_color_to_arduino(color):
    """Send the selected color to Arduino."""
    red, green, blue = color
    ser.write(f'{red},{green},{blue}\n'.encode())
    print(f"Sending {color} to Arduino")

def on_color_button_click():
    """Handle the color selection button click."""
    color_code = colorchooser.askcolor(title="Choose a color")
    if color_code:
        rgb = tuple(int(c) for c in color_code[0])
        send_color_to_arduino(rgb)

def on_scale_change(event=None):
    """Handle the change in color sliders."""
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    send_color_to_arduino((red, green, blue))

# Create GUI
root = ThemedTk(theme="arc")
root.title("Choose LED Color")

# Title label
label = ttk.Label(root, text="Choose a color for the LED", font=("Helvetica", 16))
label.pack(pady=20)

# Color selection button
color_button = ttk.Button(root, text="Choose Color From Pallete", command=on_color_button_click)
color_button.pack(pady=20)

# Button to turn off the LED
off_button = ttk.Button(root, text="Turn Off LED", command=lambda: send_color_to_arduino((0, 0, 0)))
off_button.pack(pady=20)

# Sliders for real-time color selection
red_scale = ttk.Scale(root, from_=0, to=255, orient='horizontal', command=on_scale_change)
red_scale.set(0)
red_scale.pack(fill='x', padx=20, pady=5)

green_scale = ttk.Scale(root, from_=0, to=255, orient='horizontal', command=on_scale_change)
green_scale.set(0)
green_scale.pack(fill='x', padx=20, pady=5)

blue_scale = ttk.Scale(root, from_=0, to=255, orient='horizontal', command=on_scale_change)
blue_scale.set(0)
blue_scale.pack(fill='x', padx=20, pady=5)

try:
    root.mainloop()
finally:
    ser.close()