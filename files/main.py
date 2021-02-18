from sqlite3.dbapi2 import Error
import tkinter as tk
from tkinter import (
    Toplevel,Entry,StringVar,END,Wm,Button,Label)
from files import db_stuf, second 
"""
tutorials:
https://www.tutorialspoint.com/python3/python_gui_programming.htm

"""


class Main(tk.Frame):
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.wm = Wm
        self.wm.title(self.master,"Logar/Registrar") #screen title
        self.wm.geometry(self.master,"250x250")

        lbl = Label(master,text="Logar e registrar",
        bg="grey",width="200",height="2")
        lbl.pack() #Label 1
        cleanlabel = Label(master,text="")
        cleanlabel.pack()

        self.new_window = Button(master,text="Login",
        width="250",height="2",command=self.login_screen)
        self.new_window.pack() #Login btn

        self.new_window = Button(self.master,text="Registrar",
        width="250",height="2",command=self.register)
        self.new_window.pack() #register btn

        self.destroy_butt = Button(self.master,text="Sair",
        width="250",height="2",command=self.destroyer)
        self.destroy_butt.pack() #quit btnroot
    
    def destroyer(self): #func to destroy Main()
        master = self.master
        master.quit()
        master.destroy()
        # self.master.quit
        

    def register(self): #creates Toplevel register
        self.register_screen = Toplevel(self.master)
        self.register_screen.resizable(False,False)
        self.registerscreen = Registerscreen(self.register_screen)

    def login_screen(self): # creates Toplevel login
        self.loginn = Toplevel(self.master)
        self.loginn.resizable(False,False)
        self.loginscreen = Loginscreen(self.loginn
        ,self.master)

class Registerscreen:
    def __init__(self,register):
        self.register = register
        self.wm = Wm
        self.wm.title(self.register,"Tela de Registro")
        self.wm.geometry(self.register,"300x250")

        titlelabel = Label(register,text="Tela de Registro"
        ,bg="grey",width=200,height=2)
        titlelabel.pack(side="top") #grid(row=0,column=1)
        self.cleanlabel = Label(register,text="\n")
        self.cleanlabel.pack(side="top") #grid(row=1,column=1)

        """username stuff"""
        self.username = StringVar()
        self.username_label = Label(register,text="Usuário: ")
        self.username_label.pack(side="top") #grid(row=2,column=0)
        self.username_entry = Entry(register #user entry
        ,textvariable=self.username) #stores it in a var
        self.username_entry.pack(side="top") #grid(row=2,column=1)

        """password stuff"""
        self.password = StringVar()
        self.password_label = Label(register,text="Senha: ")
        self.password_label.pack(side="top") #grid(row=3,column=0)
        self.password_entry = Entry(register#gets input
        ,textvariable=self.password,show="*")#stores it in var
        self.password_entry.pack(side="top") #grid(row=3,column=1)
        
        self.register_button = Button(register,
        text="Registrar",command=self.register_user)
        self.register_button.pack(side="top") #grid(row=4,column=1)

    def register_user(self):
        pwd = self.password.get() #get() the input
        uname = self.username.get() #stores input in var

        try: #tries saving file with username as filename
            if uname == '' or uname.isspace() == True or len(uname) <= 1:
                err = Label(self.register,text="""
                nome de usuário inválido! 
                tente novamente""",font=("Arial",10))
                err.pack(side="top")
                err.after(900,err.destroy)
            elif pwd == '' or pwd.isspace() == True or len(pwd) < 8:
                err = Label(self.register,text="""
                Senha inválida!
                Precisa conter 8 caráteres""",font=("Arial",10))
                err.pack(side="top")
                err.after(900,err.destroy)
 
            elif db_stuf.Register(uname,pwd).check() == True:
                label = Label(self.register,text="usuário já cadastrado!",
                font=("Arial",10))
                label.pack(side="top")
                self.register.after(900,label.destroy)

            else:
                lbl = Label(self.register,text="registrado!",
                font=("Arial",10))
                lbl.pack(side="top")
                self.register.after(900,lbl.destroy)

        except Error as e:
            print(e)

        self.username_entry.delete(0, END)#deletes
        self.password_entry.delete(0, END) #labels

class Loginscreen(Main):
    def __init__(self,login,master):
        self.master = master
        self.login = login
        self.wm = Wm
        self.wm.title(self.login,"Tela de Login")
        self.wm.geometry(self.login,"300x250")
        titlelabel = Label(login,text="Tela de Login"
        ,bg="grey",width=200,height=2)
        titlelabel.pack(side="top")
        self.cleanlabel = Label(login,text="\n")
        self.cleanlabel.pack(side="top") #grid(row=1,column=1)

        self.username = StringVar() #stores input in var
        self.username_label = Label(login,text="Usuário: ")
        self.username_label.pack(side="top")
        self.username_entry = Entry(login,
        textvariable=self.username)
        self.username_entry.pack(side="top")

        self.password = StringVar() #stores input in var
        self.password_label = Label(login,text="Senha: ")
        self.password_label.pack(side="top")
        self.password_entry = Entry(login
        ,show="*",textvariable=self.password)
        self.password_entry.pack(side="top")

        self.loginbutton = Button(login,text="Login"
        ,command=self.check_login)
        self.loginbutton.pack(side="top")

    def check_login(self):
        u_verify = self.username.get() #gets
        p_verify = self.password.get() #input
        
        verif = db_stuf
        
        login_user = verif.Login(u_verify,p_verify)
        
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        if bool(login_user.login_user()) == True:
            # self.master.quit()
            self.master.destroy()            
            def cur_usr(): return u_verify
            second.starter(usr=cur_usr())
            

        else:
            lbl2 = Label(self.login,text="Erro, tente novamente",
            font=("Arial",10))
            lbl2.pack(side="bottom")
            lbl2.after(900,lbl2.destroy)

def starter():
    db = db_stuf.Check_db
    db.check_table_login(self=db_stuf.Check_db(),tablename="Users") #check if table users exists

    root = tk.Tk(screenName="Main") #set Tk() main frame to root var, 
    # uses Main params as Tk params
    Main(root) #tells Main to run "root"
    root.mainloop()