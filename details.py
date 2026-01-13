from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import date, datetime
from tkcalendar import Calendar, DateEntry

class details_win:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1119x516+241+173")
        
        #=======================variables==========================
        self.details_Floor = StringVar()
        self.details_RoomNo = StringVar()
        self.details_RoomType = StringVar()
         #====================title==========================
        lbl_title = Label(self.root, text="Details", font=("times new roman", 30, "bold italic"),bg="midnightblue",fg="snow",bd=4, relief=RIDGE,anchor="w")
        lbl_title.place(x=0,y=0,width=1200,height=40)
        
         #======================logo===========================
        # img1 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\blue.jpg")
        # img1 = img1.resize((230,160),Image.Resampling.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img1)
       
        # lblimg =Label(self.root, image = self.photoimg2,bd=4,relief=RIDGE)
        # lblimg.place(x=0,y=0,width=180,height=40)
        
        #========================labelFrame=========================
        labelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", font=("times new roman", 15, "bold"),padx=2)
        labelFrameleft.place(x=0,y=41,width=500,height=380)
        
        #=======================labels and entries==========================
        #======Floor========
        lblFloor= Label(labelFrameleft, text="Floor", font=("times new roman", 12, "bold"),padx=3,pady=6)
        lblFloor.grid(row=1, column=0, sticky=W)     
        
        entry_Floor = ttk.Entry(labelFrameleft,textvariable=self.details_Floor,font=("Comic Sans MS", 12, "italic"), width=19)   
        entry_Floor.grid(row=1, column=1, padx=5, pady=6, sticky=W)
        
        #======Room No========
        lblRoomNO= Label(labelFrameleft, text="Room No.", font=("times new roman", 12, "bold"),padx=3,pady=6)
        lblRoomNO.grid(row=2, column=0, sticky=W)     
        
        entryRoomNo = ttk.Entry(labelFrameleft,textvariable=self.details_RoomNo,font=("Comic Sans MS", 12, "italic"), width=19)   
        entryRoomNo.grid(row=2, column=1, padx=5, pady=6, sticky=W)
        
        #======Room Type========
        lblRoomType= Label(labelFrameleft, text="Room Type",font=("times new roman", 12, "bold"),padx=3,pady=6)
        lblRoomType.grid(row=3, column=0, sticky=W)     
        
        entryRoomType = ttk.Combobox(labelFrameleft,textvariable=self.details_RoomType, font=("Comic Sans MS", 12, "italic"), width=20, state="readonly")
        entryRoomType["values"] = ("Single","Double","Luxury")
        entryRoomType.current(0)
        entryRoomType.grid(row=3, column=1, padx=5, pady=6, sticky=W) 
       
        
        #=======================================buttons============================================================================================
        btn_frame = Frame(labelFrameleft, bd=2)
        btn_frame.place(x=8,y=200,width=365,height=50)
        
        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnAdd.grid(row=0, column=0, padx=5, pady=5)
        
        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnUpdate.grid(row=0, column=1, padx=5, pady=5)
        
        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnDelete.grid(row=0, column=2, padx=5, pady=5)
        
        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnReset.grid(row=0, column=3, padx=5, pady=5)    
        
        #========================Table Frame=========================
        
        labelFrameRight = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 15, "bold italic"),padx=2)
        labelFrameRight.place(x=502,y=41,width=605,height=415)       
        
        scroll_x= Scrollbar(labelFrameRight, orient=HORIZONTAL)
        scroll_y= Scrollbar(labelFrameRight, orient=VERTICAL)
        
        self.room_table = ttk.Treeview(labelFrameRight, columns=("Floor","Room No.","Room Type"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)             
        
        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("Room No.", text="Room No.")
        self.room_table.heading("Room Type", text="Room Type")
      
        
        self.room_table["show"] = "headings"
        
        self.room_table.column("Floor", width=100)
        self.room_table.column("Room No.", width=100)
        self.room_table.column("Room Type", width=100)
 
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>")
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        
    #======================functions==========================    
    #Add Data 
    def add_data(self):
        if self.details_Floor.get() == "" or self.details_RoomNo.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)   
        else:  
            try:   
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (self.details_Floor.get(),
                                                                        self.details_RoomNo.get(),
                                                                        self.details_RoomType.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    #Fetch Data            
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()       
    #Get Cursor    
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        if row:
            self.details_Floor.set(row[0])
            self.details_RoomNo.set(row[1])
            self.details_RoomType.set(row[2])
            
    #Update Data
    def update(self):
        if self.details_Floor.get() == "" or self.details_RoomNo.get() == "" :
            messagebox.showerror("Error", "All fields are required",parent=self.root)   
        else:  
            try:   
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
                my_cursor = conn.cursor()
                my_cursor.execute("update detials set Floor=%s, Room_Type=%s, where Room_No=%s", (self.details_Floor.get(),
                                                                                                  self.details_RoomType.get(),
                                                                                                  self.details_RoomNo.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room booking details updated successfully",parent=self.root)      
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)  
                
    def mDelete(self): 
        mDelete = messagebox.askyesno("Delete", "Are you sure you want to delete this customer?", parent=self.root)    
        if mDelete > 0:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
                my_cursor = conn.cursor()
                query = "delete from details where Floor=%s and Room_No=%s and Room_type=%s"
                value=(self.details_Floor.get(), self.details_RoomNo.get(), self.details_RoomType.get())
                my_cursor.execute(query, value)
                messagebox.showinfo("Success", "Room booking details deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)   
        else:
            if not mDelete:
                return        
        conn.commit()
        self.fetch_data()
        conn.close()   
        
    def reset(self):
            self.details_Floor.set("")
            self.details_RoomNo.set("")   
            self.details_RoomType.set("")
            messagebox.showinfo("Reset", "All fields have been reset", parent=self.root)               

              
        
if __name__=="__main__":
    root=Tk()
    obj=details_win(root)
    root.mainloop()          
        