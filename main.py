# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter.ttk import *
from tkinter import Menu
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="Once upon a time, in a galaxy far far away....")

# Place the label in the window at 0, 0
lbl.grid(column=0, row=5)
txt = Entry(window,width=40)
 
txt.grid(column=1, row=0)
firstLabel = Label(window, text="Hello", font=("Arial Bold", 50))
firstLabel.grid(column=0, row=0) 

 
txt.grid(column=1, row=0)

cnk = Checkbutton(window, text='Choose')
window.title("Welcome to my hour and a half")
window.geometry('540x300')
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='pick', var=chk_state)
chk.grid(column=2, row=5)



menu = Menu(window)

window = Tk()
window.title("Wndo #2")

new_item = Menu(menu)
new_item.add_command(label='New boy')
menu.add_command(label='File')
window.config(menu=menu)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

window.mainloop()     # Keep the window open







