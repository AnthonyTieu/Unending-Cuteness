from pynput.mouse import Button, Controller, Listener
import pyglet
import keyboard
import sys
import os
import tkinter as tk
from pathlib import Path

mouse = Controller()
deactivation_key = '+'
root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

mid_screen_x = (screen_width)/2
mid_screen_y = (screen_height)/2

def on_click(x, y, button, pressed):

    if pressed:
        mouse.position = (mid_screen_x, mid_screen_y)
            
while True:
    
    if len(keyboard.read_key()) > 0:
        while True:
            listener = Listener(on_click=on_click)
            listener.start()

            ag_file = pyglet.image.load_animation(Path('Baby Yoda.gif'))
            sprite = pyglet.sprite.Sprite(ag_file)
            win = pyglet.window.Window(width=sprite.width, height=sprite.height)
                    
            @win.event
        
            def on_draw():
                win.clear()
                sprite.draw()

                if keyboard.is_pressed(deactivation_key):
                    listener.stop()
                    sys.exit()

            pyglet.app.run()
