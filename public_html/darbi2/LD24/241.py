# -*- coding: utf-8 -*-
# Fails: 241.py
# Darba autors: Artis Erglis
# Aplieciibas numurs: 141REB143
# Datums: 04.03.2015

from Tkinter import *
w = Tk()
w.title('Stundu saraksts')
uzr01 = Label(w,text='RTU Elektronikas un telekomunikāciju fakultāte',
bg="#28c", fg="#51C192",
font="Time 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=60)

uzr01 = Label(w,text='2015.gads',
bg="#28c", fg="#06D07C",
font="Time 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=40)

uzr01 = Label(w,text='Artis Ērglis 141REB143 REB C04',
bg="#28c", fg="#0FC076",
font="Time 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=80)

uzr01 = Label(w,text='Stundu saraksts:',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=120)

uzr01 = Label(w,text='8.15 - 9.50 Datormācība',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=175, y=120)

uzr01 = Label(w,text='10.15 - 11.50 Elektronikas teorētiskie pamati',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=175, y=145)

uzr01 = Label(w,text='12.30 - 14.05 Fizika',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=175, y=170)

uzr01 = Label(w,text='14.30 - 16.05 Datormācība',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=175, y=195)

w.geometry('550x300')

w.mainloop()
