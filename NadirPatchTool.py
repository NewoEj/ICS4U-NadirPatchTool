from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Nadir Patch Tool")

def choose_photosphere():
    global photosphere 
    photosphere = filedialog.askopenfilename(filetypes=(("jpeg files","*.jpg"),("all files","*.*")))

def choose_nadir():
    global nadir
    nadir = filedialog.askopenfilename(filetypes=(("jpeg files","*.jpg"),("all files","*.*")))

def choose_save_destination():
    save_destination = filedialog.askdirectory()
    

    

mainframe = ttk.Frame(root, padding="10")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
one = ttk.Button(mainframe, text='Choose the photosphere to be patched.', command=choose_photosphere)
two = ttk.Button(mainframe, text='Choose the nadir to be used.', command=choose_nadir)
three = ttk.Button(mainframe, text='Choose the save location of the patched photosphere.', command=choose_save_destination)
four = ttk.Button(mainframe, text='Quit program.', command=exit)
five = ttk.Label(mainframe, text='Nadir Patch Tool', font=("Arial", 20))

mainframe.grid(column=0, row=0)
one.grid(column=0, row=1, padx=10, pady=10)
two.grid(column=0, row=2, padx=10, pady=10)
three.grid(column=0, row=3, padx=10, pady=10)
four.grid(column=0, row=4, padx=10, pady=10)
five.grid(column=0, row=0)

root.mainloop()
