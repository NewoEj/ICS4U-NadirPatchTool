from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import imghdr

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
        four = ttk.Button(mainframe, text='Preview Edited Photosphere', command = self.preview_photo).grid(column=0, row=4,padx=10,pady=10)
        five = ttk.Button(mainframe, text='Quit.', command=exit).grid(column=0, row=6, padx=10, pady=10)
        six = ttk.Button(mainframe, text='Patch photosphere.', command=self.resize_and_patch).grid(column=0, row=5, padx=10, pady=10)
        seven = ttk.Label(mainframe, text='Nadir Patch Tool', font=("Arial", 20)).grid(column=0, row=0)
        
        mainframe.grid(column=0, row=0)
        
    def choose_photosphere(self):
        self.photosphere_path = filedialog.askopenfilename()
        
    def choose_nadir(self):
        self.nadir_path = filedialog.askopenfilename()
    
    def preview_photo(self):
        try:
            photosphere = Image.open(self.photosphere_path)
            nad = Image.open(self.nadir_path)
            nad = nad.resize(photosphere.size,resample=0)
            photosphere.paste(nad,(0,0),nad)
            photosphere.show()
            
        except ValueError:
            if imghdr.what(self.photosphere_path) != 'jpeg':    # Checks to see if the problem is that the Photosphere is not a jpeg
                Error_Message(1)
            else:                                               # If the Photosphere is a jpeg it means that the nadir was the problem
                Error_Message(0)
        except:                                                 # The Photosphere and Nadir have not been selected          
            Error_Message(1)
            
    def resize_and_patch(self):
        try:
            self.nadir = Image.open(self.nadir_path)
            self.photosphere = Image.open(self.photosphere_path)
            self.nadir = self.nadir.resize(self.photosphere.size, resample=0)
            self.photosphere.paste(self.nadir,(0,0),self.nadir)
        
        except ValueError:
            if imghdr.what(self.photosphere_path) != 'jpeg':    # Checks to see if the problem is that the Photosphere is not a jpeg
                Error_Message(1)
            else:                                               # If the Photosphere is a jpeg it means that the nadir was the problem
                Error_Message(0)
        except:                                                 # The Photosphere and Nadir have not been selected          
            Error_Message(1)
            
        try:            
            self.save_destination = filedialog.asksaveasfilename(defaultextension = ".jpg")
            self.photosphere.save(self.save_destination)
            messagebox.showinfo(title="Program complete.", message="The photosphere has been patched and saved.")
        
        except:                     # Sends an error message if the user exits the save tab before selecting a file to save to
            Error_Message(2)
            

class Error_Message(Toplevel):
    def __init__(self, message_num):
        messages = ["Nadir is not a png file.","Photosphere is not a jpeg file.", "Both a Photosphere and a Nadir have to selected","Not a valid save location."]
        self.error_message = messagebox.showinfo(title="Error", message=messages[message_num])
        
if __name__ == "__main__":
    root = Tk()
    root.title("Nadir Patch Tool")
    Editor_360(root)
    root.mainloop()
