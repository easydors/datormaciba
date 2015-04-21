# -*- coding: utf-8 -*-
# Fails: 243.py
# Autors: Artis Erglis
# Apliecibas numurs: 141REB143
# Datums: 04.03.2015

from Tkinter import *
import time
import urllib
import base64

w=Tk(); f=Frame(); f.pack()
time_var=StringVar()
time_labelis=Label(f, textvariable=time_var, font="Courier 60",
bg="#C9C9C9", fg="#FFFF53")
time_labelis.pack()

#Attela ievietosana izmantojot label
URL = "http://dizains.rtu.lv/ImagesPub/RTU_Logo.gif"
a = urllib.urlopen(URL)
raw_input = a.read()
a.close()
b = base64.encodestring(raw_input)
image = PhotoImage(data=b)
label = Label(image=image)
label.place(x=520, y= 280)

def mirgot():
    t = time.localtime(time.time())
    if t[5] % 2:                            #mirgoshanas efekts
        fmt="%H:%M:%S"
    else:
        fmt="%H %M %S"
    time_var.set(time.strftime(fmt, t))
    time_labelis.after(500, mirgot)         #gaidam 0.5 sekundes
    
time_labelis.after(500, mirgot)

w.title('Stundu saraksts')
uzr01 = Label(w,text='RTU Elektronikas un telekomunikāciju fakultāte',
bg="#C9C9C9", fg="#51C192",
font="Time 13 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=85)

uzr01 = Label(w,text='2015.gads',
bg="#C9C9C9", fg="#06D07C",
font="Time 13 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=65)

uzr01 = Label(w,text='Artis Ērglis 141REB143 REB C04',
bg="#C9C9C9", fg="#0FC076",
font="Time 13 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=105)

uzr01 = Label(w,text='Pirmdiena:',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=40, y=145)

uzr01 = Label(w,text='8.15 - 9.50 Elektronikas teoretiskie pamati',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=145, y=145)

uzr01 = Label(w,text='10.15 - 11.50 Elektronikas teorētiskie pamati',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=145, y=170)

uzr01 = Label(w,text='14.30 - 16.05 Elektroindzenieru matematiska datorrealizacija',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr01.pack(side=LEFT)
uzr01.place(x=145, y=195)

uzr02 = Label(w,text='Otrdiena:',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr02.pack(side=LEFT)
uzr02.place(x=40, y=225)

uzr02 = Label(w,text='8.15 - 9.50 Matematika',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr02.pack(side=LEFT)
uzr02.place(x=145, y=225)

uzr02 = Label(w,text='10.15 - 11.50 Matematika',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr02.pack(side=LEFT)
uzr02.place(x=145, y=250)

uzr02 = Label(w,text='12.30 - 14.05 Elektronikas teoretiskie pamati',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr02.pack(side=LEFT)
uzr02.place(x=145, y=275)

uzr03 = Label(w,text='Tresdiena:',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr03.pack(side=LEFT)
uzr03.place(x=40, y=305)

uzr03 = Label(w,text='8.15 - 9.50 Datormācība',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr03.pack(side=LEFT)
uzr03.place(x=145, y=305)

uzr03 = Label(w,text='10.15 - 11.50 Elektronikas teorētiskie pamati',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr03.pack(side=LEFT)
uzr03.place(x=145, y=330)

uzr03 = Label(w,text='12.30 - 14.05 Fizika',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr03.pack(side=LEFT)
uzr03.place(x=145, y=355)

uzr03 = Label(w,text='14.30 - 16.05 Datormācība',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr03.pack(side=LEFT)
uzr03.place(x=145, y=380)

uzr04 = Label(w,text='Ceturdiena:',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr04.pack(side=LEFT)
uzr04.place(x=40, y=410)

uzr04 = Label(w,text='8.15 - 9.50 Elektroindzenieru matematiska datorrealizacija',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr04.pack(side=LEFT)
uzr04.place(x=145, y=410)

uzr04 = Label(w,text='10.15 - 11.50 Elektriba un magnetisms',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr04.pack(side=LEFT)
uzr04.place(x=145, y=435)

uzr04 = Label(w,text='12.30 - 14.05 Sports',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr04.pack(side=LEFT)
uzr04.place(x=145, y=460)

uzr04 = Label(w,text='14.30 - 16.05 Datormācība',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr04.pack(side=LEFT)
uzr04.place(x=145, y=485)

uzr05 = Label(w,text='Piektdiena:',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr05.pack(side=LEFT)
uzr05.place(x=40, y=515)

uzr05 = Label(w,text='8.15 - 9.50 Anglu valoda',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr05.pack(side=LEFT)
uzr05.place(x=145, y=515)

uzr05 = Label(w,text='10.15 - 11.50 Matematika',
bg="#72A5F2", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr05.pack(side=LEFT)
uzr05.place(x=145, y=540)

uzr05 = Label(w,text='12.30 - 14.05 Elektriba un magnetisms',
bg="#2F74DC", fg="#FBFF61",
font="Helvetica 12 bold italic" )
uzr05.pack(side=LEFT)
uzr05.place(x=145, y=565)


w.geometry('1000x630')

w.mainloop()
