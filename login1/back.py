from tkinter import*
from PIL import*
self_root = Tk()

self_root.geometry("455x244")
photo = PhotoImage(file="vector")
t_label = Label(image=photo)
t_label.pack()

self_root.mainloop()