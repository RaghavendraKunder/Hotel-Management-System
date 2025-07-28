from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector



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
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\admin\OneDrive\Desktop\Hotel Management System\images\mountain1.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1) 
        
        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\admin\OneDrive\Desktop\Hotel Management System\images\left1.png")
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
        img1=Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel Management System\images\register1.png")
        img1=img1.resize((30,40),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimage,bg="black",borderwidth=0)
        lblimg1.place(x=410,y=385,width=30,height=40)
        b1=Button(frame,text="REGISTER",command=self.register_data,font=("Helvatica",10,"bold italic"),bd=3,relief=RIDGE,fg="snow",bg="red",activeforeground="snow",activebackground="red",cursor="hand2")
        b1.place(x=442,y=385,width=77,height=40)
        
        
        img2=Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel Management System\images\login2.png")
        img2=img2.resize((35,35),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img2)
        lblimg2=Label(frame,image=self.photoimage1,bg="black",borderwidth=0)
        lblimg2.place(x=550,y=388,width=35,height=35)
        b2=Button(frame,text="LOGIN",font=("Helvatica",10,"bold italic"),bd=3,relief=RIDGE,fg="snow",bg="red",activeforeground="snow",activebackground="red",cursor="hand2")
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
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()