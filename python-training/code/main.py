import tkinter as tk
from tkinter import messagebox


class Quadrilateral:
    def __init__(self, edge1, edge2, edge3, edge4):
        self.edge1 = edge1
        self.edge2 = edge2
        self.edge3 = edge3
        self.edge4 = edge4

    @property
    def perimeter(self):
        return self.edge1 + self.edge2 + self.edge3 + self.edge4

    @property
    def max_distance(self):
        return max(self.edge1, self.edge2, self.edge3, self.edge4)

    def __str__(self):
        return f"{self.edge1} - {self.edge2} - {self.edge3} - {self.edge4}"


root = tk.Tk()
root.title('Bài tập 1')
root.geometry('500x300')

lbl1_1 = tk.Label(root, text=' ' * 9)
lbl1_1.grid(row=0, column=0)

lbl1 = tk.Label(root, text='Tứ giác 1')
lbl1.grid(row=0, column=1)

lbl2 = tk.Label(root, text='Tứ giác 2')
lbl2.grid(row=0, column=2)

lbl3 = tk.Label(root, text='Tứ giác 3')
lbl3.grid(row=0, column=3)

# Edge1
lbl1_e1 = tk.Label(root, text='Cạnh 1:')
lbl1_e1.grid(row=1, column=0)

quad1_e1 = tk.StringVar()
txt1_e1 = tk.Entry(root, textvariable=quad1_e1)
txt1_e1.grid(row=1, column=1)

quad2_e1 = tk.StringVar()
txt2_e1 = tk.Entry(root, textvariable=quad2_e1)
txt2_e1.grid(row=1, column=2)

quad3_e1 = tk.StringVar()
txt3_e1 = tk.Entry(root, textvariable=quad3_e1)
txt3_e1.grid(row=1, column=3)

# Edge2
lbl1_e2 = tk.Label(root, text='Cạnh 2:')
lbl1_e2.grid(row=2, column=0)

quad1_e2 = tk.StringVar()
txt1_e2 = tk.Entry(root, textvariable=quad1_e2)
txt1_e2.grid(row=2, column=1)

quad2_e2 = tk.StringVar()
txt2_e2 = tk.Entry(root, textvariable=quad2_e2)
txt2_e2.grid(row=2, column=2)

quad3_e2 = tk.StringVar()
txt3_e2 = tk.Entry(root, textvariable=quad3_e2)
txt3_e2.grid(row=2, column=3)

# Edge3
lbl1_e3 = tk.Label(root, text='Cạnh 3:')
lbl1_e3.grid(row=3, column=0)

quad1_e3 = tk.StringVar()
txt1_e3 = tk.Entry(root, textvariable=quad1_e3)
txt1_e3.grid(row=3, column=1)

quad2_e3 = tk.StringVar()
txt2_e3 = tk.Entry(root, textvariable=quad2_e3)
txt2_e3.grid(row=3, column=2)

quad3_e3 = tk.StringVar()
txt3_e3 = tk.Entry(root, textvariable=quad3_e3)
txt3_e3.grid(row=3, column=3)

# Edge4
lbl1_e4 = tk.Label(root, text='Cạnh 4:')
lbl1_e4.grid(row=4, column=0)

quad1_e4 = tk.StringVar()
txt1_e4 = tk.Entry(root, textvariable=quad1_e4)
txt1_e4.grid(row=4, column=1)

quad2_e4 = tk.StringVar()
txt2_e4 = tk.Entry(root, textvariable=quad2_e4)
txt2_e4.grid(row=4, column=2)

quad3_e4 = tk.StringVar()
txt3_e4 = tk.Entry(root, textvariable=quad3_e4)
txt3_e4.grid(row=4, column=3)


def get_result():
    try:
        values = [
            (quad1_e1, quad1_e2, quad1_e3, quad1_e4),
            (quad2_e1, quad2_e2, quad2_e3, quad2_e4),
            (quad3_e1, quad3_e2, quad3_e3, quad3_e4),
        ]

        perimeters = []

        for counter, value in enumerate(values, start=1):
            obj = Quadrilateral(*map(lambda x: eval(x.get()), value))
            res = f'Chu vi tứ giác {counter}: {obj.perimeter}. Cạnh lớn nhất: {obj.max_distance}'
            perimeters += [obj.perimeter]
            tk.Label(root, text=res).grid(row=counter + 5, column=1)

        min_cv = min(perimeters)
        temp = []

        for idx, per in enumerate(perimeters, start=1):
            if per == min_cv:
                temp += [f'Tứ giác {idx} có chu vi nhỏ nhất']

        for idx, string in enumerate(temp, start=1):
            tk.Label(root, text=string).grid(row=idx + 8, column=1)
    except Exception:
        messagebox.showerror('Lỗi đầu vào', 'Một số ô đầu vào không phải số')


btn_result = tk.Button(text='Xem kết quả', command=get_result)
btn_result.grid(row=5, column=1)
root.mainloop()
