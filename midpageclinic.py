from tkinter import *
from pymysql import *
from tkinter import messagebox
# from mysql import *
from clinicrec import *
from viewrec import *

from keyboard import *
class clinicmenu:
    def __init__(self):
        self.climenu=Tk()
        self.climenu.title("clinic login")
        self.climenu.iconbitmap("clinic.ico")
        
        self.climenu.state("zoomed")
        # obj=clinicreco()

        menubar = Menu(self.climenu, background='yellow', fg='white')
  

        add = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Add', menu = add)
        add.add_command(label ='Add', command =clinicreco)
        # self.cli.destroy()
        view = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='View', menu = view)
        add.add_command(label ='View', command =viewreco)

        self.climenu.config(menu = menubar)
        # self.cli.config(vmenu = menubar)

     
        self.climenu.mainloop()
if __name__=='__main__':
    
    midpg=clinicmenu()