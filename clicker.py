import global_vars
from tkinter import *
from time import time
from PIL import ImageTk, Image
from tkinter import messagebox as mb


# import  tkinter as tk
def show_help():
    mb.showinfo(message="Жми кнопку быстрее!")
def show_records():
    records = ""
    with open('clicker_records.txt', 'r', encoding='utf-8') as f:
        record_list = f.readlines()
        records = "".join(record_list)
    mb.showinfo(message= records)

def show_about():
    mb.showinfo(message="Сделал РОББО")

def clicker():
    def entry_clear(z):
        name_entry.delete(0,END)

    def check_record(name: str, points: int) -> None:
        with open('clicker_records.txt', 'r+', encoding='utf-8') as f:
            print(name)
            record_list = f.readlines()
            new_record_list = [line.strip('\n').split(";") for line in record_list]

            for index, line_num in enumerate(new_record_list):
                if points > int(line_num[2]):
                    new_record_list.insert(index, [str(index + 1), name, str(points)])
                    break
            for line_num in range(index + 1, len(new_record_list)):
                new_record_list[line_num][0] = str(line_num + 1)
            print(record_list)
            record_list = [";".join(i) + "\n" for i in new_record_list]
            f.seek(0)
            f.writelines(record_list)

    def on_click():
        if global_vars.cc == 0:
            global_vars.sc = time()
        if time()-global_vars.sc<3:
            global_vars.cc += 1
            lbl.config(text=f"Кликов\n{global_vars.cc}")
        else:
            confirm =mb.showinfo(message=f'Хватит жать!\nВаш результат {global_vars.cc}!')
            check_record(name_entry.get(),global_vars.cc)
            if confirm=="ok":

                lbl.config(text=f"Кликов\n0")
                global_vars.cc=0

    root = Tk()
    root.geometry('400x300+250+200')
    root.resizable(False, False)
    icon_img = PhotoImage(file="hummer.png")
    root.iconposition(100, 50)
    root.iconphoto(False, icon_img)

    bg = ImageTk.PhotoImage(file = 'earth.jpg')
    btn_bg = ImageTk.PhotoImage(file = 'earth2.jpg')
    my_canvas = Canvas(root, width = 400, height = 300,  highlightthickness = 0)
    my_canvas.pack()
    my_canvas.create_image(-100,-100, image = bg, anchor = 'nw')
    """
    Создаём панель меню под заголовком окна
    """
    mainmenu = Menu(root)
    root.config(menu = mainmenu)

    # mainmenu.add_command(label = "Выход", command = root.destroy)
    # mainmenu.add_command(label = "Справка")

    filemenu = Menu(mainmenu, tearoff =0)
    filemenu.add_command(label="Выход", command=root.destroy)

    refmenu = Menu(mainmenu, tearoff =1)
    refmenu.add_command(label="Помощь", command=show_help)
    refmenu.add_command(label="Рекорды", command=show_records)
    refmenu.add_command(label="О программе", command=show_about)

    mainmenu.add_cascade(label = "Файл",menu=filemenu)
    mainmenu.add_cascade(label = "Справка",menu=refmenu)


    btn = Button(text="Жми сюда!",
                 font=("Comic Sans", 15, 'bold'),
                 width=10,
                 height=3,
                 bg="red",
                 fg="#96B254",
                 relief=SOLID,
                 bd=10,
                 command=on_click,
                 image = btn_bg,
                 compound = CENTER,
                 padx = 70,
                 pady=10
                 )
    lbl = Label(text="Кликов\n0",
                font=("Comic Sans", 15, 'bold'),
                width=10,
                height=3,
                bg="yellow",
                fg="green",
                anchor='center',
                justify=CENTER
                )
    name_entry = Entry(root, width=20)
    name_entry.insert(0, "username")
    lbl_window = my_canvas.create_window(200,20, anchor = "n", window = lbl)
    btn_window = my_canvas.create_window(200,100, anchor = "n", window = btn)
    entry_window = my_canvas.create_window(200,250, anchor = "n", window = name_entry)

    name_entry.bind("<Button-1>", entry_clear)

    # lbl.pack()
    # btn.pack()

    root.mainloop()


if __name__ == "__main__":
    clicker()





