from tkinter import *

window = Tk()
window.configure(bg="#333333")
window.title("Calculator")
window.geometry("386x186")

expresion = StringVar()
expresion_entry = Entry(window, textvariable=expresion)
expresion_entry.grid(row=0, columnspan=4, sticky="nswe")



window.mainloop()