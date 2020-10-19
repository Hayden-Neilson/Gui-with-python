from tkinter import *

window = Tk()


def kg_to_():
    Grams = float(el_value.get()) * 1000

    pound = float(el_value.get())*2.20462

    # Get user value from input box and multiply by 35.274 to get ounces
    ounce = float(el_value.get())*35.274

    # Deletes the content of the Text box from start to END
    txt1.delete("1.0", END)
    # Fill in the text box with the value of gram variable
    txt1.insert(END, Grams)
    txt2.delete("1.0", END)
    txt2.insert(END, pound)
    txt3.delete("1.0", END)
    txt3.insert(END, ounce)


but1 = Button(window, text="Convert", command=kg_to_)
but1.grid(row=0, column=0)

e1 = Label(window, text="Kg")
e1.grid(row=0, column=0)

el_value = StringVar()
entry1 = Entry(window, textvariable=el_value)
entry1.grid(row=0, column=2)

txt1 = Text(window, height=1, width=20)
txt1.grid(row=1, column=0)

txt2 = Text(window, height=1, width=20)
txt2.grid(row=1, column=1)

txt3 = Text(window, height=1, width=20)
txt3.grid(row=1, column=2)
window.mainloop()
