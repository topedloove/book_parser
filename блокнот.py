from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


window = Tk()
window.title('Бокнот')
window.geometry('600x700')
window.geometry(f'+{(window.winfo_screenwidth()-600)//2}+{(window.winfo_screenheight()-700)//2}')

f_text = Frame(window)
f_text.pack(fill=BOTH, expand=1)


def chenge_theme(theme):
	text_fild['bg'] = view_colors[theme]['text_bg']
	text_fild['fg'] = view_colors[theme]['text_fg']
	text_fild['insertbackground'] = view_colors[theme]['cursor']
	text_fild['selectbackground'] = view_colors[theme]['select_bg']


def chenge_fonts(fontes):
	text_fild['font'] = fonts[fontes]['font']


def notepad_exit():
	answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти')
	if answer:
		window.destroy()


def open_file():
	file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt' ), ('Все файлы', '*.*')))
	if file_path:
		text_fild.delete('1.0', END)
		text_fild.insert('1.0', open(file_path, encoding='UTF-8').read())


def safe_file():
	file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt' ), ('Все файлы', '*.*')))
	f = open(file_path, 'w', encoding='utf-8')
	text = text_fild.get('1.0', END)
	f.write(text)
	f.close()


view_colors = {
	'dark': {
		'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#214283'
	},
	'light': {
		'text_bg': 'white', 'text_fg': 'black', 'cursor': 'black', 'select_bg': '#214283'
	}
}

fonts = {
	'Arial': {
		'font': 'Arial 14 bold'
	},
	'Comic Sans MS': {
		'font': ('Comic Sans MS', 14, 'bold')
	},
	'Times New Roman': {
		'font': ('Times New Roman', 14, 'bold')
	}
}

text_fild = Text(f_text,
				 bg='white',
				 fg='black',
				 padx=10,
				 pady=10,
				 wrap=WORD,
				 insertbackground='black',
				 selectbackground='#214283',
				 spacing3=10,
				 width=30,
				 font='Arial 14 bold'
				 )
text_fild.pack(expand=1, fill=BOTH, side='left')

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side='left', fill=Y)
text_fild.config(yscrollcommand=scroll.set)


main_menu = Menu(window)


# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=safe_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
window.config(menu=file_menu)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Темная', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('Comic Sans MS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('Times New Roman'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
window.config(menu=view_menu)


# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)

window.config(menu=main_menu)




window.mainloop()