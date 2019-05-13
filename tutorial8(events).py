from tkinter import *

def rajat(event):
    print(event.x,event.y)

root = Tk()

root.geometry("600x334")

widget = Button(root,text="Clicked me please")
widget.pack()
widget.bind('<Button-1>',rajat)
widget.bind('<Double-1>',quit)

root.mainloop()