# Imports necessary tkinter modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

# Imports module necessary to determine the type of image
import imghdr

# Imports the necessary PIL modules
from PIL import Image
from PIL import ImageTk

class Editor_360(ttk.Frame):
    
    def __init__(self, parent):
        
        self.photosphere = Image.Image._new
        self.nadir = Image.Image._new

        # Creates the GUI
        mainframe = ttk.Frame(parent, padding="10")
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        # Creates the buttons and labels
        ttk.Button(mainframe, text='Step 1: Choose the photosphere to be patched.', command=self.choose_photosphere).grid(column=0, row=1, padx=10, pady=10)
        ttk.Button(mainframe, text='Step 2: Choose the nadir in 2:1 aspect ratio to be used.', command=self.choose_nadir).grid(column=0, row=2, padx=10, pady=10)
        ttk.Button(mainframe, text='Step 3: Preview Edited Photosphere', command = self.preview_photo).grid(column=0, row=4,padx=10,pady=10)
        ttk.Button(mainframe, text='Quit.', command=exit).grid(column=0, row=6, padx=10, pady=10)
        ttk.Button(mainframe, text='Step 4: Patch photosphere.', command=self.resize_and_patch).grid(column=0, row=5, padx=10, pady=10)
        ttk.Label(mainframe, text='Nadir Patch Tool', font=("Arial", 20)).grid(column=0, row=0)

        # Allows the buttons and labels to be organized
        mainframe.grid(column=0, row=0)
        
    def choose_photosphere(self):
        # Opens a selection box for the user to choose the photosphere that will be patched, and limits the possible input file types
        self.photosphere_path = filedialog.askopenfilename(filetypes=(("jpeg files","*.jpg"),("all files","*")))
        
    def choose_nadir(self):
        # Opens a selection box for the user to choose the nadir that will be applied to the photosphere, and limits the possible input file types
        self.nadir_path = filedialog.askopenfilename(filetypes=(("png files","*.png"),("all files","*")))
    
    def preview_photo(self):
        # Tries to display the photo
        try:
            # Opens the photosphere and nadir
            self.photosphere = Image.open(self.photosphere_path)
            self.nad = Image.open(self.nadir_path)
            # Resizes the nadir to the dimensions of the photosphere
            self.nad = self.nad.resize(self.photosphere.size,resample=0)
            # Pastes the nadir onto the photosphere at (0,0)
            self.photosphere.paste(self.nad,(0,0),self.nad)
            # Displays the photosphere
            self.photosphere.show()

        # Checks if the photosphere and nadir are the correct file format
        except OSError:
            # Checks to see if the problem is that the photosphere is not a jpeg
            if imghdr.what(self.photosphere_path) != 'jpeg':
                Error_Message(1)
            # If the photosphere is a jpeg, then the nadir must be the problem
            elif imghdr.what(self.nadir_path) != 'png':
                Error_Message(0)
        # Checks if both a photosphere and nadir have been selected
        except AttributeError:
            Error_Message(2)
            
    def resize_and_patch(self):
        # Tries to resize the nadir and paste it onto the photosphere
        try:
            # Opens the nadir and photosphere
            self.nadir = Image.open(self.nadir_path)
            self.photosphere = Image.open(self.photosphere_path)
            # Resizes the nadir to the dimensions of the photosphere
            self.nadir = self.nadir.resize(self.photosphere.size, resample=0)
            # Pastes the nadir onto the photosphere at (0,0)
            self.photosphere.paste(self.nadir,(0,0),self.nadir)

        # Checks if the photosphere and nadir are the correct file format
        except OSError:
            # Checks to see if the problem is that the photosphere is not a jpeg
            if imghdr.what(self.photosphere_path) != 'jpeg':
                Error_Message(1)
            # If the photosphere is a jpeg, then the nadir must be the problem
            elif imghdr.what(self.nadir_path) != 'png':
                Error_Message(0)
        # Checks if both a photosphere and nadir have been selected
        except AttributeError:
            Error_Message(2)

        # Tries to save the patched photosphere
        try:
            # Opens a selection box for the user to choose the name and save location of the finished photosphere
            self.save_destination = filedialog.asksaveasfilename(defaultextension = ".jpg")
            # Saves the photosphere to the selected location
            self.photosphere.save(self.save_destination)
            # Displays a pop-up box informing the user that the photosphere has been patched and saved
            messagebox.showinfo(title="Program complete.", message="The photosphere has been patched and saved.")

        # Sends an error message if the user exits the selection box before selecting a save location
        except: 
            Error_Message(3)

class Error_Message(Toplevel):
    def __init__(self, message_num):
        # Creates a list of possible error messages
        messages = ["Nadir is not a .png file. Please select a .png file to be used as the nadir.","Photosphere is not a .jpeg file. Please select a .jpeg file to be used as the photosphere.", "Please select both a valid photosphere and nadir.","Please select a save location."]
        # Displays a pop-up box informing the user of the error
        self.error_message = messagebox.showinfo(title="Error", message=messages[message_num])

# Runs the GUI
if __name__ == "__main__":
    root = Tk()
    root.title("Nadir Patch Tool")
    Editor_360(root)
    root.mainloop()
