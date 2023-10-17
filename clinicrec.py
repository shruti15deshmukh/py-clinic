from tkinter import *
from pymysql import *
from tkinter import messagebox
# from clinic import *
class clinicreco:
    def __init__(self):
        self.clirec=Tk()
        self.clirec.title("clinic record")
        self.clirec.iconbitmap("clinic.ico")
        self.clirec.state("zoomed")

        # self.show()


        self.lvid=Label(master=self.cli, text= "visit no", font=("times new roman",10,"italic"), fg="blue")
        self.lvid.place(x=10,y=10,width=100,height=30)
        self.evid=Entry(master=self.cli,font=("times new roman",10,"italic"))
        self.evid.place(x=140,y=10,width=150,height=30)

        self.luid=Label(master=self.cli, text= "patient id" ,font=("times new roman",10,"italic"), fg="blue")
        self.luid.place(x=10,y=30,width=110,height=30)
        self.euid=Entry(master=self.cli, font=("times new roman",10,"italic"))
        self.euid.place(x=140,y=30,width=150,height=30) 
        # obj=cliniclogin()
        # self.euid.insert(0,obj.euid )

        self.lname=Label(master=self.cli, text= "name", font=("times new roman",10,"italic"), fg="blue")
        self.lname.place(x=10,y=50,width=100,height=30)
        self.ename=Entry(master=self.cli,font=("times new roman",10,"italic"))
        self.ename.place(x=140,y=50,width=150,height=30)

        self.lage=Label(master=self.cli, text= "age" ,font=("times new roman",10,"italic"), fg="blue")
        self.lage.place(x=10,y=70,width=110,height=30)
        self.eage=Entry(master=self.cli, font=("times new roman",10,"italic"))
        self.eage.place(x=140,y=70,width=150,height=30)

        self.lweight=Label(master=self.cli, text= "weight", font=("times new roman",10,"italic"), fg="blue")
        self.lweight.place(x=10,y=90,width=100,height=30)
        self.ewt=Entry(master=self.cli,font=("times new roman",10,"italic"))
        self.ewt.place(x=140,y=90,width=150,height=30)

        self.lsex=Label(master=self.cli, text= "gender" ,font=("times new roman",10,"italic"), fg="blue")
        self.lsex.place(x=10,y=110,width=110,height=30)
        self.esex=Entry(master=self.cli, font=("times new roman",10,"italic"))
        self.esex.place(x=140,y=110,width=150,height=30)

        self.ladd=Label(master=self.cli, text= "address", font=("times new roman",10,"italic"), fg="blue")
        self.ladd.place(x=10,y=130,width=100,height=30)
        self.eadd=Entry(master=self.cli,font=("times new roman",10,"italic"))
        self.eadd.place(x=140,y=130,width=150,height=30)

        self.lph=Label(master=self.cli, text= "phone" ,font=("times new roman",10,"italic"), fg="blue")
        self.lph.place(x=10,y=150,width=110,height=30)
        self.eph=Entry(master=self.cli, font=("times new roman",10,"italic"))
        self.eph.place(x=140,y=150,width=150,height=30)

        self.ldis=Label(master=self.cli, text= "disease", font=("times new roman",10,"italic"), fg="blue")
        self.ldis.place(x=10,y=170,width=100,height=30)
        self.edis=Entry(master=self.cli,font=("times new roman",10,"italic"))
        self.edis.place(x=140,y=170,width=150,height=30)

        self.lbgrp=Label(master=self.cli, text= "blood group" ,font=("times new roman",10,"italic"), fg="blue")
        self.lbgrp.place(x=10,y=190,width=110,height=30)
        self.ebgrp=Entry(master=self.cli, font=("times new roman",10,"italic"))
        self.ebgrp.place(x=140,y=190,width=150,height=30)

        

        self.lmed=Label(master=self.cli, text= "med history", font=("times new roman",10,"italic"), fg="blue")
        self.lmed.place(x=10,y=230,width=100,height=30)
        self.emed=Entry(master=self.cli,font=("times new roman",10,"italic"))
        self.emed.place(x=140,y=230,width=150,height=30)

        self.lbp=Label(master=self.cli, text= "bp", font=("times new roman",10,"italic"), fg="blue")
        self.lbp.place(x=10,y=210,width=100,height=30)
        self.ebp=Entry(master=self.cli,font=("times new roman",10,"italic"))
        self.ebp.place(x=140,y=210,width=150,height=30)

        # self.lvisdt=Label(master=self.cli, text= "visit date", font=("times new roman",10,"italic"), fg="blue")
        # self.lvisdt.place(x=10,y=250,width=100,height=30)
        # self.evisdt=Entry(master=self.cli,font=("times new roman",10,"italic"))
        # self.evisdt.place(x=140,y=250,width=150,height=30)

        

        




        self.subm = Button(self.cli, text = 'submit', bd = '10',command = self.insertData)
        self.subm.place(x=10,y=300,width=150)
        self.clr = Button(self.cli, text = 'clear', bd = '10',command = self.clrdata)
        self.clr.place(x=250,y=300,width=150)

        self.connectToDb()

        self.clirec.mainloop()
    
    # def show(self):
    #    obj=cliniclogin()
    #    uid=obj.checklogin.id
    #    self.euid.insert(0,uid)
    def connectToDb(self):
        self.rowno=0

        

        # Conneting string
        self.con = connect(host= 'localhost', user= 'root', password= '', db= 'clinicdb')

        # Connect to db
        self.cur = self.con.cursor()

        self.getData()

    def getData(self):

        # Executing the query
        self.cur.execute("select * from record;")

        self.data = self.cur.fetchall()

    #     self.showData()

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
        
    def clrdata(self):
        self.evid.delete(0,END)
        self.euid.delete(0,END)
        self.ename.delete(0,END)
        self.eage.delete(0,END)
        self.ewt.delete(0,END)
        self.esex.delete(0,END)
        self.eadd.delete(0,END)
        self.eph.delete(0,END)
        self.edis.delete(0,END)
        self.ebgrp.delete(0,END)
        
        self.emed.delete(0,END)
        self.ebp.delete(0,END)
        # self.evisdt.delete(0,END)
        

    def insertData(self):

        vid = self.evid.get()
        pid = self.euid.get()
        name = self.ename.get()
        age = self.eage.get()
        weight = self.ewt.get()
        sex = self.esex.get()
        add = self.eadd.get()
        phno = self.eph.get()
        disease = self.edis.get()
        bloodgroup = self.ebgrp.get()
        
        medhis = self.emed.get()
        bp = self.ebp.get()
        # dateofvisit = self.evisdt.get()
        
        

        query = "insert into record values(" + vid  + ",'" + pid + "','" + name + "'," + age + "," + weight + ",'" + sex + "','" + add + "'," + phno + ",'" + disease + "','" + bloodgroup + "','" + medhis+ "'," + bp + ");"
        # self.connectToDb()
        # print (query)
        n = self.cur.execute(query)
        self.con.commit()

        if(n > 0):
            messagebox.showinfo('Success', 'Record Inserted')
            self.rowno = 0
            self.getData()
        else:
            messagebox.showerror('UnSuccess', 'Record Insertion error')
    



if __name__== '__main__' :
    rec=clinicreco()