from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk


class tkinter_edit(ttk.Frame):
    """Has the Attributes:
    
    Base_Photo
    Nadir
    
    
    """
    
    def __init__(self,parent):
        class photo(object):
            """ Has the Attributes:

            Image Name
            Size
            
            """
            def __init__(self):
                self.name = ""
        
            def find_name(self):
                try:
                    self.name = filedialog.askopenfilename()
                    self.pic = Image.open(self.name)
                    self.dim_x, self.dim_y = self.pic.size
                except:
                    Error_Message()       
            
            def make_tkImage(self,wide, high):
                self.pic = self.pic.resize((wide, high), Image.BICUBIC)
                tkImage = ImageTk.PhotoImage(self.pic)
                return tkImage
            
            def resize_image(self,wide, high):
                self.pic = self.pic.resize((wide,high), Image.BICUBIC)

        self.base_photo = photo()
        self.nadir = photo()
               
        self.master = ttk.Frame(parent, padding = "10")
        self.master.grid(column=0, row=0)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        
        ttk.Button(self.master, text = "Select Photosphere", command = lambda: self.base_photo.find_name()).grid(column=0,row=1,pady=10)        
        ttk.Button(self.master, text = "Select Nadir", command = lambda: self.nadir.find_name()).grid(column=0,row=2,pady=10)
        ttk.Button(self.master, text = "Preview", command = lambda: self.preview_photo()).grid(column=0,row=3,pady=10)
        ttk.Button(self.master, text = "Save", command = lambda: self.save_photo()).grid(column=0,row=4,pady=10)
        ttk.Button(self.master, text = "Quit Program", command = exit).grid(column=0,row=5,padx=10,pady=10)
        
        ttk.Label(self.master, textvariable = self.base_photo.name).grid(column=1, row=1, sticky = W)
        ttk.Label(self.master, textvariable = self.nadir.name).grid(column=1, row=2, sticky=W)
        ttk.Label(self.master, text = "Nadir Patch Tool", font=("Arial", 20)).grid(column=0,row=0)
    
    def preview_photo(self):
        self.app = Preview_360(self.base_photo, self.nadir)
        
    def save_photo(self):
        self.base_photo.resize_image(self.base_photo.dim_x,self.base_photo.dim_y)
        self.nadir.resize_image(self.base_photo.dim_x, self.base_photo.dim_y)
        self.base_photo.pic.paste(self.nadir.pic,(0,0),self.nadir.pic)
        filename = filedialog.asksaveasfilename(defaultextension = ".jpg")
        try:
            self.base_photo.pic.save(filename)
        except:
            Error_Message()        
          
class Preview_360(Toplevel):
    def __init__(self, base_photo, nadir):
        back_img = Image.open(base_photo)
        nad = Image.open(nadir)
        back_img.paste(nad,(0,0),nad)
        tkimage = ImageTk.PhotoImage(back_img)
        panel1 = Label(root,image = tkimage)
        panel1.pack()
        
        
            
class Error_Message(Toplevel):
    def __init__(self):
        self.error_message = messagebox.showinfo(title="Error", message="Invalid Option")
        
if __name__ == "__main__":
    root = Tk()
    root.title("Nadir Patch Tool")
    tkinter_edit(root)
    root.mainloop()


