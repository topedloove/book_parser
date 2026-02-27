from tkinter import *
import requests
from io import BytesIO
from PIL import Image, ImageTk

url = 'https://i.ytimg.com/vi/iWivuAO3X1Q/hqdefault.jpg'


def load_image():
    response = requests.get(url)
    if response.status_code != 200:
        label['text'] = 'Изображение не найдено' + str(response.status_code)
    else:
        image = ImageTk.PhotoImage(Image.open(
            BytesIO(response.content)).resize((500, 500), Image.Resampling.LANCZOS))

        label.config(image=image)
        label.image = image


window = Tk()
window.title('Практика')
window.geometry('500x500')
window.geometry(
    f'+{(window.winfo_screenwidth()-500)//2}+{(window.winfo_screenheight()-500)//2}')
window.resizable(0, 0)

Button(window,
       text='покзать картинку',
       font=('Comic Sans MS', 20),
       command=load_image).pack()

label = Label(window)
label.pack()


window.mainloop()
