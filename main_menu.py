from tkinter import *
from clicker import *

def start_game1():
    game1_wind = Toplevel(tk)
    clicker(game1_wind)

def records():
    rec_wind = Toplevel(tk)
    rec_wind.title("Рекордсмены")
    width = 300
    height = 400
    rec_wind.geometry(f'{width}x{height}')
    rec_wind.resizable(False, False)
    rec_canvas = Canvas(rec_wind, width = width, height=height, bg='yellow')
    rec_canvas.pack()
    rec_canvas.create_text(width//2,
                           10,
                           text="Рекордсмены",
                           font=("Comic Sans", 15, 'bold'))
    records = ""
    with open('clicker_records.txt', 'r', encoding='utf-8') as f:
        record_list = f.readlines()
        records = "".join(record_list)
    rec_canvas.create_text(width // 2,
                           100,
                           text=records,
                           font=("Comic Sans", 15, 'bold'))


tk = Tk()

tk.title("Мое приложение")
tk.resizable(False, False)
tk.geometry('200x100')
tk.config(bg='green')

btn1 = Button(tk, text="Играть в кликер", command=start_game1)
btn2 = Button(tk, text="Рекорды", command=records)

btn1.place(x=100, y=10, anchor='n')
btn2.place(x=100, y=50, anchor='n')



tk.mainloop()