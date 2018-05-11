from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root = Tk()
root.title("Nadir Patch Tool")

def choose_photosphere():
    global photosphere_path
    photosphere_path = filedialog.askopenfilename()

def choose_nadir():
    global nadir_path
    nadir_path = filedialog.askopenfilename()

def choose_save_destination():
    global save_destination 
    save_destination = filedialog.askdirectory()

def resize_nadir():
    global nadir 
    nadir = Image.open(nadir_path)
    global photosphere
    photosphere = Image.open(photosphere_path)
    nadir = nadir.resize(photosphere.size, resample=0)
    
def patch():
    photosphere.paste(nadir,(0,0),nadir)
    photosphere.save("patchedsphere.jpeg","JPEG")
    messagebox.showinfo(title="Program complete.", message="The photosphere has been patched and saved.")

mainframe = ttk.Frame(root, padding="10")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
one = ttk.Button(mainframe, text='Choose the photosphere to be patched.', command=choose_photosphere)
two = ttk.Button(mainframe, text='Choose the nadir to be used.', command=choose_nadir)
three = ttk.Button(mainframe, text='Choose the save location of the patched photosphere.', command=choose_save_destination)
four = ttk.Button(mainframe, text='Resize nadir.', command=resize_nadir)
five = ttk.Button(mainframe, text='Quit.', command=exit)
six = ttk.Button(mainframe, text='Patch photosphere.', command=patch)
seven = ttk.Label(mainframe, text='Nadir Patch Tool', font=("Arial", 20))

mainframe.grid(column=0, row=0)
one.grid(column=0, row=1, padx=10, pady=10)
two.grid(column=0, row=2, padx=10, pady=10)
three.grid(column=0, row=3, padx=10, pady=10)
four.grid(column=0, row=4, padx=10, pady=10)
five.grid(column=0, row=6, padx=10, pady=10)
six.grid(column=0, row=5, padx=10, pady=10)
seven.grid(column=0, row=0)

root.mainloop()
