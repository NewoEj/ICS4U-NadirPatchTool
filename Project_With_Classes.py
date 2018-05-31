from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
from PIL import ImageGrab
from PIL import ImageTk
import os



class tkinter_edit(ttk.Frame):
    """Has the Attributes:
    
    
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

            def give_name(self):
                return self.name        
            
            def make_tkImage(self,wide, high):
                    self.pic = self.pic.resize((wide, high), Image.BICUBIC)
                    self.dim_x, self.dim_y = self.pic.size
                    tkImage = ImageTk.PhotoImage(self.pic)
                    return tkImage

        self.base_photo = photo()
        self.nadir = photo()
        self.save = ""
        self.save_name = ""
        self.final_pic = photo()
               
        self.master = ttk.Frame(parent, padding = "3 3 12 12")
        self.master.grid(column=0, row=0, sticky=(N, W, E, S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        
        ttk.Button(self.master, text = "Select Base Photo", command = lambda: self.base_photo.find_name()).grid(column=0, row=0, sticky = W)        
        ttk.Button(self.master, text = "Select Nadir", command = lambda: self.nadir.find_name()).grid(column=0,row=1,sticky=W)
        ttk.Button(self.master, text = "Edit Pictures", command = lambda: self.edit_photo()).grid(column=0,row=3,sticky=W)
        
        ttk.Label(self.master, textvariable = self.base_photo.name).grid(column=1, row=0, sticky = W)
        ttk.Label(self.master, textvariable = self.nadir.name).grid(column=1, row=1, sticky=W)

           
    def new_photo(self,name):
        name = photo()
    
    def edit_photo(self):
        new_path = os.path.join(self.save, self.save_name)
        self.app = edit_frame(self.base_photo, self.nadir, new_path) 
        
class edit_frame(Toplevel):
    def __init__(self, base_photo, nadir, save):
        try:
            self.save_location = save
            self.base = base_photo.make_tkImage(1000,500)
            self.nad = nadir.make_tkImage(1000,500)        
            self.edit = Toplevel()
            self.edit.title("Edit Photo")
            self.menu_bar = Menu(self.edit)
            self.menu_bar.add_command(label="Save", command =self.save_canvas)
            self.edit.config(menu = self.menu_bar)
            self.editor = Canvas(self.edit,width = base_photo.dim_x, height = base_photo.dim_y)
            self.editor.pack(expand = 1, fill = BOTH)
            self.i = self.editor.create_image(base_photo.dim_x/2, base_photo.dim_y/2, image = self.base)
            self.p = self.editor.create_image(base_photo.dim_x/2, base_photo.dim_y - base_photo.dim_y/2, image = self.nad)
        except:
            Error_Message()
        
        
    def save_canvas(self):
        self.editor.postscript(file = "finish")
        img = Image.open("finish")
        filename = filedialog.asksaveasfilename(defaultextension = ".jpg")
        try:
            img.save(filename)
        except:
            Error_Message()
            
class Error_Message(Toplevel):
    def __init__(self):
        self.error_screen = Toplevel()
        self.error_screen.title("Error")
        self.x = (self.error_screen.winfo_screenwidth() / 2) - 100
        self.y = (self.error_screen.winfo_screenheight() / 2) -25
        self.error_screen.geometry('%dx%d+%d+%d' % (200,50, self.x,self.y))
        self.error_message = ttk.Label(self.error_screen, text = "Invalid Option")
        self.error_message.config(font=("Times New Romans",25))
        self.error_message.pack()
        self.error_screen.grab_set()
        self.error_screen.focus()
        
if __name__ == "__main__":
    root = Tk()
    tkinter_edit(root)
    root.mainloop()


