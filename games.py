from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import random


window = Tk()
window.title('Games')
window.geometry('1280x720')
window.geometry(
    f'+{(window.winfo_screenwidth()-1280)//2}+{(window.winfo_screenheight()-720)//2}')
window.resizable(1, 1)


def zheka_is_small():
    def no():
        messagebox.showinfo('', 'Очевидно же')
        window_joke.destroy()

    def motionMouse(event):
        btn1.place(x=random.randint(30, 400), y=random.randint(30, 738))

    window_joke = Toplevel(window)
    window_joke.title('Joke')
    window_joke.geometry('432x768')
    window_joke.geometry(
        f'+{(window_joke.winfo_screenwidth()-432)//2}+{(window_joke.winfo_screenheight()-768)//2}')
    window_joke.resizable(0, 0)
    window_joke['bg'] = 'white'

    window_joke.image = PhotoImage(
        file=r'c:\Users\1\Downloads\convertio.in_S-alnQsDlrn22VJfxgeeMIS7U_6VTMB5oAqkfj1o8lJ6hk862YJgjwmiDm7nAjPGtimRJvyMrRuPa9m-VDeWtd_B.png')
    bg_image = Label(window_joke, image=window_joke.image)
    bg_image.grid(row=0, column=0)

    label = Label(window_joke, text='Бросит ли "Жека французский багет" пить ?', font=(
        'Comic Sans MS', 14), bg='gray')
    label.place(relx=0.5, y=200, anchor='center')

    btn1 = Button(window_joke, text='Да', font=(
        'Comic Sans MS', 16), bg='gray', command=motionMouse)
    btn1.place(x=120, y=270, anchor='center')
    btn1.bind('<Enter>', motionMouse)

    btn2 = Button(window_joke, text='Нет', font=(
        'Comic Sans MS', 16), bg='gray', command=no)
    btn2.place(x=320, y=270, anchor='center')


def question_func():
    window_questionw = Tk()
    window_questionw.title('?')
    window_questionw.geometry('740x493')
    window_questionw.resizable(False, False)
    window_questionw.geometry(
        f'+{(window_questionw.winfo_screenwidth()-740)//2}+{(window_questionw.winfo_screenheight()-493)//2}')
    window_questionw.config(bg='black')

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

    label = Label(window_questionw, font=(
        'Comic Sans MS', 20), bg='black', fg='white')
    label.pack(pady=125)

    btn1 = Button(window_questionw, font=('Comic Sans MS', 20), text='?',
                  command=get, bg='black', fg='white')
    btn1.place(x=150, y=250)

    btn2 = Button(window_questionw, font=('Comic Sans MS', 20), text='?',
                  command=get2, bg='black', fg='white')
    btn2.place(x=250, y=250)

    btn3 = Button(window_questionw, font=('Comic Sans MS', 20), text='?',
                  command=get3, bg='black', fg='white')
    btn3.place(x=350, y=250)

    btn4 = Button(window_questionw, font=('Comic Sans MS', 20), text='?',
                  command=get4, bg='black', fg='white')
    btn4.place(x=450, y=250)

    btn5 = Button(window_questionw, font=('Comic Sans MS', 20), text='?',
                  command=get5, bg='black', fg='white')
    btn5.place(x=550, y=250)

    clear_btn = Button(window_questionw, text='clear', font=(
        'Comic Sans MS', 20), command=clear, bg='black', fg='white')
    clear_btn.place(x=325, y=350)

    ent = Entry(window_questionw, show='*')
    ent.place(x=380, y=50, anchor='center')

    btn_get = Button(window_questionw, bg='black', fg='white', text='Вывести',
                     font=('Comic Sans MS', 15), command=get_text)
    btn_get.place(x=230, y=50, anchor='center')

    label_text = Label(window_questionw, bg='black', fg='white',
                       font=('Comic Sans MS', 20))
    label_text.place(x=380, y=100, anchor='center')

    btn_clear = Button(window_questionw, bg='black', fg='white', text='Очистить', font=(
        'Comic Sans MS', 15), command=clear_text)
    btn_clear.place(x=120, y=50, anchor='center')


def click_count_func():
    window_click = Tk()
    window_click.title('Сlick counter')
    window_click.geometry('200x200')
    window_click.resizable(False, False)
    window_click.geometry(
        f'+{(window_click.winfo_screenwidth()-200)//2}+{(window_click.winfo_screenheight()-200)//2}')
    window_click.config(bg='black')

    count = 0

    def click_counter():
        nonlocal count
        count += 1
        click.configure(text=count)

    txt_count = Label(window_click, text='Count  -->',
                      font=('Comic Sans MS', 15), bg='black', fg='white')
    txt_count.place(x=65, y=75, anchor='center')

    click = Label(window_click,
                  text='0',
                  font=('Comic Sans Ms', 15),
                  bg='black',
                  fg='white'
                  )
    click.place(x=145, y=75, anchor='center')

    btn_click = Button(window_click,
                       bg='black',
                       fg='white',
                       activebackground='black',
                       activeforeground='white',
                       text='click',
                       font=('Comic Sans Ms', 20),
                       command=click_counter)
    btn_click.place(x=100, y=150, anchor='center')


