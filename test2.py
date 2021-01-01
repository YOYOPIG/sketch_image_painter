# print('YEE')
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk

def change_pic():
    vlabel.configure(image=root.photo1)

root = tk.Tk()

photo = '1.jpg'
photo1 = "2.jpg"
root.photo = ImageTk.PhotoImage(Image.open(photo))
root.photo1 = ImageTk.PhotoImage(Image.open(photo1))

vlabel=tk.Label(root,image=root.photo)
vlabel.pack()

b2=tk.Button(root,text="Capture",command=change_pic)
b2.pack()

root.mainloop()