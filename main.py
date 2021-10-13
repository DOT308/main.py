import os
import psutil
from multiprocessing import *
from time import *
from tkinter import *
import pyfirmata as fir

from datetime import datetime

count = 0

def proc_1():
    x = Process(target=win)
    x.start()
    psutil.cpu_count()


def proc_2():
    s = Process(target=clock)
    s.daemon = True
    s.start()


def proc_3():
    s = Process(target=clock)
    s.daemon = True
    pid = os.getpid()
    print(pid)
    print("child has been killed")
    parent = psutil.Process()
    for child in parent.children(recursive=True):
        print("child", child)
        child.kill()
    print("current process:", current_process())


def clock():
    while 1 == 1:
        now = datetime.now()
        current_time = now.strftime("%H%M")
        a = fir.Arduino('COM3')
        while 1 == 1:
            while now == now:
                p = current_time
                x = int(p[0])
                y = int(p[1])
                z = int(p[2])
                w = int(p[3])
                if x >= int(0):
                    if x == int(1):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(2):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(1)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(3):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(4):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(5):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(6):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(7):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(8):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(9):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    else:
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                else:
                    print("hello world")
                a.digital[10].write(0)
                if y >= int(0):
                    if y == int(1):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(2):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(1)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(3):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(4):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(5):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(6):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(7):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(8):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(9):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    else:
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                else:
                    print("hello world")
                a.digital[11].write(0)
                if z >= int(0):
                    if z == int(1):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(2):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(1)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(3):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(4):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(5):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(6):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(7):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(8):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(9):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    else:
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                else:
                    print("hello world")
                a.digital[12].write(0)
                if w >= int(0):
                    if w == int(1):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(2):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(1)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(3):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(4):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(5):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(6):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(7):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(8):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(9):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    else:
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                else:
                    print("hello world")
                a.digital[13].write(0)
                # if not now == datetime.now():
                # print(current_time)
                current_time = now.strftime("%H%M")
                now = datetime.now()
            else:
                print("end")
        if count <= 0:
            print('lol ??')


def click():
    global count
    count += 1
    print(count)
    proc_2()
    print("cpu count:", cpu_count())


def win():
    if 0 == 0:
        print(count)

        def update():
            time_string = strftime("%H:%M:%S")
            time_label.config(text=time_string)
            window.after(1000, update)

        window = Tk()
        window.geometry("442x494")
        window.title("CASE TIME")
        icon = PhotoImage(file='icon.png')
        window.iconphoto(True, icon)
        window.config(background='white')  # hex colour picker
        photo = PhotoImage(file='time.png')
        starb = PhotoImage(file='starb.png')
        time_label = Label(window,
                           font=("Arial", 56),
                           fg="white",
                           bg="white",
                           padx=4,
                           pady=4,
                           image=photo,
                           compound='center')
        time_label.pack()
        button = Button(window,
                        text="Screen ON",
                        command=click,
                        font=("arial", 40),
                        fg="white",
                        bg="white",
                        activeforeground="white",
                        activebackground="white",
                        state=ACTIVE,
                        image=starb,
                        compound='center')
        button.pack()
        button = Button(window,
                        text="Screen OFF",
                        command=proc_3,
                        font=("arial", 40),
                        fg="white",
                        bg="white",
                        activeforeground="white",
                        activebackground="white",
                        state=ACTIVE,
                        image=starb,
                        compound='center')
        button.pack()
        update()
        mainloop()


if __name__ == '__main__':
    proc_1()
    print('p')