def magic_ball_func():
    def ask_question():
        question = simpledialog.askstring(
            "Magic square", 'Задайте свой вопрос')
        if question:
            answers = [
                # 🔮 Философские / Загадочные
                "Звёзды шепчут «да», но Луна морщится",
                "Вселенная кивает, но тень сомнения ползёт по стене",
                "Это случится, если перестанешь об этом спрашивать",
                "Ответ спит в кармане у следующего прохожего",
                "Духи перемен уже в пути... но могут свернуть не туда",
                "Да, но придётся пожертвовать пакетом чипсов",
                "Карты судьбы перемешались. Перетасуй жизнь и спроси снова",
                # 😄 Смешные / Абсурдные
                "Мой внутренний голос сейчас на кофе-брейке. Попробуй позже",
                "Будущее говорит: «Пока не купишь печеньку — не скажу»",
                "Да, но с оговорками размером со слона",
                "Нет. Но если надеть носки наизнанку — возможно",
                "Шансы 50/50: либо да, либо нет",
                "Спроси у своей кошки — у неё виднее",
                "Переформулируй запрос на языке дельфинов",
                "Ответ затерялся в спаме Вселенной",
                # 🌌 Поэтичные / Образные
                "Река времени поворачивает в твою сторону",
                "Падающая звезда только что ответила «да» за тебя",
                "Ветер принёс «да», но он может смениться на «нет» к полуночи",
                "Сердце вселенной бьётся в такт твоему желанию",
                "Созвездие Ответа восходит на востоке",
                # ⚠️ Прагматичные / Странные
                "Вероятность: 73.8%. Погрешность: ±20%",
                "По расчётам — да. По факту — кто его знает",
                "Система дала сбой. Попробуйте перезагрузить реальность",
                "Это зависит от гравитационных колебаний Юпитера",
                "Ответа нет в моей базе данных. Обнови прошивку судьбы",
                # 🎭 Двусмысленные
                "И да, и нет, и пролитое молоко",
                "Знаки есть, но они на мертвом языке",
                "Спроси ещё раз, когда дождь пойдёт вверх",
                "Твой вопрос опоздал на 5 минут. Приди завтра",
                # ✨ Магические
                "Хрустальный шум говорит: «Возможно»",
                "Древние руны показывают туманный путь",
                "Духи огня говорят «да», духи воды — «нет». Выбирай сторону",
                "Магия молчит. Попробуй принести жертву... шоколадку"
            ]
            answer = random.choice(answers)

            dialog = Toplevel(window)
            dialog.title('Ответ')
            dialog.geometry('500x200')

            dialog.update_idletasks()
            x = (dialog.winfo_screenwidth() // 2) - (500 // 2)
            y = (dialog.winfo_screenheight() // 2) - (200 // 2)
            dialog.geometry(f"+{x}+{y}")

            Label(
                dialog, text=answer, font=('Arial', 14), wraplength=500).pack(expand=True, padx=20, pady=50)

            Button(dialog, text="OK",
                   command=dialog.destroy).pack(pady=20)

    window = Tk()
    window.title('Magic square')
    window.geometry('626x626')
    window.resizable(True, True)

    window.configure(bg='#0f0f23')  # Тёмно-синий космос
    label_bg = '#0f0f23'
    btn_bg = '#9b59b6'

    window.geometry(
        f'+{(window.winfo_screenwidth()-626)//2}+{(window.winfo_screenheight()-626)//2}')

    label = Label(window, text='Magic square', font=('Arial', 24, 'bold'))
    label.pack(side='top', pady=30)

    btn = Button(window, text='Задать вопрос', font=(
        'Arial', 16, 'bold'), command=ask_question)
    btn.pack(side='bottom', anchor='center', pady=50)


tab_control = ttk.Notebook(window)
joke = ttk.Frame(tab_control)
tab_control.add(joke, text='Жека мелкий')
tab_control.place(x=0, y=0, relwidth=1, relheight=1)

joke_btn = Button(joke,
                  text='запустить',
                  font=('Comic Sans MS', 20),
                  command=zheka_is_small,
                  bg='red')
joke_btn.place(relx=0.5, rely=0.5, anchor='center')

question = ttk.Frame(tab_control)
tab_control.add(question, text='?-?-?-?-?-?')

question_btn = Button(question,
                      text='запустить',
                      font=('Comic Sans MS', 20),
                      command=question_func,
                      bg='orange')
question_btn.place(relx=0.5, rely=0.5, anchor='center')

click_count = ttk.Frame(tab_control)
tab_control.add(click_count, text='the clicker')

click_count_btn = Button(click_count,
                         text='запустить',
                         font=('Comic Sans MS', 20),
                         command=click_count_func,
                         bg='yellow')
click_count_btn.place(relx=0.5, rely=0.5, anchor='center')

magic_ball = ttk.Frame(tab_control)
tab_control.add(magic_ball, text='Magic ball')

magic_ball_btn = Button(magic_ball,
                        text='запустить',
                        font=('Comic Sans MS', 20),
                        command=magic_ball_func,
                        bg='green')
magic_ball_btn.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop()
