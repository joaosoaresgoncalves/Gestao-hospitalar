# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 19:11:44 2022

@author: marti
"""

from tkinter import *
from tkinter import ttk
from Classes.pessoa import Pessoa
import os
from tkinter import messagebox

#import csv
class Form_Login:
    code = str()
    def __init__(self, filePath = ''):
        

        # Pessoa.read()
        #self.ncols = ncols
        self.root = Tk()
        self.root.geometry('250x180')
        self.filePath = filePath
        #self.filePath = './'
        
        self.result= 1
        self.classObj = Pessoa
        self.classObj.read()
        
        self.attnames =['Login:','Password:']
        # Set root title
        self.root.title('Login')

                
        
        
        #Frame to navegate  buttons   
        self.frame_buttons = Frame(self.root)
        self.frame_buttons.grid(row=3,column=0)
        # Frame to Edit buttons
        self.frame_edit_button = Frame(self.frame_buttons)
        #self.frame_edit_button.grid(row=2,column=3, padx=10)
        self.frame_edit_button.grid(row=2,column=1, padx=10)        
    
        # Edit Buttons  
        self.button_login = Button(self.frame_edit_button,text="Entrar",  command = lambda: self.button_login_click())
        #self.button_cancel = Button(self.frame_edit_button, text="Sair",  command= lambda: self.button_cancel_click())
        #self.button_create = Button(self.frame_edit_button,text="Novo Registo",command=  lambda: self.button_create_click())
        
        # put Edit Buttons in frame Grid
        self.button_login.grid(row=2,column=2)
        # self.button_cancel.grid(row=2,column=3)
        # self.button_create.grid(row=2,column=4)
        
    
        # Frame to class
        self.frame_class = LabelFrame(self.root,text = self.classObj.__name__)
        self.frame_class.grid(row=2,column=0,padx=10,pady=10)
        
        self.ent = list()
    
        lbl = Label(self.frame_class, text='Username')
        lbl.grid(row=1, column=1, padx=10, pady=10)
        ent1 = Entry(self.frame_class)
        ent1.grid(row=1, column=2, padx=10, pady=10)
        self.ent.append(ent1)
        lbl = Label(self.frame_class, text='Password')
        lbl.grid(row=2, column=1, padx=10, pady=10)
        ent2 = Entry(self.frame_class)
        ent2.grid(row=2, column=2, padx=10, pady=10)
        self.ent.append(ent2)
        
        #### POR DEFEITO NÃO ESTÁ LOGGED IN
        self.login_Status ='Not Login'
        

        
        self.root.mainloop()

    def button_login_click(self):
        
        loginIn = self.ent[0].get()
        passwordIn = self.ent[1].get()
            
         # if loginIn[0:2] == 'es':
         #      self.result = 2
             
         #      for pessoa in self.classObj.lst:
         #          if self.classObj.obj[pessoa].username == loginIn:
         #              if self.classObj.obj[pessoa].password == passwordIn:
         #                  self.login_Status = "Login"
         #                  break
         #              else:
         #                  print("Password errada para login fornecido") 
        
         # else:
             
        username = []
        password = []
        codes=[]
        
        path = os.getcwd()
        path = path.replace("\\", '/')
        a = "/"
        
        while path[-1] != a:
            path = path[:-1]
        
        
        f1=open(path + '/forms/Pessoa.csv', 'r')
        
        for line in f1:
            a=line.split(';')
            username.append(a[10])
            codes.append(a[0])
            p=a[11]
            if p[len(p)-1]=='\n':
                password.append(p[:len(p)-1])
            else:
                password.append(p)
                
        f1.close()
        print(username, password)
        
        if loginIn not in username:
             messagebox.askokcancel("Dados inválidos", "Username não existe")
        
        else:
            if str(passwordIn) == password[username.index(loginIn)]:
                self.login_Status = "Login"

            else:
                messagebox.askokcancel("Dados inválidos", "Password incorreta")
        

        
        if  self.login_Status == "Login":
            
            Form_Login.code=codes[username.index(loginIn)]
            print(Form_Login.code)
            self.root.destroy()
            from forms.Perfil import Perfil_tk
            Perfil_tk(Form_Login.code)


        
        




        # with open('Pessoa.csv') as arquivo_referencia:
        #     tabela = csv.reader(arquivo_referencia, delimiter=';')

        #     for l in tabela:
        #         user = l[9]
        #         passw = l[10]
        #         username.append(user)
        #         password.append(passw)
            
        # arquivo_referencia.close()
    
        # if (loginIn in username) and (passwordIn in password):
        #     self.login_Status = "Login"
    
    
    
    
    
            

        #     else:
        #         if self.result == 1:
        #             self.root.destroy()
        #             from Forms.organizador_form import inicio
        #             Forms.organizador_form.inicio()
    
                       
    
    
    
    # def button_cancel_click(self):
    #    self.root.destroy()
        
    
    # def button_create_click(self):
    #     self.root.destroy()
    #     from Forms.Novo_utilizador import Registrationform
    #     Forms.Novo_utilizador.Registrationform()
        
        
        