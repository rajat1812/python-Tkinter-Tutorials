from tkinter import *

def myfunc():
    print("menu")

root = Tk()

root.geometry("600x334")
root.title("MENU")

main_menu = Menu(root)

m1 = Menu(main_menu, tearoff=0)
m1.add_command(label="save as", command=myfunc)
m1.add_command(label="Exit", command=quit)
m1.add_command(label="power", command=quit)
m1.add_command(label="new", command=quit)
m1.add_command(label="save", command=quit)


root.config(menu=main_menu)

main_menu.add_cascade(label= "File", menu=m1)



root.mainloop()