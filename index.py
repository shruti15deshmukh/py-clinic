#Login Page

from tkinter import *
from pymysql import *
from tkinter import messagebox
# from mysql import *
from clinicrec import *

class Login:

    def __init__(self) -> None:
        
        self.root = Tk()
        self.root.geometry("400x200+450+200")
        self.root.title("Login Page")
        #self.root.iconbitmap("Hospital//H.ico")

        # Creating labels

        self.lblname = Label(master= self.root, anchor= "w", justify= "center",
                               text= "Name", font=("Arial Rounded MT",18))
        self.lblname.place(x=20,y=20,width=200,height=30)

        self.lblpassword = Label(master= self.root, anchor= "w", justify= "center", 
                                 text= "Password", font= ("Arial Rounded MT",18))
        self.lblpassword.place(x=20,y=80,width=200,height=30)


        # Creating entries

        self.enname = Entry(master= self.root, font= ("Arial",14))
        self.enname.place(x=180,y=20,width=200,height=30)

        self.enpassword = Entry(master= self.root, show= "*", font= ("Arial",14))
        self.enpassword.place(x=180,y=80,width=200,height=30)

        # Creating button

        self.btnsubmit = Button(master= self.root, text= "Submit", font= ("Arial Rounded MT",18),
        command=self.checklogin)
        self.btnsubmit.place(x=110,y=140,width=100,height=30)

        #self.connectToDb()

        self.root.mainloop()

    def connectToDb(self):

        # Conneting string
        self.con = connect(host= "localhost", user= "root", password= "", db= "clinicdb")

        # Connect to db
        self.cur = self.con.cursor()

    def checklogin(self):
        name = self.enname.get()
        pas = self.enpassword.get()

        qry = "select * from login where name = '" + name + "'" +  " and Password = '" + pas + "';"

        self.connectToDb()

        n = self.cur.execute(qry)
        if(n > 0):
            messagebox.showinfo("Clinic Project","Login Successs")
            self.root.destroy()
            objpat = clinicreco()
          
           
        else:
            messagebox.showerror("Clinic Project","Login Error")



        

if __name__=='__main__':
    objlogin = Login()