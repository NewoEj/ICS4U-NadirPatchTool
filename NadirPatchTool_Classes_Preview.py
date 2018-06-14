from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

from PIL import Image
from PIL import ImageTk

class Editor_360(ttk.Frame):
    
    def __init__(self, parent):
        
        self.photosphere = Image.Image._new
        self.nadir = Image.Image._new
        
        mainframe = ttk.Frame(parent, padding="10")
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        one = ttk.Button(mainframe, text='Choose the photosphere to be patched.', command=self.choose_photosphere).grid(column=0, row=1, padx=10, pady=10)
        two = ttk.Button(mainframe, text='Choose the nadir to be used.', command=self.choose_nadir).grid(column=0, row=2, padx=10, pady=10)
        three = ttk.Button(mainframe, text='Resize nadir.', command=self.resize_nadir).grid(column=0, row=3, padx=10, pady=10)
        four = ttk.Button(mainframe, text='Preview Edited Photosphere', command = self.preview_photo).grid(column=0, row=4,padx=10,pady=10)
        five = ttk.Button(mainframe, text='Quit.', command=exit).grid(column=0, row=6, padx=10, pady=10)
        six = ttk.Button(mainframe, text='Patch photosphere.', command=self.patch).grid(column=0, row=5, padx=10, pady=10)
        seven = ttk.Label(mainframe, text='Nadir Patch Tool', font=("Arial", 20)).grid(column=0, row=0)
        
        mainframe.grid(column=0, row=0)
        
    def choose_photosphere(self):
        self.photosphere_path = filedialog.askopenfilename()
        
    def choose_nadir(self):
        self.nadir_path = filedialog.askopenfilename()
                
    def resize_nadir(self):
        self.nadir = Image.open(self.nadir_path)
        self.photosphere = Image.open(self.photosphere_path)
        self.nadir = self.nadir.resize(self.photosphere.size, resample=0)
    
    def preview_photo(self):
        #self.preview_app = Preview_360(self.photosphere_path, self.nadir_path)
        photosphere = Image.open(self.photosphere_path)
        nad = Image.open(self.nadir_path)
        nad = nad.resize(photosphere.size,resample=0)
        photosphere.paste(nad,(0,0),nad)
        photosphere.show()
            
    def patch(self):
        self.save_destination = filedialog.asksaveasfilename(defaultextension = ".jpg")
        self.photosphere.paste(self.nadir,(0,0),self.nadir)
        self.photosphere.save(self.save_destination)
        messagebox.showinfo(title="Program complete.", message="The photosphere has been patched and saved.")

#class Preview_360(Toplevel):
#    def __init__(self, photosphere_path, nadir_path):
#        try:
#            self.photosphere = Image.open(photosphere_path)
#            self.nadir = Image.open(nadir_path)
#            self.photosphere = self.photosphere.resize((1000, 500), Image.BICUBIC)
#            self.nadir = self.nadir.resize((1000, 500), Image.BICUBIC)
#            self.photosphere_tk = ImageTk.PhotoImage(self.photosphere)
#            self.nadir_tk = ImageTk.PhotoImage(self.nadir)
#            self.preview = Toplevel()
#            self.preview.title("Photosphere Preview")
#            self.previewer = Canvas(self.preview, width = 1000, height = 500)
#            self.previewer.pack(expand = 1, fill = BOTH)
#            self.previewer.create_image(500, 250, image = self.photosphere_tk)
#            self.previewer.create_image(500, 250, image = self.nadir_tk)
#        except:
#            Error_Message()

class Error_Message(Toplevel):
    def __init__(self):
        self.error_message = messagebox.showinfo(title="Error", message="Invalid Option")
        
if __name__ == "__main__":
    root = Tk()
    root.title("Nadir Patch Tool")
    Editor_360(root)
    root.mainloop()
