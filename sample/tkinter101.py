import tkinter as tk
from tkinter import ttk


def btn_pressed(idx):
    print(f'button {idx} !!')


root = tk.Tk()

for index_cell in range(3):
    # frame
    btn = tk.Button(
                    root,
                    width = 10,
                    height = 5,
                )
    btn.place(x = 50*index_cell, y=10)   
    btn.pack()
    btn.bind('<Button>', lambda  idx=index_cell: btn_pressed( idx))


btn.focus()
btn.pack(expand=True)

root.mainloop()