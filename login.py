from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector
from developers import dev_win
from customer import Cust_win

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()







class Login_window:
    
    
    
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.var_email=StringVar()
        self.var_password=StringVar()
        
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\beach1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=525,y=130,width=340,height=450)
        
        img1=Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\login1.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=652,y=135,width=98,height=98)
        
        get_str=Label(frame,text="GET STARTED", font=("times new roman",15,"bold italic"),fg="snow",bg="black")
        get_str.place(x=105,y=100)
        
        #Label
        username=lbl=Label(frame,text="USERNAME",font=("Helvatica",10,"bold italic"),fg="snow",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("Helvatica",10,"bold italic"))
        self.txtuser.place(x=40,y=175,width=270)

        password=lbl=Label(frame,text="PASSWORD",font=("Helvatica",10,"bold italic"),fg="snow",bg="black")
        password.place(x=70,y=245)
        
        self.txtpass=ttk.Entry(frame,font=("Helvatica",10,"bold italic"))
        self.txtpass.place(x=40,y=265,width=270)
        
        #icon images
        img2=Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\admin1.png")
        img2=img2.resize((30,30),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(frame,image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=40,y=145,width=30,height=30)
        
        img3=Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\pass1.png")
        img3=img3.resize((30,30),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(frame,image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=40,y=235,width=30,height=30)
        
        #Login btn
        loginbtn=Button(frame,command=self.login,text="LOGIN",font=("Helvatica",10,"bold italic"),bd=3,relief=RIDGE,fg="snow",bg="red",activeforeground="snow",activebackground="red",cursor="hand2")
        loginbtn.place(x=115,y=300,width=120,height=35)
        
        #Register btn
        registerbtn=Button(frame,text="NEW USER REGISTER",command=self.register_window,font=("Helvatica",8,"bold italic"),borderwidth=0,fg="snow",bg="black",activeforeground="snow",activebackground="black",cursor="hand2")
        registerbtn.place(x=12,y=350,width=170,height=35)
        
        #forget pass
        forgetbtn=Button(frame,text="FORGET PASSWORD",command=self.forgot_password_window,font=("Helvatica",8,"bold italic"),borderwidth=0,fg="snow",bg="black",activeforeground="snow",activebackground="black",cursor="hand2")
        forgetbtn.place(x=12,y=390,width=170,height=35)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)    
        
    def login(self):
            if self.txtuser.get()=="" or self.txtpass.get()=="":
                messagebox.showerror("ERROR","all field required")
            elif self.txtuser.get()=="Kapu" and self.txtpass.get()=="ashu":
                    messagebox.showinfo("Login successful","Welcome")
            else:
               conn=mysql.connector.connect(host="localhost",user="raghav",password="Sujat@1972",database="management")
               my_cur=conn.cursor()  
               my_cur.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                       ))  
               row=my_cur.fetchone() 
               if row is None:
                   messagebox.showerror("ERROR","Inavalid Username or Password")
               else:
                   open_main=messagebox.askyesno("YES/NO","Access only admin")
                   if open_main>0:
                       self.new_window=Toplevel(self.root)
                       self.app=HotelManagementSystem(self.new_window)
                   else:
                       if not open_main:
                           return
            conn.commit()
            conn.close()             
    
    #reset password
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("ERROR","Select security question",parent=self.root2)
        elif self.txt_security_ans.get()=="":
            messagebox.showerror("ERROR","Please enter answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("ERROR","Please enter new password",parent=self.root2)     
        else:  
            conn=mysql.connector.connect(host="localhost",user="raghav",password="Sujat@1972",database="management")
            my_cur=conn.cursor()
            qury=("select * from register where email=%s and security_Q=%s and security_ans=%s")     
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_ans.get(),)
            my_cur.execute(qury,value)
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("ERROR","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cur.execute(query,value)  
                
                conn.commit()
                conn.close()
                messagebox.showinfo("INFO","Your password has been reset, please login new password",parent=self.root2)  
                self.root2.destroy()      
    
    
    
    
    
    
    
    #forgot password
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("ERROR","Please enter the E-mail address to reset password")
        else:  
            conn=mysql.connector.connect(host="localhost",user="raghav",password="Sujat@1972",database="management")
            my_cur=conn.cursor() 
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            #print(row) 
            
            if row==None:
                messagebox.showerror("ERROR","Please eneter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("FORGOT PASSWORD")
                self.root2.geometry("340x450+525+130") 
                
                l=Label(self.root2,text="FORGOT PASSWORD", font=("Arial",15,"bold italic"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1) 
                
                security_Q=Label(self.root2,text="SECURITY QUESTION",font=("helvatica",11,"bold italic"),bg="snow")
                security_Q.place(x=50,y=80)
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("helvatica",11,"bold italic "),state="readonly")
                self.combo_security_Q ["values"]=("Select","your birth place","your mother's name","your pet name") 
                self.combo_security_Q.place(x=50,y=110,width=260)
                self.combo_security_Q.current(0)
                
                
                security_ans=Label(self.root2,text="SECURITY ANSWER",font=("helvatica",11,"bold italic"),bg="snow")
                security_ans.place(x=50,y=165)
                
                self.txt_security_ans=ttk.Entry(self.root2,font=("helvatica",11,"bold italic "))
                self.txt_security_ans.place(x=50,y=195,width=260) 
                
                new_password=Label(self.root2,text="NEW PASSWORD",font=("helvatica",11,"bold italic"),bg="snow")
                new_password.place(x=50,y=250)
                
                self.txt_new_password=ttk.Entry(self.root2,font=("helvatica",11,"bold italic "))
                self.txt_new_password.place(x=50,y=280,width=260) 
                
                btn=Button(self.root2,text="RESET",command=self.reset_password,font=("helvatica",13,"bold italic "),fg="snow",bg="#228B22")
                btn.place(x=140,y=335) 
        
        
        
        
        
        
                    
                
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_ans=StringVar()
        self.var_password=StringVar()
        self.var_c_password=StringVar()
        
        #background image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\mountain1.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1) 
        
        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\left1.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=90,y=100,width=332,height=445)  
        
        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=422,y=100,width=800,height=445)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("helvatica",20,"bold italic underline"),fg="darkgreen",bg="snow")
        register_lbl.place(x=20,y=20)
        
        #label & entry
        #1st row
        fname=Label(frame,text="FIRST NAME",font=("helvatica",12,"bold italic"),bg="snow")
        fname.place(x=50,y=80)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("helvatica",12,"bold italic "))
        self.fname_entry.place(x=50,y=110,width=320)
        
        
        lname=Label(frame,text="LAST NAME",font=("helvatica",12,"bold italic"),bg="snow")
        lname.place(x=410,y=80)
        
        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("helvatica",12,"bold italic "))
        self.lname_entry.place(x=410,y=110,width=320)
        
        #2nd row
        contact=Label(frame,text="CONTACT",font=("helvatica",12,"bold italic"),bg="snow")
        contact.place(x=50,y=160)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("helvatica",12,"bold italic "))
        self.txt_contact.place(x=50,y=190,width=320)
        
        
        email=Label(frame,text="E-MAIL",font=("helvatica",12,"bold italic"),bg="snow")
        email.place(x=410,y=160)
        
        self.email=ttk.Entry(frame,textvariable=self.var_email,font=("helvatica",12,"bold italic "))
        self.email.place(x=410,y=190,width=320)
        
         #3rd row
        security_Q=Label(frame,text="SECURITY QUESTION",font=("helvatica",12,"bold italic"),bg="snow")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("helvatica",12,"bold italic "),state="readonly")
        self.combo_security_Q ["values"]=("Select","your birth place","your mother's name","your pet name") 
        self.combo_security_Q.place(x=50,y=270,width=320)
        self.combo_security_Q.current(0)
        
        
        security_ans=Label(frame,text="SECURITY ANSWER",font=("helvatica",12,"bold italic"),bg="snow")
        security_ans.place(x=410,y=240)
        
        self.txt_security_ans=ttk.Entry(frame,textvariable=self.var_security_ans,font=("helvatica",12,"bold italic "))
        self.txt_security_ans.place(x=410,y=270,width=320)
        
         #4th row
        password=Label(frame,text="PASSWORD",font=("helvatica",12,"bold italic"),bg="snow")
        password.place(x=50,y=320)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("helvatica",12,"bold italic "))
        self.txt_password.place(x=50,y=350,width=320)
        
        
        c_password=Label(frame,text="CONFIRM PASSWORD",font=("helvatica",12,"bold italic"),bg="snow")
        c_password.place(x=410,y=320)
        
        self.txt_c_password=ttk.Entry(frame,textvariable=self.var_c_password,font=("helvatica",12,"bold italic "))
        self.txt_c_password.place(x=410,y=350,width=320)
        
        #checkbutton
        self.var_checkbtn=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_checkbtn,text="I Agree with the Terms & Condition",font=("helvatica",10,"bold italic "),bg="snow",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=385)
        
        
        #buttons
        img1=Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\register1.png")
        img1=img1.resize((30,40),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimage,bg="black",borderwidth=0)
        lblimg1.place(x=410,y=385,width=30,height=40)
        b1=Button(frame,text="REGISTER",command=self.register_data,font=("Helvatica",10,"bold italic"),bd=3,relief=RIDGE,fg="snow",bg="red",activeforeground="snow",activebackground="red",cursor="hand2")
        b1.place(x=442,y=385,width=77,height=40)
        
        
        img2=Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\login2.png")
        img2=img2.resize((35,35),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img2)
        lblimg2=Label(frame,image=self.photoimage1,bg="black",borderwidth=0)
        lblimg2.place(x=550,y=388,width=35,height=35)
        b2=Button(frame,command=self.return_login,text="LOGIN",font=("Helvatica",10,"bold italic"),bd=3,relief=RIDGE,fg="snow",bg="red",activeforeground="snow",activebackground="red",cursor="hand2")
        b2.place(x=590,y=385,width=77,height=40)
        
        
    #function declaration
    
    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()=="" or self.var_security_Q.get()=="Select":
           messagebox.showerror("ERROR","All fields are required") 
        elif self.var_password.get()!=self.var_c_password.get():
            messagebox.showerror("ERROR","Password and Confirm Password must be same")   
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("ERROR","Please agree Terms & Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sujat@1972",database="management")
            my_cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","User already exist, please try another E-mail")
            else:
                my_cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                     self.var_fname.get(),
                                                                                     self.var_lname.get(),
                                                                                     self.var_contact.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_security_Q.get(),
                                                                                     self.var_security_ans.get(),
                                                                                     self.var_password.get()
                                                                                    ))   
            conn.commit()
            conn.close()
            messagebox.showinfo("SUCCESS","Register Successfully") 
            
            
    def return_login(self):
        self.root.destroy()                             
                
 
 
