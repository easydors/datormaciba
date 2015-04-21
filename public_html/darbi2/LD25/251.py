#Fails 251.py
#Autors Artis Erglis

import Tkinter as tk

root=tk.Tk()
root.title("Mana Bilde")
w=tk.Canvas(root, width=600, height=400, bg="#abc")
w.pack()
linija=w.create_line(50,100,400,300, width=4, fill="#CB3E3E")
linija=w.create_line(70,300,350,200, width=1, fill="#987A7A")
linija=w.create_line(150,200,400,350, width=2, fill="#8684B4")

root.mainloop()
