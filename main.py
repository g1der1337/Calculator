from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("280x460")
window.config(bg="#788eac")

def fun(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.delete(0, END)
            entry.insert(END, "Ошибка")
    elif button_text == "ce":
        entry.delete(0, END)
    elif button_text == '%':
        entry.insert(END, '*0.01')
    # elif button_text == 'DEL':
    #     entry.delete(int(END)-1, END)
    else:
        entry.insert(END, button_text)


entry = Entry(width=20, font=("Arial", 18), justify='right')
entry.place(x=7, y= 20)


button_porzent = Button(text='%', command=lambda t='%': fun(t))
button_porzent.config(width=9, height= 3)
button_porzent.place(x= 0, y=150)

button_CE = Button(text='CE', command=lambda t='ce': fun(t))
button_CE.config(width=9, height= 3)
button_CE.place(x= 70, y=150)

button_brace_1 = Button(text='(', command=lambda t='(': fun(t))
button_brace_1.config(width=9, height= 3)
button_brace_1.place(x= 140, y=150)

button_brace_2 = Button(text=')', command=lambda t=')': fun(t))
button_brace_2.config(width=9, height= 3)
button_brace_2.place(x= 210, y=150)


button_root = Button(text='√', command=lambda t='**0.5': fun(t))
button_root.config(width=9, height= 3)
button_root.place(x= 0, y=200)

button_step = Button(text='**', command=lambda t='**': fun(t))
button_step.config(width=9, height= 3)
button_step.place(x= 70, y=200)

button_del = Button(text='del', command=lambda t='DEL': fun(t))
button_del.config(width=9, height= 3)
button_del.place(x= 140, y=200)

button_share = Button(text='/', command=lambda t='/': fun(t))
button_share.config(width=9, height= 3)
button_share.place(x= 210, y=200)


button_7 = Button(text='7', command=lambda t=7: fun(t))
button_7.config(width=9, height= 3)
button_7.place(x= 0, y=250)

button_8 = Button(text='8', command=lambda t=8: fun(t))
button_8.config(width=9, height= 3)
button_8.place(x= 70, y=250)

button_9 = Button(text='9', command=lambda t=9: fun(t))
button_9.config(width=9, height= 3)
button_9.place(x= 140, y=250)

button_multiply = Button(text='x', command=lambda t="*": fun(t))
button_multiply.config(width=9, height= 3)
button_multiply.place(x= 210, y=250)


button_4 = Button(text='4', command=lambda t=4: fun(t))
button_4.config(width=9, height= 3)
button_4.place(x= 0, y=300)

button_5 = Button(text='5', command=lambda t=5: fun(t))
button_5.config(width=9, height= 3)
button_5.place(x= 70, y=300)

button_6 = Button(text='6', command=lambda t=6: fun(t))
button_6.config(width=9, height= 3)
button_6.place(x= 140, y=300)

button_minus = Button(text='-', command=lambda t='-': fun(t))
button_minus.config(width=9, height= 3)
button_minus.place(x= 210, y=300)


button_1 = Button(text='1', command=lambda t=1: fun(t))
button_1.config(width=9, height= 3)
button_1.place(x= 0, y=350)

button_2 = Button(text='2', command=lambda t=2: fun(t))
button_2.config(width=9, height= 3)
button_2.place(x= 70, y=350)

button_3 = Button(text='3', command=lambda t=3: fun(t))
button_3.config(width=9, height= 3)
button_3.place(x= 140, y=350)

button_plus = Button(text='+', command=lambda t='+': fun(t))
button_plus.config(width=9, height= 3)
button_plus.place(x= 210, y=350)


button_00 = Button(text='')
button_00.config(width=9, height= 3)
button_00.place(x= 0, y=400)

button_0 = Button(text='0', command=lambda t=0: fun(t))
button_0.config(width=9, height= 3)
button_0.place(x= 70, y=400)

button_point = Button(text='.', command=lambda t='.': fun(t))
button_point.config(width=9, height= 3)
button_point.place(x= 140, y=400)

button_still = Button(text='=', command=lambda t='=': fun(t))
button_still.config(width=9, height= 3)
button_still.place(x= 210, y=400)




window.mainloop()