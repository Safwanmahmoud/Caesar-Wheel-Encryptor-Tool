import math
from tkinter import *

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
letters_smallCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]
root = Tk()
root.geometry("963x600")
myCanvas = Canvas(root, height=500, width=900)
myCanvas.place(x=0, y=0)

for i in range(1, 27):
    var = StringVar()
    var.set(letters[i - 1])

    globals()['labels%s' % i] = Label(root, textvariable=var, relief=RAISED, bd=0, font=("Arial", 25), anchor=NE)
    globals()['labels%s' % i].place(
        x=780 + (150 * math.cos(math.radians(13.84615 * i + 5 * 13.84615))),
        y=200 - (150 * math.sin(math.radians(13.84615 * i + 5 * 13.84615))))

for i in range(1, 27):
    var = StringVar()
    var.set(letters[i - 1])
    Label(root, textvariable=var, relief=RAISED, bd=0, font=("Arial", 15)).place(
        x=780 + (110 * math.cos(math.radians(13.84615 * i + 5 * 13.84615))),
        y=200 - (110 * math.sin(math.radians(13.84615 * i + 5 * 13.84615))))

T_1 = Text(root, font=("Arial", 15), width=50, height=8)
T_2 = Text(root, font=("Arial", 15), width=50, height=8)

T_1.place(x=40, y=40)
T_2.place(x=40, y=300)


def create_circle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)


def add_the_circle(init_angle):
    for i in range(1, 27):
        var = StringVar()
        var.set(letters[i - 1])

        globals()['labels%s' % i] = Label(root, textvariable=var, relief=RAISED, bd=0, font=("Arial", 25), anchor=NE)
        globals()['labels%s' % i].place(
            x=780 + (150 * math.cos(math.radians(13.84615 * i + init_angle + 5 * 13.84615))),
            y=200 - (150 * math.sin(math.radians(13.84615 * i + init_angle + 5 * 13.84615))))


def destroy_circle():
    for i in range(1, 27):
        globals()['labels%s' % i].destroy()


E1 = Entry(root, bd=5, width=5)
E1.insert(END, 0)
E1.place(x=770, y=440)


def rotate(l, n):
    return l[n:] + l[:n]


def solve():
    inp = T_1.get(1.0, "end-1c")
    solved = []
    no = int(E1.get())
    destroy_circle()
    add_the_circle(no * 13.84615)
    rotated_letters = rotate(letters_smallCase, no)
    for o in inp:

        for r in range(len(letters_smallCase)):
            if o == letters_smallCase[r]:
                solved.append(rotated_letters[r])
        if o == " ":
            solved.append(" ")
    solved = ''.join(solved)
    T_2.delete(1.0, 'end')
    T_2.insert(END, solved)


solve = Button(root, width=25, bd=5, text="Solve!", command=solve).place(x=400, y=520)

root.mainloop()
