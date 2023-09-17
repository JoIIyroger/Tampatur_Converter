from tkinter import *


def convert():
    temp_c = scale_c.get()
    temp_f = int((temp_c * 9/5)+32)
    label_c.config(text="are "+str(temp_f)+"°F")
    scale_f.set(temp_f)
    label_f.config(text="")


def convert_f():
    temp_f = scale_f.get()
    temp_c = int(((temp_f - 32)*5/9))
    label_f.config(text="are "+str(temp_c) + "°C")
    scale_c.set(temp_c)
    label_c.config(text="")


window = Tk()
frame = Frame(window, bg="#f2e6a0")
frame.pack()

label = Label(frame, text="Convert", font=("Arial", 40), padx=10, pady=10, bg="#f2e6a0")
label.grid(row=0, column=1,)

label_c = Label(frame, text="", font=("Arial", 30), padx=10, pady=10, width=15, bg="#f2e6a0")
label_c.grid(row=1, column=0,)

label_c1 = Label(frame, text="Celsius", font=("Arial", 30), padx=10, pady=10, width=15, bg="#f2e6a0")
label_c1.grid(row=0, column=0,)

button_c = Button(frame, text="Convert", font=("Arial", 20), bg="#f7c068", command=convert)
button_c.grid(row=4, column=0)

scale_c = Scale(frame, from_=100, to=-25, length=500, tickinterval=10, font=("Arial", 20),
                troughcolor="#00f2ff", bg="#faf1bb", fg="#22c3f0")
scale_c.grid(row=2, column=0)

label_f = Label(frame, text="", font=("Arial", 30), padx=10, pady=10, width=15, bg="#f2e6a0")
label_f.grid(row=1, column=2,)

label_f1 = Label(frame, text="Fahrenheit", font=("Arial", 30), padx=10, pady=10, width=15, bg="#f2e6a0")
label_f1.grid(row=0, column=2,)

button_f = Button(frame, text="Convert", font=("Arial", 20), bg="#f7c068", command=convert_f)
button_f.grid(row=4, column=2)

scale_f = Scale(frame, from_=250, to=-25, length=500, tickinterval=25, font=("Arial", 20),
                troughcolor="#2678fc", bg="#faf1bb", fg="#2240f0")
scale_f.grid(row=2, column=2)

window.mainloop()
