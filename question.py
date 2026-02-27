from tkinter import *

window = Tk()
window.title('?')
window.geometry('740x493')
window.resizable(False, False)
window.geometry(
    f'+{(window.winfo_screenwidth()-740)//2}+{(window.winfo_screenheight()-493)//2}')
window.config(bg='black')


def get():
    label.configure(text='hello')


def get2():
    label.configure(text='bye')


def get3():
    label.configure(text='good')


def get4():
    label.configure(text='fuck you')


def get5():
    label.configure(text='nothing')


def get_text():
    label_text['text'] = ent.get()


def clear_text():
    label_text.configure(text='')
    ent.delete(0, END)


def clear():
    label.configure(text='')


label = Label(window, font=('Comic Sans MS', 20), bg='black', fg='white')
label.pack(pady=125)

btn1 = Button(window, font=('Comic Sans MS', 20), text='?',
              command=get, bg='black', fg='white')
btn1.place(x=150, y=250)

btn2 = Button(window, font=('Comic Sans MS', 20), text='?',
              command=get2, bg='black', fg='white')
btn2.place(x=250, y=250)

btn3 = Button(window, font=('Comic Sans MS', 20), text='?',
              command=get3, bg='black', fg='white')
btn3.place(x=350, y=250)

btn4 = Button(window, font=('Comic Sans MS', 20), text='?',
              command=get4, bg='black', fg='white')
btn4.place(x=450, y=250)

btn5 = Button(window, font=('Comic Sans MS', 20), text='?',
              command=get5, bg='black', fg='white')
btn5.place(x=550, y=250)

clear_btn = Button(window, text='clear', font=(
    'Comic Sans MS', 20), command=clear, bg='black', fg='white')
clear_btn.place(x=325, y=350)

ent = Entry(window, show='*')
ent.place(x=380, y=50, anchor='center')

btn_get = Button(window, bg='black', fg='white', text='Вывести',
                 font=('Comic Sans MS', 15), command=get_text)
btn_get.place(x=230, y=50, anchor='center')


label_text = Label(window, bg='black', fg='white', font=('Comic Sans MS', 20))
label_text.place(x=380, y=100, anchor='center')

btn_clear = Button(window, bg='black', fg='white', text='Очистить',
                   font=('Comic Sans MS', 15), command=clear_text)
btn_clear.place(x=120, y=50, anchor='center')


window.mainloop()
