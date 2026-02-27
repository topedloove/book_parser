from tkinter import *
from datetime import datetime

window = Tk()
window.title('Секундомер')
window.geometry('300x200')
window.resizable(False, False)
window.geometry(f'+{(window.winfo_screenwidth()-300)//2}+{(window.winfo_screenheight()-200)//2}')

temp = 0
after_id = ''


def tick():
	global temp, after_id
	after_id = window.after(1000, tick)
	f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
	label.configure(text=str(f_temp))
	temp += 1


def tick_start():
	btn_start.pack_forget()
	btn_stop.pack()
	tick()



def tick_stop():
	btn_stop.pack_forget()
	btn_continue.pack()
	btn_clean.pack()
	window.after_cancel(after_id)


def tick_continue():
	btn_continue.pack_forget()
	btn_clean.pack_forget()
	btn_stop.pack()
	tick()


def tick_clean():
	global temp
	temp = 0
	label.configure(text='00:00')
	btn_continue.pack_forget()
	btn_clean.pack_forget()
	btn_start.pack()



label = Label(window, text='00:00', font=('Comic Sans MS', 20), width=10)
label.pack()

btn_start = Button(window, text='Start', font=('Comic Sans MS', 20), width=15, command=tick_start)
btn_start.pack()

btn_stop = Button(window, text='Stop', font=('Comic Sans MS', 20), width=15, command=tick_stop)
btn_continue = Button(window, text='continue', font=('Comic Sans MS', 20), width=15, command=tick_continue)
btn_clean = Button(window, text='clean', font=('Comic Sans MS', 20), width=15, command=tick_clean)






window.mainloop()