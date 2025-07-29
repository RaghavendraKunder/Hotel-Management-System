from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import random
import mysql.connector
from tkinter import messagebox

class Cust_win:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1119x516+241+173")
        
        #============================variables=================================
        self.cust_ref = StringVar()
        x=random.randint(1000,9999)
        self.cust_ref.set(str(x))
        
        self.cust_name = StringVar()
        self.cust_mother = StringVar()
        self.cust_gender = StringVar()
        self.cust_mobile = StringVar()
        self.cust_email = StringVar()
        self.cust_country = StringVar()
        self.cust_idproof = StringVar()
        self.cust_idnum = StringVar()
        self.cust_address = StringVar()
        
        #====================title==========================
        lbl_title = Label(self.root, text="Add Customer Details", font=("times new roman", 30, "bold italic"),bg="midnightblue",fg="snow",bd=4, relief=RIDGE,anchor="w")
        lbl_title.place(x=369,y=0,width=1119,height=40)
        
         #======================logo===========================
        img1 = Image.open(r"C:\Users\admin\OneDrive\Desktop\Hotel-Management-System\images\blue.jpg")
        img1 = img1.resize((230,160),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
       
        lblimg =Label(self.root, image = self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=180,height=40)
        
        #========================labelFrame=========================
        labelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 15, "bold"),padx=2)
        labelFrameleft.place(x=0,y=1,width=368,height=514)
        
        #=======================labels and entries==========================
        #======Cust ref========
        lbl_cust_ref = Label(labelFrameleft, text="Customer Ref", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1, column=0, sticky=W)     
        
        entry_ref = ttk.Entry(labelFrameleft,textvariable=self.cust_ref, font=("Comic Sans MS", 12, "italic"), width=22,state='readonly')   
        entry_ref.grid(row=1, column=1, padx=5, pady=6, sticky=W)
        
        #======Cust Name========
        cName = Label(labelFrameleft, text="Customer Name", font=("times new roman", 12, "bold"),padx=2,pady=6)
        cName.grid(row=2, column=0, sticky=W)     
        
        txtName = ttk.Entry(labelFrameleft, textvariable=self.cust_name, font=("Comic Sans MS", 12, "italic"), width=22)   
        txtName.grid(row=2, column=1, padx=5, pady=6, sticky=W)
        
        #======Mother Name========
        mName = Label(labelFrameleft, text="Mother Name", font=("times new roman", 12, "bold"),padx=2,pady=6)
        mName.grid(row=3, column=0, sticky=W)     
        
        txtMname = ttk.Entry(labelFrameleft ,textvariable=self.cust_mother, font=("Comic Sans MS", 12, "italic"), width=22)   
        txtMname.grid(row=3, column=1, padx=5, pady=6, sticky=W)
        
        #======Gender Combobox========
        gender = Label(labelFrameleft, text="Gender", font=("times new roman", 12, "bold"),padx=2,pady=6)
        gender.grid(row=4, column=0, sticky=W)     
        
        combo_gender = ttk.Combobox(labelFrameleft ,textvariable=self.cust_gender, font=("Comic Sans MS", 12, "italic"), width=20, state="readonly")
        combo_gender["values"] = ("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4, column=1, padx=5, pady=6, sticky=W)        
        #======Mobile Number========
        mobileNumber = Label(labelFrameleft, text="Mobile Number", font=("times new roman", 12, "bold"),padx=2,pady=6)
        mobileNumber.grid(row=5, column=0, sticky=W)     
        
        lblMnum = ttk.Entry(labelFrameleft ,textvariable=self.cust_mobile, font=("Comic Sans MS", 12, "italic"), width=22)   
        lblMnum.grid(row=5, column=1, padx=5, pady=6, sticky=W)
        
        #======Email========
        eMail = Label(labelFrameleft, text="Email", font=("times new roman", 12, "bold"),padx=2,pady=6)
        eMail.grid(row=6, column=0, sticky=W)     
        
        lblEmail = ttk.Entry(labelFrameleft ,textvariable=self.cust_email, font=("Comic Sans MS", 12, "italic"), width=22)   
        lblEmail.grid(row=6, column=1, padx=5, pady=6, sticky=W)
        
        #======Nationality========
        country = Label(labelFrameleft, text="Nationality", font=("times new roman", 12, "bold"),padx=2,pady=6)
        country.grid(row=7, column=0, sticky=W)     
        
        combo_Nationality = ttk.Combobox(labelFrameleft ,textvariable=self.cust_country, font=("Comic Sans MS", 12, "italic"), width=20, state="readonly")
        combo_Nationality["values"] = (
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Cote d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czechia",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Kosovo",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Korea",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Korea",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates (UAE)",
    "United Kingdom (UK)",
    "United States of America (USA)",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City (Holy See)",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe"
)
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1, padx=5, pady=6, sticky=W)
        
        #======idproof type combobox========
        idProof = Label(labelFrameleft, text="Id Proof", font=("times new roman", 12, "bold"),padx=2,pady=6)
        idProof.grid(row=8, column=0, sticky=W)     
        
        combo_idProof = ttk.Combobox(labelFrameleft ,textvariable=self.cust_idproof, font=("Comic Sans MS", 12, "italic"), width=20, state="readonly")
        combo_idProof["values"] = ("Aadhar","Pan Card","Driving License","Passport")
        combo_idProof.current(0)
        combo_idProof.grid(row=8, column=1, padx=5, pady=6, sticky=W)  
        
         #======Id Number========
        idNumber = Label(labelFrameleft , text="Id Number", font=("times new roman", 12, "bold"),padx=2,pady=6)
        idNumber.grid(row=9, column=0, sticky=W)     
        
        lblIdnum = ttk.Entry(labelFrameleft, textvariable=self.cust_idnum, font=("Comic Sans MS", 12, "italic"), width=22)   
        lblIdnum.grid(row=9, column=1, padx=5, pady=6, sticky=W)
        
         #======Address========
        address = Label(labelFrameleft , text="Address", font=("times new roman", 12, "bold"),padx=2,pady=6)
        address.grid(row=10, column=0, sticky=W)     
        
        lblAddress = ttk.Entry(labelFrameleft, textvariable=self.cust_address, font=("Comic Sans MS", 12, "italic"), width=22)   
        lblAddress.grid(row=10, column=1, padx=5, pady=6, sticky=W)
        
        #=======================================buttons============================================================================================
        btn_frame = Frame(labelFrameleft, bd=2)
        btn_frame.place(x=-4,y=435,width=365,height=50)
        
        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnAdd.grid(row=0, column=0, padx=5, pady=5)
        
        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnUpdate.grid(row=0, column=1, padx=5, pady=5)
        
        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnDelete.grid(row=0, column=2, padx=5, pady=5)
        
        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnReset.grid(row=0, column=3, padx=5, pady=5)
        
        #========================Table Frame=========================
        labelFrameRight = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 15, "bold italic"),padx=2)
        labelFrameRight.place(x=369,y=41,width=745,height=473)   
        
        searchBy = Label(labelFrameRight, text="Search By", font=("times new roman", 12, "bold italic"),bg="midnightblue",fg="snow",padx=2,pady=2)
        searchBy.grid(row=0, column=0, padx=0, pady=6, sticky=W)
        
        combo_searchBy = ttk.Combobox(labelFrameRight, font=("Comic Sans MS", 12, "bold italic"), width=20, state="readonly")
        combo_searchBy["values"] = ("Ref Id","Name","Mother's Name","Gender","Mobile NO","Email","Country","Id Proof","Id Number","Address")
        combo_searchBy.current(0)
        combo_searchBy.grid(row=0, column=1, padx=0, pady=6, sticky=W) 
        
        searchField = ttk.Entry(labelFrameRight, font=("Comic Sans MS", 12, "italic"), width=22)   
        searchField.grid(row=0, column=2, padx=4, pady=6, sticky=W)
        
        btnSearch = Button(labelFrameRight, text="Update", font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnSearch.grid(row=0, column=3, padx=2, pady=2)
        
        btnShowall = Button(labelFrameRight, text="Delete", font=("times new roman", 12, "bold italic"), bg="midnightblue", fg="white", width=8)
        btnShowall.grid(row=0, column=4, padx=2, pady=2)
        
        #========================Show Data Table=========================
        labelFrametable = Frame(labelFrameRight, bd=2, relief=RIDGE,padx=2)
        labelFrametable.place(x=0,y=41,width=737,height=400) 
        
        scroll_x= Scrollbar(labelFrametable, orient=HORIZONTAL)
        scroll_y= Scrollbar(labelFrametable, orient=VERTICAL)
        
        self.Cust_Details_table = ttk.Treeview(labelFrametable, columns=("ref","name","mother","gender","mobile","email","country","idproof","idnum","address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.Cust_Details_table.xview)
        scroll_y.config(command=self.Cust_Details_table.yview)
        
        self.Cust_Details_table.heading("ref", text="Refer No")
        self.Cust_Details_table.heading("name", text="Name")
        self.Cust_Details_table.heading("mother", text="Mother's Name")
        self.Cust_Details_table.heading("gender", text="Gender")
        self.Cust_Details_table.heading("mobile", text="Mobile Number")
        self.Cust_Details_table.heading("email", text="Email Address")
        self.Cust_Details_table.heading("country", text="Country")        
        self.Cust_Details_table.heading("idproof", text="ID Proof")
        self.Cust_Details_table.heading("idnum", text="Id Number")
        self.Cust_Details_table.heading("address", text="Address")
        
        self.Cust_Details_table["show"] = "headings"
        self.Cust_Details_table.column("ref", width=100)
        self.Cust_Details_table.column("name", width=100)
        self.Cust_Details_table.column("mother", width=100)
        self.Cust_Details_table.column("gender", width=100)
        self.Cust_Details_table.column("mobile", width=100)
        self.Cust_Details_table.column("email", width=100)
        self.Cust_Details_table.column("country", width=100)
        self.Cust_Details_table.column("idproof", width=100)
        self.Cust_Details_table.column("idnum", width=100)
        self.Cust_Details_table.column("address", width=100)
        self.Cust_Details_table.pack(fill=BOTH, expand=1)
        self.Cust_Details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()  
        
    def add_data(self):
        if self.cust_mobile.get() == "" or self.cust_mother.get() == "" or self.cust_name.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)   
        else:  
            try:   
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                 self.cust_ref.get(),
                                                                                                 self.cust_name.get(),
                                                                                                 self.cust_mother.get(),
                                                                                                 self.cust_gender.get(),
                                                                                                 self.cust_mobile.get(),
                                                                                                 self.cust_email.get(),
                                                                                                 self.cust_country.get(),
                                                                                                 self.cust_idproof.get(),
                                                                                                 self.cust_idnum.get(),
                                                                                                 self.cust_address.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)    
            
     
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
            for i in rows:
                self.Cust_Details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_table.focus()
        content = self.Cust_Details_table.item(cursor_row)
        row = content["values"]
        if row:
            self.cust_ref.set(row[0])
            self.cust_name.set(row[1])
            self.cust_mother.set(row[2])
            self.cust_gender.set(row[3])    
            self.cust_mobile.set(row[4])
            self.cust_email.set(row[5])
            self.cust_country.set(row[6])
            self.cust_idproof.set(row[7])
            self.cust_idnum.set(row[8])
            self.cust_address.set(row[9])
            
    def update(self):
        if self.cust_mobile.get() == "" or self.cust_mother.get() == "" or self.cust_name.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)   
        else:  
            try:   
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
                my_cursor = conn.cursor()
                my_cursor.execute("update customer set name=%s, mother=%s, gender=%s, mobile=%s, email=%s, country=%s, idproof=%s, idnum=%s, address=%s where ref=%s", (self.cust_name.get(),
                                                                                                                                                            self.cust_mother.get(),
                                                                                                                                                            self.cust_gender.get(),
                                                                                                                                                            self.cust_mobile.get(),
                                                                                                                                                            self.cust_email.get(),
                                                                                                                                                            self.cust_country.get(),
                                                                                                                                                            self.cust_idproof.get(),
                                                                                                                                                            self.cust_idnum.get(),
                                                                                                                                                            self.cust_address.get(),
                                                                                                                                                            self.cust_ref.get(),))  
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer details updated successfully",parent=self.root)      
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)  
                
    def mDelete(self): 
        mDelete = messagebox.askyesno("Delete", "Are you sure you want to delete this customer?", parent=self.root)    
        if mDelete > 0:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sujat@1972", database="management")     
                my_cursor = conn.cursor()
                query = "delete from customer where ref=%s and name=%s and mother=%s"
                value=(self.cust_ref.get(), self.cust_name.get(), self.cust_mother.get())
                my_cursor.execute(query, value)
                messagebox.showinfo("Success", "Customer details deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)   
        else:
            if not mDelete:
                return        
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
            self.cust_name.set("")
            self.cust_ref.set("")
            self.cust_mother.set("")
            self.cust_gender.set("")    
            self.cust_mobile.set("")
            self.cust_email.set("")
            self.cust_country.set("")
            self.cust_idproof.set("")
            self.cust_idnum.set("")
            self.cust_address.set("")  
            messagebox.showinfo("Reset", "All fields have been reset", parent=self.root)          
      
            
if __name__=="__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()
            