from tkinter import *


# it creates basic gui (it consist of all basic gui components)
root = Tk()

# width x height
root.geometry("444x234")

# width,height
root.minsize(100,100)
root.maxsize(900,900)

# we have to pack for displaying label
lbl = Label(text = "rajat is a nice guy")
lbl.pack()



# it keeps u on the main window & remember all the logics u have made
root.mainloop()

