from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow



class dev_win:
    def __init__(self,root):
        self.root = root
        self.root.title("DEVELOPERS")
        self.root.geometry("1119x447+241+244")
        
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\admin\OneDrive\Desktop\Hotel Management System\images\dev.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="snow")
        frame.place(x=150,y=60,width=840,height=340)
        
        Devlopers=lbl=Label(frame,text="DEVELOPERS",font=("Helvatica",18,"bold italic underline"),fg="black",bg="snow")
        Devlopers.place(x=15,y=15)
       #============================     
        Raghav=lbl=Label(frame,text="2.) 33. RAGHAVENDRA KUNDER",font=("Helvatica",14,"bold italic "),fg="black",bg="snow")
        Raghav.place(x=20,y=105)
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    app=dev_win(root)
    root.mainloop()      
        