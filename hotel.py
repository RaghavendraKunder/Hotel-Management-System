from tkinter import *
from PIL import Image,ImageTk  #pip install pillow
from customtkinter import *
from developers import dev_win
from customer import Cust_win

class HotelManagementSystem:
    def __init__(self, root):
       self.root=root
       self.root.title("Hotel Management System")
       self.root.geometry("1550x800+0+0")
       
       
       #======================1st img===========================
       img1 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\hotellogo1.png")
       img1 = img1.resize((1320,160),Image.Resampling.LANCZOS)
       self.photoimg1 = ImageTk.PhotoImage(img1)
       
       lblimg =Label(self.root, image = self.photoimg1,bd=4,relief=RIDGE)
       lblimg.place(x=230,y=0,width=1320,height=160)
       
        #======================2nd img===========================
       img2 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\hotellogo1.png")
       img2 = img2.resize((230,160),Image.Resampling.LANCZOS)
       self.photoimg2 = ImageTk.PhotoImage(img2)
       
       lblimg =Label(self.root, image = self.photoimg2,bd=4,relief=RIDGE)
       lblimg.place(x=0,y=0,width=230,height=160) 
       
       #=======================title===============================
       lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 30, "bold italic"),bg="midnightblue",fg="snow",bd=4, relief=RIDGE)
       lbl_title.place(x=0,y=160,width=1550,height=50)
       
       #=======================main frame==========================
       main_frame = Frame(self.root,bd=4,relief=RIDGE)
       main_frame.place(x=0,y=210,width=1550,height=620) 
       
       #=======================menu================================
       lbl_menu = Label(main_frame,text="MENU", font=("times new roman", 20, "bold"),bg="black",fg="snow",bd=4, relief=FLAT)
       lbl_menu.place(x=0,y=0,width=235,height=45) 
       
       #=======================btn frame==========================
       btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
       btn_frame.place(x=1,y=45,width=235,height=190)
       
       cust_btn=Button(btn_frame,text="Customer", command=self.Cust_win, width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       cust_btn.grid(row=0,column=0,pady=1)    
       
       room_btn=Button(btn_frame,text="Room", width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       room_btn.grid(row=1,column=0,pady=1) 
       
       details_btn=Button(btn_frame,text="Details", width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       details_btn.grid(row=2,column=0,pady=1) 
       
       report_btn=Button(btn_frame,text="Developers",command=self.dev_details, width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       report_btn.grid(row=3,column=0,pady=1)
       
       logout_btn=Button(btn_frame,text="Logout", width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       logout_btn.grid(row=4,column=0,pady=1)
       
       #=======================Rightside image=============================
       img3 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\hotel4.png")
       img3 = img3.resize((1119,480),Image.Resampling.LANCZOS)
       self.photoimg3 = ImageTk.PhotoImage(img3)
       
       lblimg =Label(main_frame, image = self.photoimg3,bd=4,relief=RIDGE)
       lblimg.place(x=236,y=0,width=1119,height=480)
       
       #===========================side img=================================
       img4 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\hotel5.png")
       img4 = img4.resize((236,125),Image.Resampling.LANCZOS)
       self.photoimg4 = ImageTk.PhotoImage(img4)
       
       lblimg =Label(main_frame, image = self.photoimg4,bd=4,relief=RIDGE)
       lblimg.place(x=0,y=235,width=236,height=125)
       
       img5 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\hotel6.png")
       img5 = img5.resize((236,125),Image.Resampling.LANCZOS)
       self.photoimg5 = ImageTk.PhotoImage(img5)
       
       lblimg =Label(main_frame, image = self.photoimg5,bd=4,relief=RIDGE)
       lblimg.place(x=0,y=360,width=236,height=125)
       
       
       
    def dev_details(self):
        self.new_window=Toplevel(self.root)  
        self.app=dev_win(self.new_window) 
        
    def Cust_win(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)
       
           
if __name__=="__main__":       
 root = Tk()
 obj = HotelManagementSystem(root)
 root.mainloop()