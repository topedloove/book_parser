from tkinter import *
from tkinter import messagebox
import random


def no():
	messagebox.showinfo('', 'Очевидно же')
	quit()


def motionMouse(event):
	btn1.place(x=random.randint(30, 400), y=random.randint(30, 738))



window = Tk()
window.title('Joke')
window.geometry('432x768')
window.geometry(f'+{(window.winfo_screenwidth()-432)//2}+{(window.winfo_screenheight()-768)//2}')
window.resizable(0, 0)
window['bg'] = 'white'

window.image = PhotoImage(file=r'c:\Users\1\Downloads\convertio.in_S-alnQsDlrn22VJfxgeeMIS7U_6VTMB5oAqkfj1o8lJ6hk862YJgjwmiDm7nAjPGtimRJvyMrRuPa9m-VDeWtd_B.png')
bg_image = Label(window, image=window.image)
bg_image.grid(row=0, column=0)

label = Label(window, text='Бросит ли "Жека французский багет" пить ?', font=('Comic Sans MS', 14), bg='gray')
label.place(relx=0.5, y=200, anchor='center')

btn1 = Button(window, text='Да', font=('Comic Sans MS', 16), bg='gray', command=motionMouse)
btn1.place(x=120, y=270, anchor='center')
btn1.bind('<Enter>', motionMouse)

btn2 = Button(window, text='Нет', font=('Comic Sans MS', 16), bg='gray', command=no)
btn2.place(x=320, y=270, anchor='center')

window.mainloop()