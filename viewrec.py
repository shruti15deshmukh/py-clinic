from tkinter import *
from pymysql import *
from tkinter import ttk
# import pyodbc
class viewreco:
    def __init__(self):
        self.table=Tk()
        self.table.title("table view")
        self.table.iconbitmap("clinic.ico")
        self.table.state("zoomed")

        
        self.wrapperpat = LabelFrame(self.table, text="Patients")
        self.wrappersrch = LabelFrame(self.table, text="Search")
       

        self.wrapperpat.pack(fill="both", expand="yes", padx=20,pady=20)
        self.wrappersrch.pack(fill="both", expand="yes", padx=20, pady=10)

        self.trv = ttk.Treeview(self.wrapperpat, columns=(1,2,3,4,5,6,7,8,9,10,11,12), show="headings", height="6")
        self.trv.pack()

        self.trv.heading(1, text="visit number")
        self.trv.heading(2, text="Patient ID")
        self.trv.heading(3, text="name") 
        self.trv.heading(4, text="Age")
        self.trv.heading(5, text="weight")
        self.trv.heading(6, text="Gender")
        self.trv.heading(7, text="address")
        self.trv.heading(8, text="phone")
        self.trv.heading(9, text="disease")
        self.trv.heading(10, text="blood grp")
        self.trv.heading(11, text="med history")
        self.trv.heading(12, text="blood pressure")
        self.table.mainloop()
    
    def connectToDb(self):
        self.rows=0
       

        

        # Conneting string
        self.con = connect(host= 'localhost', user= 'root', password= '', db= 'clinicdb')

        # Connect to db
        self.cur = self.con.cursor()

        self.getData()

    def getData(self):
        # self.data = self.cur.execute("SELECT * FROM record")
        # self.data.fetchall()
        
        # Executing the query
        self.cur.execute("select * from record;")
        self.data = self.cur.fetchall()
        # self.update(self.rows) 

        # self.showData()

    # def showData(self):

    #     self.clrdata()
    #     self.evid.insert(0,self.data[self.rowno][0])
    #     self.euid.insert(0,self.data[self.rowno][1])
    #     self.ename.insert(0,self.data[self.rowno][2])
    #     self.eage.insert(0,self.data[self.rowno][3])
    #     self.ewt.insert(0,self.data[self.rowno][4])
    #     self.esex.insert(0,self.data[self.rowno][5])
    #     self.eadd.insert(0,self.data[self.rowno][6])
    #     self.eph.insert(0,self.data[self.rowno][7])
    #     self.edis.insert(0,self.data[self.rowno][8])
    #     self.ebgrp.insert(0,self.data[self.rowno][9])
    #     # self.evisdt.insert(0,self.data[self.rowno][10])
    #     self.emed.insert(0,self.data[self.rowno][10])
    #     self.ebp.insert(0,self.data[self.rowno][11])
        
    
        

    # def update(self,rows):
    #     for i in rows:
    #         self.trv.insert('', 'end', values=(i['visitno'], i['pid'], i['name'], i['age'],i['weight'], i['gender'], i['address'], i['phone']
    #                                            ,i['disease'], i['bloodgrp'], i['med_history'], i['bp']))

   


if __name__=='__main__':

    v=viewreco()





    
