from tkinter import *
from tkinter import ttk
root_file = Tk()
frm = ttk.Frame(root_file,padding=15)
frm.grid()
ttk.Label(frm,text="Hello World").grid(column=0,row=0)
ttk.Button(frm,text="Click Me").grid(column=1,row=0)

ttk.PanedWindow().grid(column=1,row=2)

root_file.mainloop()