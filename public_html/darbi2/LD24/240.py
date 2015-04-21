# -*- coding: utf-8 -*-
# Fails: 240.py
# Darba autors: Artis Erglis
# Aplieciibas numurs: 141REB143
# Datums: 04.03.2015

from Tkinter import *
w = Tk()
w.title('Mana forma')
uzr01 = Label(w,text='RTU Elektronikas un telekomunikaaciju fakultaate',
bg="#28c", fg="red",
font="Time 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=60)
w.geometry('550x200')

w.mainloop()
