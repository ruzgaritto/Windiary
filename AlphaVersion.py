from tkinter import *
from tkinter import filedialog
import time


def saveandexit():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text File", ".txt")])
    if file is None:
        return
    file.write(str(writespace.get(1.0, END)))
    file.write("\n")
    file.write(str(time.ctime()))


window = Tk()
window.geometry("2560x1600")
window.config(bg="#272727")
window.title("Windiary")

frame1 = Frame(window, bg="#272727")
frame1.pack(expand=True)
frame2 = Frame(window, bg="#272727")
frame2.pack(expand=True)

title = Label(frame1, text="Windiary", font=("Tesla", 64), bg="#272727", fg="#5b5b85")
title.pack()

writespace = Text(frame2, bg="#313131", font=("Helvetica", 16), fg="#aaaaff", highlightbackground="#272727",
                  highlightthickness=0, width=100, height=35, padx=20, pady=20)
writespace.pack()

saveandexit = Button(frame2, text="S A V E", command=saveandexit, highlightbackground="#272727")
saveandexit.pack()
Label(frame2, text="This is Alpha Version of Windiary", font="Helvetica", bg="#272727", fg="#5b5b85", pady=20).pack()

window.mainloop()
