# -*- coding: utf-8 -*-
# Fails: 250.py
# Autors: Artis Erglis

import Tkinter as tk
root= tk.Tk();
root.title("Mana Tafele")

v = tk.StringVar()
v.set('Teksts uz taafeles')

def fun():
    e = tk.Entry(root, textvariable=v)
    e.pack()
    w.itemconfig(t, text=e.get())
    
b = tk.Button(root, text="Spied", command=fun)
b.pack()

w = tk.Canvas(root, width=600, height=400, \
              bg="#456", relief="sunken", border=10 )
w.pack()
t = w.create_text(50, 100, text="2 + 2 = 4",\
                  font="Courier 40 italic", fill ="#ffc", anchor='nw')
t2=w.create_text(600, 20, text="Artis Erglis",\
                  font="Courier 40 italic", fill ="#ffc", anchor='ne')
w.mainloop()
