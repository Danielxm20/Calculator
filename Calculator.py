from tkinter import *

window = Tk()
window.configure(bg="#333333")
window.title("Calculator")
window.geometry("386x186")

expresion = StringVar()
expresion_entry = Entry(window, textvariable=expresion)
expresion_entry.grid(row=0, columnspan=4, sticky="nswe")

btn7 = Button(window, text=" 7 ", foreground="#fff", background="#666")
btn7.grid(row=1, column=0, sticky="nswe")

btn8 = Button(window, text=" 8 ", foreground="#fff", background="#666")
btn8.grid(row=1, column=1, sticky="nswe")

btn9 = Button(window, text=" 9 ", foreground="#fff", background="#666")
btn9.grid(row=1, column=2, sticky="nswe")

btn4 = Button(window, text=" 4 ", foreground="#fff", background="#666")
btn4.grid(row=2, column=0, sticky="nswe")

btn5 = Button(window, text=" 5 ", foreground="#fff", background="#666")
btn5.grid(row=2, column=1, sticky="nswe")

btn6 = Button(window, text=" 6 ", foreground="#fff", background="#666")
btn6.grid(row=2, column=2, sticky="nswe")

btn1 = Button(window, text=" 1 ", foreground="#fff", background="#666")
btn1.grid(row=3, column=0, sticky="nswe")

btn2 = Button(window, text=" 2 ", foreground="#fff", background="#666")
btn2.grid(row=3, column=1, sticky="nswe")

btn3 = Button(window, text=" 3 ", foreground="#fff", background="#666")
btn3.grid(row=3, column=2, sticky="nswe")

btn0 = Button(window, text=" 0 ", foreground="#fff", background="#666")
btn0.grid(row=4, column=0, sticky="nswe", columnspan=2)



window.mainloop()