#Fails 252.py
#Autors Artis Erglis

import Tkinter as tk

root=tk.Tk()
root.title("Televizijas krasu tabula")
w=tk.Canvas(root, width=800, height=450, bg="#abc")
w.pack()
linija=w.create_line(50,450,50,0, width=100, fill="#FFFFFF")
linija=w.create_line(150,450,150,0, width=100, fill="#FFF700")
linija=w.create_line(250,450,250,0, width=100, fill="cyan")
linija=w.create_line(350,450,350,0, width=100, fill="green")
linija=w.create_line(450,450,450,0, width=100, fill="#800080")
linija=w.create_line(550,450,550,0, width=100, fill="red")
linija=w.create_line(650,450,650,0, width=100, fill="blue")
linija=w.create_line(750,450,750,0, width=100, fill="black")

t2=w.create_text(120,20, text="Artis Erglis kraasu tabula", font="Helvetica 15 normal", fill="#403C39")

root.mainloop()
