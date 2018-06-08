from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk


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

def preview():
    photosphere = Image.open(photosphere_path)
    nad = Image.open(nadir_path)
    nad = nad.resize(photosphere.size,resample=0)
    photosphere.paste(nad,(0,0),nad)
    photosphere.show()
    

mainframe = ttk.Frame(root, padding="10")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
one = ttk.Button(mainframe, text='Choose the photosphere to be patched.', command=choose_photosphere).grid(column=0, row=1, padx=10, pady=10)
two = ttk.Button(mainframe, text='Choose the nadir to be used.', command=choose_nadir).grid(column=0, row=2, padx=10, pady=10)
three = ttk.Button(mainframe, text='Choose the save location of the patched photosphere.', command=choose_save_destination).grid(column=0, row=3, padx=10, pady=10)
four = ttk.Button(mainframe, text='Resize nadir.', command=resize_nadir).grid(column=0, row=4, padx=10, pady=10)
five = ttk.Button(mainframe, text='Quit.', command=exit).grid(column=0, row=7, padx=10, pady=10)
six = ttk.Button(mainframe, text='Patch photosphere.', command=patch).grid(column=0, row=5, padx=10, pady=10)
eight = ttk.Button(mainframe, text='Preview', command = preview).grid(column=0,row=6,padx=10,pady=10)
seven = ttk.Label(mainframe, text='Nadir Patch Tool', font=("Arial", 20)).grid(column=0, row=0)

mainframe.grid(column=0, row=0)
root.mainloop()
