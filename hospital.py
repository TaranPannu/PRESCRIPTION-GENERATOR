from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1100x700")

        self.NameofTablets = StringVar()
        self.ref = StringVar()
        self.patientname = StringVar()
        self.patientage = StringVar()
        self.problem = StringVar()

        lbltitle = Label(
            self.root,
            bd=1,
            relief=RIDGE,
            text="PRESCRIPTION GENERATOR",
            fg="white",
            bg="black",
            font=("Arial", 40, "bold"),
        )
        lbltitle.pack(side=TOP, fill=X)
        # ---------------------------------Dataframe---------------------------------
        DataFrame = Frame(self.root, bd=2, padx=20, relief=RIDGE, bg="black")
        DataFrame.place(x=0, y=80, width=1500, height=350)

        DataFrameLeft = LabelFrame(
            DataFrame,
            bd=1,
            padx=20,
            relief=RIDGE,
            bg="black",
            fg="white",
            font=("arial", 12, "bold"),
            text="Patient Information",
        )
        DataFrameLeft.place(x=0, y=5, width=600, height=300)

        DataFrameRight = LabelFrame(
            DataFrame,
        
            padx=20,
            relief=RIDGE,
            bg="black",
            fg="white",
            font=("arial", 12, "bold"),
            text="Prescription",
        )
        DataFrameRight.place(x=620, y=5, width=450, height=300)

        # ---------------------------------Button frame---------------------------------

        ButtonFrame = Frame(self.root, bd=1, relief=RIDGE, bg="black")
        ButtonFrame.place(x=0, y=470, width=1500, height=70)

        # ---------------------------------Details frame---------------------------------

        DetailsFrame = Frame(self.root, bd=1, relief=RIDGE)
        DetailsFrame.place(x=0, y=520, width=1500, height=260)

        # ---------------------------------Data frame Left---------------------------------
        

        lblNameTablet = Label(
    DataFrameLeft,
    text="Names of Tablet: ",
    font=("arial", 12, "bold"),
    padx=2,
   pady=10,   
    
    fg="white",
    bg="black"
)

        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(
            DataFrameLeft,
            textvariable=self.NameofTablets,
            font=("arial", 12, "bold"),
            width=20,
        )
        comNametablet["values"] = ("Hydrocodone", "Metformin", "Antibiotics", "Antibiotics", "Losartan")
        comNametablet.grid(row=0, column=1)
      

        lblref = Label(
            DataFrameLeft,
           
            text="Refrence no:  ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=2.5,
            fg="white",
            bg="black",
        )
        lblref.grid(row=1, column=0, sticky=W)
        txt = Entry(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            width=20,
        )
        txt.grid(row=1, column=1)

        lblpatientname = Label(
            DataFrameLeft,
            text="Patient Name: ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=2.5,
            fg="white",
            bg="black",
        )
        lblpatientname.grid(row=2, column=0)

        txtpatientname = Entry(
            DataFrameLeft,
            textvariable=self.patientname,
            font=("arial", 12, "bold"),
            width=20,
        )
        txtpatientname.grid(row=2, column=1)

        lblpatientage = Label(
            DataFrameLeft,
            text="Patient Age: ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=2.5,
            fg="white",
            bg="black",
        )
        lblpatientage.grid(row=3, column=0)

        txtpatientage = Entry(
            DataFrameLeft,
            textvariable=self.patientage,
            font=("arial", 12, "bold"),
            width=20,
        )
        txtpatientage.grid(row=3, column=1)

        lblproblem = Label(
            DataFrameLeft,
            text="Problem: ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=2.5,
            fg="white",
            bg="black",
        )
        lblproblem.grid(row=4, column=0)

        txtproblem = Entry(
            DataFrameLeft,
            textvariable=self.problem,
            font=("arial", 12, "bold"),
            width=20,
        )
        txtproblem.grid(row=4, column=1)


        # ---------------------------------Data frame Right---------------------------------

        self.txtpers = Text(
            DataFrameRight,
            font=("arial", 12, "bold"),
            width=40,
            height=13,
            padx=2,
            pady=2,
            fg="white",
            bg="black",
        )
        self.txtpers.grid(row=0, column=0)

        # ---------------------------------Buttons---------------------------------
        btnpers = Button(
            ButtonFrame,
            text="Submit Data",
             bg="blue",
            fg="black",
            font=("arial", 12, "bold"),
            width=15,
            height=1,
            padx=10,
            pady=9,
            borderwidth=1,
            relief="ridge",
            command=self.iPrescriptionData,
        )
        btnpers.grid(row=0, column=0)
        btnpers = Button(
            ButtonFrame,
            text="Get Prescription",
             bg="blue",
            fg="black",
            font=("arial", 12, "bold"),
            width=15,
            height=1,
            padx=10,
            pady=9,
            borderwidth=1,
            relief="ridge",
            command=self.iPrectioption,
        )
        btnpers.grid(row=0, column=2)
        btnpers = Button(
            ButtonFrame,
            text="Update Information",
             bg="blue",
            fg="black",
            font=("arial", 12, "bold"),
            width=15,
            height=1,
            padx=10,
            pady=9,
            borderwidth=1,
            relief="ridge",
            command=self.update,
        )
        btnpers.grid(row=0, column=4)
        btnpers = Button(
            ButtonFrame,
            text="Delete",
             bg="blue",
            fg="black",
            font=("arial", 12, "bold"),
            width=15,
            height=1,
            padx=10,
            pady=9,
            borderwidth=1,
            relief="ridge",
            command=self.idelete,
        )
        btnpers.grid(row=0, column=6)
        # ---------------------------------Table---------------------------------
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(
            DetailsFrame,
            columns=("nameoftable", "ref", "patientname", "patientage", "problem"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable", text="Name of Table")
        self.hospital_table.heading("ref", text="Refrence no:")
        self.hospital_table.heading("patientname", text="Patient Name")
        self.hospital_table.heading("patientage", text="Patient Age")
        self.hospital_table.heading("problem", text="Problem")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def iPrescriptionData(self):
        
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Mysql!1221",
                    database="hospital",
                )
                mycursor = conn.cursor()
                mycursor.execute(
                    "INSERT INTO hospital (Name_of_tablets, patientname, patientage, problem) VALUES ( %s, %s, %s, %s)",
                    (
                        self.NameofTablets.get(),
        
                        self.patientname.get(),
                        self.patientage.get(),
                        self.problem.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data inserted successfully")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                messagebox.showinfo("Error", str(e))

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Mysql!1221",
            database="hospital",
        )
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM hospital")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
         cursor_rows=self.hospital_table.focus()
         content=self.hospital_table.item(cursor_rows)
         row=content["values"]
         self.NameofTablets.set(row[0])
         self.ref.set(row[1])
         self.patientname.set(row[2])
         self.patientage.set(row[3])

    def iPrectioption(self):
         self.txtpers.insert(END,"name of Tablets:\t\t\t"+self.NameofTablets.get()+"\n")
         self.txtpers.insert(END,"Refrence No:\t\t\t"+self.ref.get()+"\n")
         self.txtpers.insert(END,"Patient Name:\t\t\t"+self.patientname.get()+"\n")
         self.txtpers.insert(END,"Patient age:\t\t\t"+self.patientage.get()+"\n")
         self.txtpers.insert(END,"Problem:\t\t\t"+self.problem.get()+"\n")
    
    def update(self):
             conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Mysql!1221",
                    database="hospital",
                )
             mycursor = conn.cursor()
             mycursor.execute("update hospital set Name_of_tablets=%s,patientname=%s,patientage=%s,problem=%s",   (
                        self.NameofTablets.get(),
        
                        self.patientname.get(),
                        self.patientage.get(),
                        self.problem.get(),
                    ),)
             conn.commit()
             conn.close()
    def idelete(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Mysql!1221",
            database="hospital",
        )
        mycursor = conn.cursor()
        query="delete from hospital where patientage=%s"
        value=(self.patientage.get(),)
        mycursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")
root = Tk()
ob = Hospital(root)
root.mainloop()

 
