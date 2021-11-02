from tkinter import *

def start_game1():
    pass
def records():
    pass
root = Tk()

root.title("Мое приложение")
root.resizable(False, False)
root.geometry('200x100')
root.config(bg='green')

btn1 = Button(root, text="Играть в кликер", command=start_game1)
btn2 = Button(root, text="Рекорды", command=records)

btn1.place(x=100, y=10, anchor='n')
btn2.place(x=100, y=50, anchor='n')

root.mainloop()