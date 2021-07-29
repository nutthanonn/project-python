#My first Game
from tkinter import *
import random
import tkinter.messagebox
block_game = Tk()
block_game.title("block_game")
block_game.geometry("300x250+100+100")
def show_message():
    comfirm = tkinter.messagebox.askquestion("yes", "Start ?")
    if comfirm == "yes":
        block_random()


def block_random():
    n, m = 5, 5
    block = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    for i in range(10):
        b1 = ['-', '-', random.choice(block)]
        b2 = ['-', '-', random.choice(block)]
        if b1 == b2: b2 == ['-', '-', '-', '-', random.choice(block)]
        else: break
    txt = []
    for i in range(n):
        if i < n - 1:
            txt.append('#')
            for j in range(m - 2):
                txt.append('-')
            txt.append('#')
        else:
            for j in range(m):
                txt.append('#')
    for i in range(20):
        r = ['-', '-', '#', '-', '-']
        if txt[i] == "-":
            r1 = random.choice(r)
            txt[i] = r1
    for j in range(3):
        for i in range(len(txt) - 5):
            if txt[i] != '#' and txt[i+5] == '#' and txt[i+5] != b1[2] or txt[i+5] == b2[2]:
                if txt[i] == '-':
                    txt[i] = random.choice(b1)
        for i in range(len(txt)):
            if txt[i] == b1[2] == txt[i+1]:
                txt[i+1] = '-'

        for i in range(len(txt) - 5):
            if txt[i] != '#' and txt[i+5] == '#' and txt[i+5] != b2[2] or txt[i+5] == b1[2]:
                if txt[i] == '-':
                    txt[i] = random.choice(b2)
        for i in range(len(txt)):
            if b2[2] == txt[i] == txt[i+1]:
                txt[i+1] = '-'
    out = ''
    for i in range(25):
        out += txt[i] + " "
        if (i%5) == 4:
            out += '\n'
    boxs.set(txt)
    output.set(out)


def move_box():
    a = positions.get().split()
    box = boxs.get()[2:-2:].split("', '")
    p1 = a[0]; p2 = a[1]; lr = a[2] 
    if int(p1) == 0:
        position = int(p2)
    elif int(p1) != 0:
        position = 5*int(p1) + int(p2)
    if lr == "R":
        if box[position] != "#" and box[position] != "-":
            if box[position + 1] == "-":
                box[position], box[position+1] = box[position+1], box[position]

    elif lr == "L":
        if box[position] != "#" and box[position] != "-":
            if box[position - 1] == "-":
                box[position], box[position-1] = box[position-1], box[position]
    for k in range(2):
        for j in range(5):
            c = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
            for i in range(20):
                if box[i] in c:
                    if box[i+5] == "-":
                        box[i], box[i+5] = box[i+5], box[i]

        for i in range(20):
            if box[i] in c:
                if box[i+1] == box[i] and box[i+2] == box[i] and box[i+6] == box[i]:
                    box[i], box[i+2], box[i+1], box[i+5] = '-', '-', '-', '-'

                elif box[i+1] == box[i] and box[i+5] == box[i]:
                    box[i], box[i+5], box[i+1] = '-', '-', '-'

                elif box[i+1] == box[i] and box[i+2] == box[i]:
                    box[i+1], box[i+2], box[i] = '-', '-', '-'

                elif box[i+1] == j and box[i+6] == j:
                    box[i], box[i+1], box[i+6] = '-', '-', '-'

                elif box[i+1] == box[i]:
                    box[i], box[i+1] = '-', '-'

                elif box[i+5] == box[i]:
                    box[i], box[i+5] = '-', '-'
    out = ''
    for i in range(25):
        out += box[i] + " "
        if (i%5) == 4:
            out += '\n'
    boxs.set(box)
    output.set(out)


def Rule_game():
    r = Tk()
    r.title("Rule")
    r.geometry("700x100")
    lb1 = Label(r, text="เกมประกอบด้วยบอร์ดและบล็อก กำหนดให้บอร์ดมีขนาด 5×5 และบล็อกมีไม่เกิน 2 ชนิด \nเฉพาะบล็อกเท่านั้นที่สามารถเคลื่อนย้ายได้ และจะย้ายไปทางด้านซ้ายหรือด้านขวาเท่านั้นหากมีที่ว่าง ส่วนบอร์ดไม่สามารถเคลื่อนย้ายได้ หลังการเคลื่อนย้ายบล็อกใด ๆที่ไม่มีบล็อกหรือบอร์ดรองรับจะทำให้บล็อกนั้นตกลงไปทับบล็อกหรือบอร์ดที่อยู่ด้านล่าง \nหากมีกลุ่มของบล็อกชนิดเดียวกันตั้งแต่ 2 บล็อกขึ้นไปอยู่ติดกันไม่ว่าจะเป็นในแนวตั้งหรือแนวนอน กลุ่มของบล็อกนั้นจะถูกลบออกไปจากบอร์ด").pack()


def How():
    h = Tk()
    h.title("How to play")
    h.geometry("400x100")
    lb_h = Label(h, text="ใส่ตัวเลข 2 ตัว ขั่นด้วยช่องว่าง 1 ช่อง เเละตามด้วยตัวอักษร L หรือ R \nเพื่อกำหนดทิศทางว่าจะให้กล่องขยับไปทางไหน  \nEx. 1 2 R -> หมายถึง กล่องใน Row=1 colum=2 ไปทาง ขวา").pack()


boxs = StringVar()
positions = StringVar()
output = StringVar()
start = Button(text="Click to Start", command=show_message, fg="black").grid(row=0, column=0)
out_put = Label(textvariable=output).grid(row=1, column=0)
rule = Button(text="RULE", fg="red", command=Rule_game).grid(row=1, column=1)
How_to_play = Button(text="How to play", command=How, fg="green").grid(row=2, column=1)
lb = Entry(textvariable=positions).grid(row=2, column=0)
e = Button(text="Enter", fg="blue", command=move_box).grid(row=3, column=0)
reset_game = Button(text="Reset", fg="red", command=block_random).grid(row=3, column=1)
block_game.mainloop()