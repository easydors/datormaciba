# Fails: 261.py
# Autors: Artis Erglis
# Apliecibas numurs: 141REB143

import Tkinter as tk
import time
root=tk.Tk()
root.title("Mana Tafele ar dinamisku tekstu")

w=tk.Canvas(root, width=600, height=400, bg="#456", relief="sunken", border=10)
w.pack()

t=w.create_text(50, 100, text="2 + 2 = \n4", font="Courier 40 bold", fill="#ffc", anchor="nw")

def funA():
    k=16
    s=e2.get()
    for i in range(k):
        print s[:i]
        w.itemconfig(t, text=s[:i])
        w.update()
        time.sleep(0.5)

def funB():
    k=16
    s=e2.get()
    for i in range(k):
        print s[i:]
        w.itemconfig(t, text=s[i:])
        w.update()
        time.sleep(0.5)

def funC():
    w.move(t, 10, 0)

v=tk.StringVar()
v.set("0123456789ABCDF")

e2=tk.Entry(root, textvariable=v)
e2.pack()

b=tk.Button(root, text="Spied", command=funA)
b.pack()

b=tk.Button(root, text="Dzest", command=funB)
b.pack()

b=tk.Button(root, text="Move", command=funC)
b.pack()

root.mainloop()