class HotelManagementSystem:
    def __init__(self, root):
       self.root=root
       self.root.title("Hotel Management System")
       self.root.geometry("1550x800+0+0")
       
       
       #======================1st img===========================
       img1 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\hotell1.png")
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
       
       cust_btn=Button(btn_frame,text="Customer", command=self.customer_details, width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       cust_btn.grid(row=0,column=0,pady=1)    
       
       room_btn=Button(btn_frame,text="Room", width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       room_btn.grid(row=1,column=0,pady=1) 
       
       details_btn=Button(btn_frame,text="Details", width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       details_btn.grid(row=2,column=0,pady=1) 
       
       report_btn=Button(btn_frame,text="Developers",command=self.dev_details, width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
       report_btn.grid(row=3,column=0,pady=1)
       
       logout_btn=Button(btn_frame,text="Logout",command=self.return_login1, width=20,font=("times new roman", 14, "bold"),bg="#473C8B",fg="#87CEEb",bd=0,cursor="hand2",relief=RIDGE,activebackground="#6A5ACD",activeforeground="black")
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
    
    def return_login1(self):
        self.root.destroy() 
        
    def dev_details(self):
        self.new_window=Toplevel(self.root)  
        self.app=dev_win(self.new_window)    
    
    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)        


if __name__ =="__main__":
    main()