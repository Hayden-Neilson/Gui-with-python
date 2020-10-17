from tkinter import *

window = Tk()


def km_to_miles():
    print('success ')


but1 = Button(window, text="Execute", command=km_to_miles)
but1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

txt1 = Text(window, height=1, width=20)
txt1.grid(row=0, column=2)
window.mainloop()
