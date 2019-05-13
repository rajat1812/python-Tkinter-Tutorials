from tkinter import *


root = Tk()

root.geometry("600x600")

root.configure(background='black')
can_widget = Canvas(root,width=300,height=300)
can_widget.pack()

# the line goes from the point x1,y1 to x2,y2
can_widget.create_line(0,0,300,200, fill= "red")
can_widget.create_line(0,200,300,0, fill= "red")

#  to create a rectangle specify coordinates in this order
can_widget.create_rectangle(3,10 ,300,100)

# create text
can_widget.create_text(200,200,text="python",fill="brown")

# create oval
can_widget.create_oval(4,12,299,98,fill="blue")


root.mainloop()