from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
from PIL import ImageChops
from PIL import ImageTk
import os

def import_image(base_photo):
    base_photo.set(filedialog.askopenfilename())

def import_nadir(nadir):
    nadir.set(filedialog.askopenfilename())
    
def save_loc(save_location):
    save_location.set(filedialog.askdirectory())
    
def save_image(save_location, base_photo, final_pic):
    new_name = os.path.basename(base_photo.get())
    new_path = os.path.join(save_location.get(), new_name)
    final_pic.save(new_path)

def merge_img(base_photo, nadir):
    global final_pic
    base = Image.open(base_photo.get())
    nad = Image.open(nadir.get())
    merge_im = ImageChops.add_modulo(base,nad)
    width, height = base.size
    width2, height2 = nad.size
    final_pic = final_pic.resize(((width),(height)),0)
    final_pic.paste(merge_im)

root = Tk()
root.title("Nadir Patch Tool")

base_photo = StringVar()
nadir = StringVar()
save_location = StringVar()
final_pic = Image.new("RGBX", (0,0))

mainframe = ttk.Frame(root, padding = "10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

choose_image = ttk.Button(mainframe, text = "Select Photosphere", command = lambda: import_image(base_photo)).grid(column=0, row=1, padx=5,pady=5)
choose_nadir = ttk.Button(mainframe, text = "Select Nadir", command = lambda: import_nadir(nadir)).grid(column=0,row=2,padx=5,pady=5)
choose_save = ttk.Button(mainframe, text = "Select Save Location", command = lambda: save_loc(save_location)).grid(column=0,row=3,padx=5,pady=5)
merge = ttk.Button(mainframe, text = "Merge", command = lambda: merge_img(base_photo, nadir)).grid(column=0,row=4,padx=5,pady=5)
save = ttk.Button(mainframe, text = "Save Merged Photo", command = lambda: save_image(save_location, base_photo, final_pic)).grid(column=0, row=5,padx=5,pady=5)
open_merpic = ttk.Button(mainframe, text="Open Merged Photo", command = lambda: final_pic.show()).grid(column=0,row=6,padx=5,pady=5)
quit = ttk.Button(mainframe, text="Quit Program",command=exit).grid(column=0,row=7,padx=5,pady=5)

image_selected = ttk.Label(mainframe, textvariable = base_photo).grid(column=1, row=0, sticky = W)
nadir_selected = ttk.Label(mainframe, textvariable = nadir).grid(column=1, row=1, sticky=W)
save_selected = ttk.Label(mainframe, textvariable = save_location).grid(column=1, row=2, sticky=W)
title = ttk.Label(mainframe, text='Nadir Patch Tool', font=("Arial", 20)).grid(column=0,row=0)


root.mainloop()