from tkinter import *
import random

window = Tk()
window.title('Тестовое окно')
window.geometry('800x800')
window.resizable(width=False, height=False)
window.geometry(f'+{(window.winfo_screenwidth()-800)//2}+{(window.winfo_screenheight()-800)//2}')
window.config(bg = 'black')


def add():
	ent.insert(END, 'hi')


def delettt():
	ent.delete(0, END)


def get():
	label1['text'] = ent.get()


def random_color():
	colors = ['black', 'yellow', 'red', 'green', 'purple']
	print(random.choice(colors))

btn = Button(window,
			text='цветOK',
			command=random_color,
			font=('Comic Sans MS', 30),
			bg='red',
			fg='blue',
			activebackground='blue',
			activeforeground='red',
			padx=100
			)


btn.pack(side='bottom', anchor='center', pady=100)


label = Label(window,
			  text='Разные цветОчКи',
			  font=('Comic Sans MS', 40),
			  bg='red',
			  fg='blue'
			  )


label.pack(side='top', anchor='center')


img = PhotoImage(file=r'c:\Users\1\Downloads\x2431275-1770566753.png')
i_img = Label(window,
			  image=img,
			  bg='black'
			  )
i_img.pack(side='left', padx=100)


ent = Entry(window, show='*')
ent.pack(pady=10)

btn1 = Button(window, text='добавить', font=('Comic Sans MS', 15), bg='brown', command=add)
btn1.pack()

btn2 = Button(window, text='удалить', font=('Comic Sans MS', 15), bg='brown', command=delettt)
btn2.pack()

btn3 = Button(window, text='вывести', font=('Comic Sans MS', 15), bg='brown', command=get)
btn3.pack()

label1 = Label(window, bg='black', fg='white')
label1.pack()

label2 = Label(window, text='привет', bg='white', fg='red')
label2.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.2, relheight=0.2)

canvas = Canvas(window, bg='white', width=800, height=600)


canvas.create_rectangle(150, 150, 200, 200, fill='lime', width=10, outline='brown')
canvas.create_line(100, 100, 210, 210, fill='yellow')
canvas.create_oval(50, 80, 100, 100, fill='green', outline='brown')

canvas.create_polygon(110, 110, 110, 120, 200, 120)

canvas.pack()
window.mainloop()