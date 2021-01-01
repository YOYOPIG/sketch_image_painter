import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from tkinter import filedialog
# from tkinter import *
from PIL import Image, ImageTk

def browse_sketch():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askopenfilename()
    print(filename)
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    input_sketch_lbl.configure(image=photo)
    input_sketch_lbl.photo = photo

def generate():
    print('gen')

window = tk.Tk()
window.title('Painter')
window.geometry('1000x750')
# window.iconbitmap('./horse.ico')
#window.configure(background='white')
fontStyle_bold = tkFont.Font(family='Open sans bold', size=12)
fontStyle = tkFont.Font(family='Open sans', size=10)

top_frame = tk.Frame(window)
top_frame.pack()
input_frame = tk.Frame(top_frame)
input_frame.pack(side=tk.LEFT)
output_frame = tk.Frame(top_frame)
output_frame.pack(side=tk.RIGHT)
bottom_frame = tk.Frame(window)
bottom_frame.pack()

# 建立事件處理函式（event handler），透過元件 command 參數存取
def echo_hello():
    print('hello world :)')

input_lbl = tk.Label(input_frame, text='Input sketch', font=fontStyle_bold)
input_lbl.pack()
# input_path_lbl = tk.Label(input_frame, text='Input sketch', font=fontStyle_bold)
left_button = tk.Button(input_frame, text='Browse', command=browse_sketch)
left_button.pack()
photo = ImageTk.PhotoImage(Image.open('1.png'))
input_sketch_lbl = tk.Label(input_frame, image=photo)
input_sketch_lbl.pack()
generation_button = tk.Button(input_frame, text='Start', command=generate)
generation_button.pack(fill=tk.X)

output_lbl = tk.Label(output_frame, text='Generated output', font=fontStyle_bold)
output_lbl.pack()
photo2 = ImageTk.PhotoImage(Image.open('1.png'))
output_img_lbl = tk.Label(output_frame, image=photo2)
output_img_lbl.pack()

# img = Image.open(filename)
# photo = ImageTk.PhotoImage(img)
# label = tk.Label(input_frame, image=photo)
# label.pack()


# middle_button = tk.Button(output_frame, text='Green', fg='green')
# middle_button.pack(side=tk.LEFT)

# right_button = tk.Button(output_frame, text='Blue', fg='blue')
# right_button.pack(side=tk.LEFT)

bottom_button = tk.Button(bottom_frame, text='Black', fg='black', command=echo_hello)
bottom_button.pack(side=tk.BOTTOM)

window.mainloop()