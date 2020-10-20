import tkinter as tk
from tkinter import *
from tkinter import ttk

win = tk.Tk()
win.title("Aviato")

menubar = Menu(win)

# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_command(label='Exit', command=win.destroy)

#frame for buttons and slider
bframe=Frame(win)
bframe.pack(side=BOTTOM,fill=Y,pady=10)

#frame for the image
imgframe=Frame(win)
imgframe.pack(side=TOP,fill=Y)

#frame for slider
sliderframe=Frame(bframe)
sliderframe.pack(side=TOP)

#frame for Buttons
butframe=Frame(bframe)
butframe.pack(side=BOTTOM)


#buttons in the button frame
ttk.Button(butframe, text="crop").grid(column=0, row=0)
ttk.Button(butframe, text="filters").grid(column=1, row=0)
ttk.Button(butframe, text="brightness").grid(column=2, row=0)
ttk.Button(butframe, text="sharpen").grid(column=3, row=0)

#Label which will be replaced by image
label=ttk.Label(imgframe,text="Image will come here",background="white").pack(fill=BOTH)

#slider
slider=ttk.Scale(sliderframe,from_=0,to=100).grid(row=0,column=4)


#======================
# Start GUI
#======================

win.config(menu = menubar)
win.mainloop()