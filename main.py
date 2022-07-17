import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("GIẢI PHƯƠNG TRÌNH BẬC HAI")

tk.Label(root, text="HỆ SỐ A", font='Helvetica 10 bold').grid(row=1, column=0, padx=(20, 0), pady=(20, 0))

a_coef = tk.StringVar()
tk.Entry(root, textvariable=a_coef).grid(row=1, column=1, padx=20, pady=(20, 0))

######################################################################################

tk.Label(root, text="HỆ SỐ B", font='Helvetica 10 bold').grid(row=2, column=0, padx=(20, 0))

b_coef = tk.StringVar()
tk.Entry(root, textvariable=b_coef).grid(row=2, column=1)

######################################################################################

tk.Label(root, text="HỆ SỐ C", font='Helvetica 10 bold').grid(row=3, column=0, padx=(20, 0), pady=(0, 10))

c_coef = tk.StringVar()
tk.Entry(root, textvariable=c_coef).grid(row=3, column=1, pady=(0, 10))

######################################################################################


def quadratic_equation_solver(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "VÔ SỐ NGHIỆM"
            else:
                return "VÔ NGHIỆM"
        else:
            return "CÓ NGHIỆM DUY NHẤT: {}".format(-c/b)
    else:
        denta = b**2 - 4*a*c
        if denta > 0:
            x1 = (-b + denta**0.5) / (2*a)
            x2 = (-b - denta**0.5) / (2*a)
            return "CÓ HAI NGHIỆM PHÂN BIỆT:\n{}\n{}".format(x1, x2)
        elif denta == 0:
            return "CÓ NGHIỆM KÉP: {}".format(-b/(2*a))
        else:
            x1 = complex(-b/(2*a), (-denta)**0.5 / (2*a))
            x2 = complex(-b/(2*a), -(-denta)**0.5 / (2*a))
            return "CÓ HAI NGHIỆM PHỨC PHÂN BIỆT:\n{}\n{}".format(x1, x2)


def show_graph(a, b, c):
    import matplotlib.pyplot as plt

    x_cords = []
    y_cords = []

    for x in range(-50, 50):
        y = a*x**2 + b*x + c
        x_cords.append(x)
        y_cords.append(y)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x_cords, y_cords)
    plt.savefig("parabol.png")
    plt.show()


def solver():
    a = eval(a_coef.get())
    b = eval(b_coef.get())
    c = eval(c_coef.get())
    res = quadratic_equation_solver(a, b, c)
    messagebox.showinfo("KẾT QUẢ", res)


def show_parabola():
    a = eval(a_coef.get())
    b = eval(b_coef.get())
    c = eval(c_coef.get())
    show_graph(a, b, c)


tk.Button(root, text="GIẢI", font='Helvetica 10 bold', command=solver).grid(row=4, column=0, padx=(20, 0), pady=(2, 10), ipadx=10)
tk.Button(root, text="ĐỒ THỊ", font='Helvetica 10 bold', command=show_parabola).grid(row=4, column=1, pady=(0, 10), ipadx=10)

root.mainloop()
