from tkinter import *

window = Tk()
window.configure(bg="#333333")
window.title("Calculator")
window.geometry("200x186")

expresion = StringVar()

def press(num):
    expresion.set(expresion.get() + str(num))
    #print(expresion.get())
  
def equalpress():
    try:
        total = str(eval(expresion.get()))
        expresion.set(total)
    except:
        expresion.set("error")

def clear():
    expresion.set("")

expresion_entry = Entry(window, textvariable=expresion)
expresion_entry.grid(row=0, columnspan=4, sticky="nswe")

btn7 = Button(window, text=" 7 ", foreground="#fff", background="#666", command=lambda:press(7))
btn7.grid(row=1, column=0, sticky="nswe")

btn8 = Button(window, text=" 8 ", foreground="#fff", background="#666", command=lambda:press(8))
btn8.grid(row=1, column=1, sticky="nswe")

btn9 = Button(window, text=" 9 ", foreground="#fff", background="#666", command=lambda:press(9))
btn9.grid(row=1, column=2, sticky="nswe")

btn4 = Button(window, text=" 4 ", foreground="#fff", background="#666", command=lambda:press(4))
btn4.grid(row=2, column=0, sticky="nswe")

btn5 = Button(window, text=" 5 ", foreground="#fff", background="#666", command=lambda:press(5))
btn5.grid(row=2, column=1, sticky="nswe")

btn6 = Button(window, text=" 6 ", foreground="#fff", background="#666", command=lambda:press(6))
btn6.grid(row=2, column=2, sticky="nswe")

btn1 = Button(window, text=" 1 ", foreground="#fff", background="#666", command=lambda:press(1))
btn1.grid(row=3, column=0, sticky="nswe")

btn2 = Button(window, text=" 2 ", foreground="#fff", background="#666", command=lambda:press(2))
btn2.grid(row=3, column=1, sticky="nswe")

btn3 = Button(window, text=" 3 ", foreground="#fff", background="#666", command=lambda:press(3))
btn3.grid(row=3, column=2, sticky="nswe")

btn0 = Button(window, text=" 0 ", foreground="#fff", background="#666", command=lambda:press(0))
btn0.grid(row=4, column=0, sticky="nswe", columnspan=2)

btn_dec = Button(window, text=" . ", foreground="#fff", background="#666", command=lambda:press('.'))
btn_dec.grid(row=4, column=2, sticky="nswe")

plus = Button(window, text=" + ", fg="#fff", bg="#fe9727", command=lambda:press('+'))
plus.grid(row=1, column=3, sticky="nswe")

minus = Button(window, text=" - ", fg="#fff", bg="#fe9727", command=lambda:press('-'))
minus.grid(row=2, column=3, sticky="nswe")

multi = Button(window, text=" * ", fg="#fff", bg="#fe9727", command=lambda:press('*'))
multi.grid(row=3, column=3, sticky="nswe")

divid = Button(window, text=" / ", fg="#fff", bg="#fe9727", command=lambda:press('/'))
divid.grid(row=4, column=3, sticky="nswe")

equal = Button(window, text=" = ", fg="#fff", bg="#fe9727", command=equalpress)
equal.grid(row=5, column=3, sticky="nswe")

clear = Button(window, text="clear", fg="#fff", bg="#999", command=clear)
clear.grid(row=5, column=2, sticky="nswe")




window.mainloop()