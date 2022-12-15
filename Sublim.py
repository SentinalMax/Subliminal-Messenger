import tkinter as tk
import time
import random
from random import choice
from tkinter import *
import requests

# VARIABLES TO CHANGE
wait_time=100 # In milliseconds
color='black' # for white -> 'white'
font=("Helvetica", 20) # Font & Size
quotes=('Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.', 
'The will to win, the desire to succeed, the urge to reach your full potential... these are the keys that will unlock the door to personal excellence.',
'Always do your best. What you plant now, you will harvest later.',
'In order to succeed, we must first believe that we can.',
'You have to learn the rules of the game. And then you have to play better than anyone else.',
'A creative being is motivated by the desire to achieve, not by the desire to beat others.')

# UI STUFF

root = tk.Tk()
# Hide the root window drag bar and close button
root.overrideredirect(True)
root.wm_state("normal")
# Make the root window always on top
root.wm_attributes("-alpha", True) #alpha works / topmost would be ideal
# Turn off the window shadow
root.wm_attributes("-transparent", True)
# Set the root window background color to a transparent color
root.config(bg='systemTransparent')

def do_stuff():
    
    s = choice(quotes)
    l.config(text=s, fg=color)
    root.after(wait_time, do_stuff)
    root.geometry("{0}x{1}+0+0".format(1000, 350)) #x, y
    l.place(x=random.randint(0,3000), y=random.randint(0,3000))


#root.bind("<Button-1>", lambda evt: root.destroy()) #click to destroy

l = tk.Label(text='', font=font) #font & text size
l.pack(expand=True)
l.config(bg='systemTransparent')
l.pack()

do_stuff()
root.mainloop()
