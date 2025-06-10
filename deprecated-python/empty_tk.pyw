#!/usr/bin/python

import Tkinter

root = Tkinter.Tk()
root.title('Testing')
entry = Tkinter.Entry(root)
entry.pack(side=Tkinter.LEFT)
Button = Tkinter.Button(root, text='Submit')
Button.pack()
root.mainloop()
