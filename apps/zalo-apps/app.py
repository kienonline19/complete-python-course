import utils
import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
root.geometry('400x200+150+150')
root.title('UNG DUNG SAO CHEP FILE')

data_folder = tk.StringVar()
dst1_folder = tk.StringVar()
dst2_folder = tk.StringVar()


def select_data_folder():
    data_folder.set(fd.askdirectory())


def select_dst1():
    dst1_folder.set(fd.askdirectory())


def select_dst2():
    dst2_folder.set(fd.askdirectory())


data_btn = tk.Button(root, text='CHON THU MUC DATA',
                     command=select_data_folder)
data_btn.pack()

data_lbl = tk.Label(root, textvariable=data_folder)
data_lbl.pack()

dst1_btn = tk.Button(root, text='CHON THU MUC OUTPUT1', command=select_dst1)
dst1_btn.pack()

dst1_lbl = tk.Label(root, textvariable=dst1_folder)
dst1_lbl.pack()

dst2_btn = tk.Button(root, text='CHON THU MUC OUTPUT2', command=select_dst2)
dst2_btn.pack()

dst2_lbl = tk.Label(root, textvariable=dst2_folder)
dst2_lbl.pack()


def handle():
    my_path = data_folder.get()
    dst1 = dst1_folder.get()
    dst2 = dst2_folder.get()
    utils.copy_files(dst1, dst2, my_path)


btn = tk.Button(root, text='XU LY', command=handle)
btn.pack()

root.mainloop()
