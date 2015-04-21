#Autors: Artis Erglis
from Tkinter import *
import tkMessageBox

def calc():
    try:
        #saskaitisana
        if oper.get() == '+':
            try:
                value = float(num1.get()) + float(num2.get())
            except:
                tkMessageBox.showerror("Error!", 'Kaut kas nogaja greizi! Megini velreiz')

        str(num1)
        str(oper)
        str(num2)
        answer = Label(app, text='{0} {1} {2}='.format(num1.get(), oper.get(), num2.get()))
        answer.grid(row=3, column= 0, sticky=SW)
        answer2 = Label(app, text=value)
        answer2.grid(row=4, column= 0, sticky=S)
    except:
        tkMessageBox.showerror("Error!", 'Kaut kas nogaja greizi! Megini velreiz')


global value
value = 0

#Modificee logu
root = Tk()
root.title('Saskaitisanas kalkulators')
root.geometry('340x132')
root.resizable(0,0)


#izveido raami
app = Frame(root)
app.pack()

#loga atribuuti
label1 = Label(app, text='Ievadi skaitli 1 -->')
label1.grid(row=0, column=0, sticky=NW)

label2 = Label(app, text='Ievadi + ziimi -->')
label2.grid(row=1, column=0, sticky=W)

label3 = Label(app, text='Ievadi skaitli 2 -->')
label3.grid(row=2, column= 0, sticky=W)

global num1
num1 = StringVar()
number1 = Entry(app, textvariable= num1)
number1.grid(row=0, column=1, sticky=NE)

global oper
oper = StringVar()
operator = Entry(app, textvariable= oper)
operator.grid(row=1, column=1, sticky=E)

global num2
num2 = StringVar()
number2 = Entry(app, textvariable = num2)
number2.grid(row=2, column=1, sticky=E)

button = Button(app, text='Aprekinat', command = calc)
button.grid(row=3, column=1, sticky=SE)


root.mainloop()
