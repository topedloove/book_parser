from tkinter import *

window = Tk()
window.title('Сlick counter')
window.geometry('200x200')
window.resizable(False, False)
window.geometry(f'+{(window.winfo_screenwidth()-200)//2}+{(window.winfo_screenheight()-200)//2}')
window.config(bg = 'black')

count = 0


def click_counter():
	global count
	count += 1
	click.configure(text=count)

txt_count = Label(window, text='Count  -->', font=('Comic Sans MS', 15), bg='black', fg='white')
txt_count.place(x=65, y=75, anchor='center')

click = Label(window,
			  text='0',
			  font=('Comic Sans Ms', 15),
			  bg='black',
			  fg='white'
			  )
click.place(x=145, y=75, anchor='center')

btn_click = Button(window,
				   bg='black',
				   fg='white',
				   activebackground='black',
				   activeforeground='white',
				   text='click',
				   font=('Comic Sans Ms', 20),
				   command=click_counter)
btn_click.place(x=100, y=150, anchor='center')


window.mainloop()