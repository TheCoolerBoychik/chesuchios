from tkinter import *  # импорт ткинтера
from tkinter import messagebox  # импорт

# главное окно
window = Tk()
window.title('Авторизация')  # заголовок
window.geometry('450x230')
window.resizable(False, False)
font_header = ('Arial', 15)  # вид окна
font_entry = ('Arial', 14)
label_font = ('Arial', 14)
base_padding = {'padx': 10, 'pady': 8}  # вид окна
header_padding = {'padx': 10, 'pady': 12}


def clicked():
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo('Заголовок', '{username}, '
                                     '{password}'.format(username=username, password=password))


main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()
username_label = Label(window, text='Имя пользователя', font=label_font, **base_padding)
username_label.pack()
username_entry = Entry(window, bg='#FFFFFF', fg='#B5DEFA', font=font_entry)
username_entry.pack()
password_label = Label(window, text='Пароль', font=label_font, **base_padding)  # функция для пароля
password_label.pack()

password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)
window.mainloop()  # вывод цикла
