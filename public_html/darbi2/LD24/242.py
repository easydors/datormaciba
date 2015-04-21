# -*- coding: utf-8 -*-
# Fails: 242.py
# Autors: Artis Erglis
# Apliecibas numurs: 141REB143
# Datums: 04.03.2015

from Tkinter import *
import time

def mirgot():
    t = time.localtime(time.time())
    if t[5] % 2:                            #mirgoshanas efekts
        fmt="%H:%M:%S"
    else:
        fmt="%H %M %S"
    time_var.set(time.strftime(fmt, t))
    time_labelis.after(500, mirgot)         #gaidam 0.5 sekundes
    
w=Tk(); f=Frame(); f.pack()
time_var=StringVar()
time_labelis=Label(f, textvariable=time_var, font="Courier 60",
bg="#2A2A08", fg="#FFFF53")
time_labelis.pack()

time_labelis.after(500, mirgot)
w.mainloop()
