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
                self.name = filedialog.askopenfilename()
                self.pic = Image.open(self.name)
                self.dim_x, self.dim_y = self.pic.size

            def give_name(self):
                return self.name        
            
            def make_tkImage(self,wide, high):
                self.pic.thumbnail((wide, high), Image.BICUBIC)
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
        self.save_location = save
        self.base = base_photo.make_tkImage(1000,500)
        self.nad = nadir.make_tkImage(100,50)        
        self.edit = Toplevel()
        self.edit.title("Edit Photo")
        self.editor = Canvas(self.edit,width = base_photo.dim_x, height = base_photo.dim_y)
        self.editor.pack(expand = 1, fill = BOTH)
        self.old_x = base_photo.dim_x/2
        self.old_y = base_photo.dim_y/2
        self.i = self.editor.create_image(base_photo.dim_x/2, base_photo.dim_y/2, image = self.base)
        self.p = self.editor.create_image(base_photo.dim_x/2, base_photo.dim_y/2, image = self.nad)
        self.editor.bind("<Button 1>", self.new_coord)
        self.edit.bind('s', self.save_canvas)
        
    def new_coord(self, eventorigin):
        self.new_x = eventorigin.x
        self.new_y = eventorigin.y
        self.x = self.new_x - self.old_x 
        self.y = self.new_y - self.old_y 
        self.editor.move(self.p,self.x,self.y)
        self.old_y = self.new_y
        self.old_x = self.new_x
        
    def save_canvas(self,eventorigin):
        self.editor.postscript(file = "finish")
        img = Image.open("finish")
        filename = filedialog.asksaveasfilename(defaultextension = ".jpg")
        img.save(filename)
        
if __name__ == "__main__":
    root = Tk()
    tkinter_edit(root)
    root.mainloop()


