from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import date, datetime
from tkcalendar import Calendar, DateEntry

class room_win:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1119x516+241+173")
        
        #============================variables=================================
        
        self.room_Contacts= StringVar()
        self.room_Checkin= StringVar()
        self.room_Checkout = StringVar()
        self.room_roomtype = StringVar()
        self.room_availableroom = StringVar()
        self.room_noOfdays = StringVar()
        self.room_paidtax = StringVar()
        self.room_roomfee = StringVar()
        self.room_totalfee = StringVar()
        
        #====================title==========================
        lbl_title = Label(self.root, text="Room Booking Details", font=("times new roman", 30, "bold italic"),bg="midnightblue",fg="snow",bd=4, relief=RIDGE,anchor="w")
        lbl_title.place(x=369,y=0,width=1119,height=40)
        
         #======================logo===========================
        img1 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\blue.jpg")
        img1 = img1.resize((230,160),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
       
        lblimg =Label(self.root, image = self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=180,height=40)
        
        #========================labelFrame=========================
        labelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", font=("times new roman", 15, "bold"),padx=2)
        labelFrameleft.place(x=0,y=1,width=368,height=514)
        
        #=======================labels and entries==========================
        #======Customer Contact========
        cust_contact = Label(labelFrameleft, text="Customer Contact", font=("times new roman", 12, "bold"),padx=2,pady=6)
        cust_contact.grid(row=1, column=0, sticky=W)     
        
        entry_contact = ttk.Entry(labelFrameleft,textvariable=self.room_Contacts,font=("Comic Sans MS", 12, "italic"), width=13)   
        entry_contact.grid(row=1, column=1, padx=5, pady=6, sticky=W)
        
        #=======fetch data button========
        btnFetchData = Button(labelFrameleft, command=self.fetchData, text="fetch Data",font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=9)
        btnFetchData.place(x=270,y=4)
        
        #======Check_in Date========
        Check_in_date = Label(labelFrameleft, text="Check in Date", font=("times new roman", 12, "bold"),padx=2,pady=6)
        Check_in_date.grid(row=2, column=0, sticky=W)     
        
        self.entry_CheckIn = DateEntry(labelFrameleft,textvariable=self.room_Checkin,date_pattern='dd/mm/yyyy',mindate=date.today(),width=22)   
        self.entry_CheckIn.grid(row=2, column=1, padx=5, pady=6, sticky=W)
        # when check-in changes, set checkout's min date and recalc
        self.entry_CheckIn.bind("<<DateEntrySelected>>", lambda e: (self.entry_Checkout.config(mindate=self.entry_CheckIn.get_date()), self.total()))

        
        #======Check_out Date========
        Check_out_date = Label(labelFrameleft, text="Check Out Date", font=("times new roman", 12, "bold"),padx=2,pady=6)
        Check_out_date.grid(row=3, column=0, sticky=W)     
        
        self.entry_Checkout = DateEntry(labelFrameleft,textvariable=self.room_Checkout,date_pattern='dd/mm/yyyy', mindate=date.today(), width=22)   
        self.entry_Checkout.grid(row=3, column=1, padx=5, pady=6, sticky=W)
        self.entry_Checkout.bind("<<DateEntrySelected>>", lambda e: self.total())
        
        #======Room type combobox========
        roomType = Label(labelFrameleft, text="Id Proof", font=("times new roman", 12, "bold"),padx=2,pady=6)
        roomType.grid(row=4, column=0, sticky=W)     
        
        conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
        my_cursor = conn.cursor()
        my_cursor.execute("select Room_Type from details")
        rows1 = my_cursor.fetchall()
        combo_roomType = ttk.Combobox(labelFrameleft,textvariable=self.room_roomtype, font=("Comic Sans MS", 12, "italic"), width=20, state="readonly")
        combo_roomType["values"] = rows1
        combo_roomType.current(0)
        combo_roomType.grid(row=4, column=1, padx=5, pady=6, sticky=W)
              
        #======Available room========
        Available_room = Label(labelFrameleft, text="Available Room", font=("times new roman", 12, "bold"),padx=2,pady=6)
        Available_room.grid(row=5, column=0, sticky=W)     
        
        # entry_AvailableRoom = ttk.Entry(labelFrameleft,textvariable=self.room_availableroom, font=("Comic Sans MS", 12, "italic"), width=22)   
        # entry_AvailableRoom.grid(row=5, column=1, padx=5, pady=6, sticky=W)
        conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
        my_cursor = conn.cursor()
        my_cursor.execute("select Room_No from details")
        rows2 = my_cursor.fetchall()
        entry_roomNo = ttk.Combobox(labelFrameleft,textvariable=self.room_availableroom, font=("Comic Sans MS", 12, "italic"), width=20, state="readonly")
        entry_roomNo["values"] = rows2
        entry_roomNo.current(0)
        entry_roomNo.grid(row=5, column=1, padx=5, pady=6, sticky=W)
        #======No Of Days========
        No_of_days = Label(labelFrameleft, text="No of days", font=("times new roman", 12, "bold"),padx=2,pady=6)
        No_of_days.grid(row=6, column=0, sticky=W)     
        
        entry_noOfDays = ttk.Entry(labelFrameleft,textvariable=self.room_noOfdays, font=("Comic Sans MS", 12, "italic"), width=22)   
        entry_noOfDays.grid(row=6, column=1, padx=5, pady=6, sticky=W)
        
        #======Paid Tax========
        Paid_Tax = Label(labelFrameleft, text="Paid Tax", font=("times new roman", 12, "bold"),padx=2,pady=6)
        Paid_Tax.grid(row=7, column=0, sticky=W)     
        
        entry_paidTax = ttk.Entry(labelFrameleft,textvariable=self.room_paidtax, font=("Comic Sans MS", 12, "italic"), width=22)   
        entry_paidTax.grid(row=7, column=1, padx=5, pady=6, sticky=W) 
        
        #======Room Fee========
        Room_Fee = Label(labelFrameleft, text="Room Fee", font=("times new roman", 12, "bold"),padx=2,pady=6)
        Room_Fee.grid(row=8, column=0, sticky=W)     
        
        entry_roomFee = ttk.Entry(labelFrameleft,textvariable=self.room_roomfee, font=("Comic Sans MS", 12, "italic"), width=22)   
        entry_roomFee.grid(row=8, column=1, padx=5, pady=6, sticky=W)
        
        #======Total Cost========
        Total_Cost = Label(labelFrameleft, text="Total Cost", font=("times new roman", 12, "bold"),padx=2,pady=6)
        Total_Cost.grid(row=9, column=0, sticky=W)     
        
        entry_totalCost = ttk.Entry(labelFrameleft,textvariable=self.room_totalfee, font=("Comic Sans MS", 12, "italic"), width=22)   
        entry_totalCost.grid(row=9, column=1, padx=5, pady=6, sticky=W)
        
        btnBill = Button(labelFrameleft, text="Bill",command=self.total, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnBill.grid(row=10, column=0, padx=5, pady=5)
        
        #=======================================buttons============================================================================================
        btn_frame = Frame(labelFrameleft, bd=2)
        btn_frame.place(x=-4,y=435,width=365,height=50)
        
        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnAdd.grid(row=0, column=0, padx=5, pady=5)
        
        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnUpdate.grid(row=0, column=1, padx=5, pady=5)
        
        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnDelete.grid(row=0, column=2, padx=5, pady=5)
        
        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnReset.grid(row=0, column=3, padx=5, pady=5)
        
        #========================Table Frame=========================
        
        labelFrameRight = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 15, "bold italic"),padx=2)
        labelFrameRight.place(x=369,y=215,width=745,height=295)   
        
        searchBy = Label(labelFrameRight, text="Search By", font=("times new roman", 12, "bold italic"),bg="midnightblue",fg="snow",padx=2,pady=2)
        searchBy.grid(row=0, column=0, padx=0, pady=6, sticky=W)
        
        self.searchVar = StringVar()
        combo_searchBy = ttk.Combobox(labelFrameRight,textvariable=self.searchVar, font=("Comic Sans MS", 12, "bold italic"), width=20, state="readonly")
        combo_searchBy["values"] = ("Contacts","Room")
        combo_searchBy.current(0)
        combo_searchBy.grid(row=0, column=1, padx=0, pady=6, sticky=W) 
        
        self.srchField = StringVar()
        searchField = ttk.Entry(labelFrameRight,textvariable=self.srchField, font=("Comic Sans MS", 12, "italic"), width=22)   
        searchField.grid(row=0, column=2, padx=4, pady=6, sticky=W)
        
        btnSearch = Button(labelFrameRight, text="Search",command=self.searchData, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnSearch.grid(row=0, column=3, padx=2, pady=2)
        
        btnShowall = Button(labelFrameRight, text="Show All", font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnShowall.grid(row=0, column=4, padx=2, pady=2)
        
        #========================Show Data Table=========================
        labelFrametable = Frame(labelFrameRight, bd=2, relief=RIDGE,padx=2)
        labelFrametable.place(x=0,y=41,width=737,height=400) 
        
        scroll_x= Scrollbar(labelFrametable, orient=HORIZONTAL)
        scroll_y= Scrollbar(labelFrametable, orient=VERTICAL)
        
        self.room_table = ttk.Treeview(labelFrametable, columns=("Contacts","Checkin","Checkout","roomtype","availableroom","noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("Contacts", text="Contacts")
        self.room_table.heading("Checkin", text="Check In Date")
        self.room_table.heading("Checkout", text="Check Out Date")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("availableroom", text="Available Room")
        self.room_table.heading("noofdays", text="No Of Days")
        
        self.room_table["show"] = "headings"
        
        self.room_table.column("Contacts", width=100)
        self.room_table.column("Checkin", width=100)
        self.room_table.column("Checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("availableroom", width=100)
        self.room_table.column("noofdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>")
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()    
        
        
        
        
        
        
        
    def fetchData(self):
        if self.room_Contacts.get() == "":
            messagebox.showerror("Error", "Please enter contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")
            my_cursor = conn.cursor()
            query = "select name from customer WHERE mobile=%s"
            value = (self.room_Contacts.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error", "This contact number not found", parent=self.root)
            else:  
                conn.commit()
                conn.close()
            #======================Name=======================================    
                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=369, y=40, width=360, height=170)
                
                lblName = Label(showDataFrame, text="Name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblName.grid(row=0, column=0, sticky=W)
                
                lbl = Label(showDataFrame, text=row, font=("times new roman", 12, "bold"), padx=2, pady=6)    
                lbl.grid(row=0, column=1, sticky=W)
                
            #======================Gender========================================
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")
                my_cursor = conn.cursor()
                query = "select gender from customer WHERE mobile=%s"
                value = (self.room_Contacts.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblGender = Label(showDataFrame, text="Gender:", font=("times new roman", 12, "bold") , padx=2, pady=6)
                lblGender.grid(row=1, column=0, sticky=W)
                
                lbl2 = Label(showDataFrame, text=row, font=("times new roman", 12, "bold"), padx=2, pady=6)
                lbl2.grid(row=1, column=1, sticky=W)
                
            #======================email========================================
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")
                my_cursor = conn.cursor()
                query = "select email from customer WHERE mobile=%s"
                value = (self.room_Contacts.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblEmail = Label(showDataFrame, text="Email:", font=("times new roman", 12, "bold") , padx=2, pady=6)
                lblEmail.grid(row=2, column=0, sticky=W)
                
                lbl3 = Label(showDataFrame, text=row, font=("times new roman", 12, "bold"), padx=2, pady=6)
                lbl3.grid(row=2, column=1, sticky=W) 
                
            #======================Gender========================================
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")
                my_cursor = conn.cursor()
                query = "select country from customer WHERE mobile=%s"
                value = (self.room_Contacts.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblNationality = Label(showDataFrame, text="Nationality:", font=("times new roman", 12, "bold") , padx=2, pady=6)
                lblNationality.grid(row=3, column=0, sticky=W)
                
                lbl4 = Label(showDataFrame, text=row, font=("times new roman", 12, "bold"), padx=2, pady=6)
                lbl4.grid(row=3, column=1, sticky=W)    
                
            #======================Gender========================================
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")
                my_cursor = conn.cursor()
                query = "select address from customer WHERE mobile=%s"
                value = (self.room_Contacts.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblAddress = Label(showDataFrame, text="Address:", font=("times new roman", 12, "bold") , padx=2, pady=6)
                lblAddress.grid(row=4, column=0, sticky=W)
                
                lbl5 = Label(showDataFrame, text=row, font=("times new roman", 12, "bold"), padx=2, pady=6)
                lbl5.grid(row=4, column=1, sticky=W)           
            
                      
    def add_data(self):
        if self.room_Contacts.get() == "" or self.room_Checkin.get() == "" or self.room_Checkout.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)   
        else:  
            try:   
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
                my_cursor = conn.cursor()
                # check duplicate primary key (Available_room) before insert
                my_cursor.execute("select Available_room from room where Available_room=%s", (self.room_availableroom.get(),))
                if my_cursor.fetchone() is not None:
                    messagebox.showerror("Error", "Available Room value already exists. Choose a different value.", parent=self.root)
                    conn.close()
                    return

                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s)", (self.room_Contacts.get(),
                                                                                self.room_Checkin.get(),
                                                                                self.room_Checkout.get(),
                                                                                self.room_roomtype.get(),
                                                                                self.room_availableroom.get(),
                                                                                self.room_noOfdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room booked succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)    
                
    def update(self):
        if self.room_Contacts.get() == "" or self.room_Checkin.get() == "" :
            messagebox.showerror("Error", "All fields are required",parent=self.root)   
        else:  
            try:   
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
                my_cursor = conn.cursor()
                my_cursor.execute("update room set Checkin=%s, Checkout=%s, Roomtype=%s, Available_room=%s, No_of_days=%s where Contacts=%s", (
                                                                                                                                                self.room_Checkin.get(),
                                                                                                                                                self.room_Checkout.get(),
                                                                                                                                                self.room_roomtype.get(),
                                                                                                                                                self.room_availableroom.get(),
                                                                                                                                                self.room_noOfdays.get(),
                                                                                                                                                self.room_Contacts.get()))
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
                query = "delete from room where Contacts=%s and Checkin=%s and Checkout=%s"
                value=(self.room_Contacts.get(), self.room_Checkin.get(), self.room_Checkout.get())
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
            self.room_Contacts.set("")
            self.room_Checkin.set("")   
            self.room_Checkout.set("")
            self.room_roomtype.set("")
            self.room_availableroom.set("")
            self.room_noOfdays.set("")  
            self.room_paidtax.set("")
            self.room_roomfee.set("")
            self.room_totalfee.set("")
            messagebox.showinfo("Reset", "All fields have been reset", parent=self.root)   
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        if row:
            self.room_Contacts.set(row[0])
            self.room_Checkin.set(row[1])
            self.room_Checkout.set(row[2])
            self.room_roomtype.set(row[3])    
            self.room_availableroom.set(row[4])
            self.room_noOfdays.set(row[5])
            
    def total(self):
        try:
            in_date = datetime.strptime(self.room_Checkin.get(), "%d/%m/%Y").date()
            out_date = datetime.strptime(self.room_Checkout.get(), "%d/%m/%Y").date()
        except ValueError:
            messagebox.showerror("Error", "Dates must be in dd/mm/YYYY format", parent=self.root)
            return

        if out_date < in_date:
            messagebox.showerror("Error", "Check-out must be the same or after Check-in", parent=self.root)
            return

        noOfDays = (out_date - in_date).days
        self.room_noOfdays.set(str(noOfDays))
        noOfDays = int(self.room_noOfdays.get())
        
        if self.room_roomtype.get() == "Single":
            roomFee = 500
        elif self.room_roomtype.get() == "Double":
            roomFee = 800
        else:
            roomFee = 1200
            
        totalRoomFee = noOfDays * roomFee
        tax = totalRoomFee * 0.1
        totalCost = totalRoomFee + tax
        
        self.room_paidtax.set(f"{tax:.2f}")
        self.room_roomfee.set(f"{totalRoomFee:.2f}")
        self.room_totalfee.set(f"{totalCost:.2f}")        
 
                  
            
    def searchData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")
        my_cursor = conn.cursor()
        column = self.searchVar.get()
        value = self.srchField.get()
        column_map = {
            "Contacts": "Contacts",
            "Room":"Room_available"
        }
        db_column = column_map.get(column, "Contacts")
        query = f"SELECT * FROM room WHERE {db_column} LIKE %s"
        my_cursor.execute(query, ('%' + value + '%',))
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()         
            
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=room_win(root)
    root.mainloop()        
