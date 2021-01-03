import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from tkinter import filedialog
# from tkinter import *
import os
from shutil import copyfile
from PIL import Image, ImageTk

sketch_path=''
model_path=''
train_img_path=''


def browse_sketch():
    global sketch_path
    filename = filedialog.askopenfilename(initialdir = "./input_paintings")
    print(filename)
    sketch_path = filename
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    input_sketch_lbl.configure(image=photo)
    input_sketch_lbl.photo = photo

def browse_trained():
    global model_path
    filename = filedialog.askopenfilename(initialdir = "./input_images")
    print(filename)
    model_path = filename
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    style_img_lbl.configure(image=photo)
    style_img_lbl.photo = photo

def generate():
    head1, tail1 = os.path.split(sketch_path)
    head2, tail2 = os.path.split(model_path)
    cmd = 'python ./SinGan/paint2image.py --input_name '+tail2+' --ref_name '+tail1+' --paint_start_scale 1'
    print(cmd)
    os.system(cmd)
    img = Image.open('./output_images/generated.png')
    photo = ImageTk.PhotoImage(img)
    output_img_lbl.configure(image=photo)
    output_img_lbl.photo = photo
    
def train():
    head, tail = os.path.split(train_img_path)
    os.system('python main_train.py --input_name '+tail)

def browse_style():
    global train_img_path
    filename = filedialog.askopenfilename()
    head, tail = os.path.split(filename)
    copyfile(filename, './input_images/'+tail)
    img = Image.open('./input_images/'+tail)
    photo = ImageTk.PhotoImage(img)
    style_img_lbl.configure(image=photo)
    style_img_lbl.photo = photo
    os.system('python ./SinGan/main_train.py --input_name '+tail)

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
bottom_frame.pack(pady=20)
browse_frame = tk.Frame(input_frame)
browse_frame.pack()


input_lbl = tk.Label(input_frame, text='Input sketch', font=fontStyle_bold)
input_lbl.pack()
browse_frame = tk.Frame(input_frame)
browse_frame.pack()
browse_lbl = tk.Label(browse_frame, text='Select your sketch image', font=fontStyle)
browse_lbl.pack(side=tk.LEFT)
browse_button = tk.Button(browse_frame, text='Browse', command=browse_sketch)
browse_button.pack(side=tk.RIGHT)
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

style_lbl = tk.Label(bottom_frame, text='Target style', font=fontStyle_bold)
style_lbl.pack()
style_photo = ImageTk.PhotoImage(Image.open('1.png'))
style_img_lbl = tk.Label(bottom_frame, image=style_photo)
style_img_lbl.pack(side=tk.LEFT)
style_button = tk.Button(bottom_frame, text='Select style', command=browse_trained)
style_button.pack(fill=tk.X)
train_button = tk.Button(bottom_frame, text='Train on new image', command=browse_style)
train_button.pack()

window.mainloop()