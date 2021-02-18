from tkinter import (
    Toplevel
    ,Entry
    ,messagebox
    ,StringVar
    ,END
    ,Button
    ,Frame
    ,Tk
    ,Label
    ,Menu
    ,Text
    ,Wm)

import tkinter.constants
from . import db_stuf




def starter(**usr):
    root = Tk() #set Tk() main frame to root var, 
    # uses Second params as Tk params
    Second(root,usr=usr["usr"]) #tells Main to run "root"
    root.mainloop() 

class Second(Frame):
    def __init__(self,second,usr=...):
        super().__init__()
        self.usr = usr
        self.db = db_stuf.Get_user()
        self.wm = Wm
        self.second = second
        self.wm.title(self.second,"Página Principal")
        self.wm.state(self.second,"zoomed") #set to maximized
        self.bar = Menu(self.second)        
        
        file_menu = Menu(self.bar,tearoff=0)
        file_menu.add_command(label="Novo Paciente")
        file_menu.add_command(label="Novo Laudo")
        file_menu.add_separator()
        file_menu.add_command(label="sair",command=self.quit)
        self.bar.add_cascade(label="Arquivo",menu=file_menu)
       
        self.second.config(menu=self.bar)

        lbl = Label(self.second,text=f"""Bem vindo {self.usr}"""
          )
        btn1 = Button(self.second,text="Novo Paciente",width=20
        ,height=1,command=self.n_laudo)
        btn2 = Button(self.second,text="Novo Laudo",width=20
        ,height=1,command=self.n_laudo)
        
        lbl.grid(row=0,pady=10)
        btn1.grid(row=1,column=0,padx=10)
        btn2.grid(row=1,column=1,padx=10)
        
    def n_laudo(self):
        top = Toplevel(self.second)
        top.focus
        top.title("Novo paciente")