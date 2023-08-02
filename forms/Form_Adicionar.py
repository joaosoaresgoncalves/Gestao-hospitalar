#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 21:24:42 2022

@author: inespaivacampos
"""

import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Classes.pessoa import Pessoa
from Classes.departamento import Departamento

def Adicionar_tk():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Perfil")
    #setting height and width of screen
    reg_screen.geometry("520x500")
    
    reg_screen.configure(bg="#2b9f90")
    
    #declaring variable
    #code, name, dob, gender, nif, salary, email, phone, depcode, username, password
    global message;
    global _code
    global _nome
    global _funcao
    global _dob
    global _gender
    global _nif
    global _salary
    global _email
    global _phone2
    global _depcode    
    global _username
    global _password
    
    _code = IntVar()
    _nome = StringVar()
    _funcao = StringVar()
    _phone2 = IntVar()
    _email=StringVar()
    _gender=StringVar()
    _dob=StringVar()
    _nif=IntVar()
    _salary=IntVar()
    _depcode=IntVar()
    _username=StringVar()
    _password=StringVar()
    
    message=StringVar()
    
    #########################
    
    def save_ad():
    # Pessoa.read()
    # obj=Pessoa.obj[codigo]
    #obj=Pessoa.obj[code]
    
        Departamento.read()
        Pessoa.read()
        
        print(Departamento.lst)

        lista=_dob.get().strip().split("-")
        if len(str(_phone2.get())) !=9:
            messagebox.askokcancel("Dados inválidos", "o seu número tem de ter 9 algarismos")
        elif len(lista[0])!=4 or len(lista[1])!=2 or len(lista[2])!=2:
            messagebox.askokcancel("Dados inválidos", "a data tem de estar no formato AAAA-MM-DD")
        elif datetime.date.fromisoformat(_dob.get())>=datetime.date.today():
            messagebox.askokcancel("Dados inválidos", "a data ainda não aconteceu")
        elif (_gender.get()!="F" and _gender.get()!="M"):
            messagebox.askokcancel("Dados inválidos", "o género não existe")
        elif _depcode.get() not in Departamento.lst:
            messagebox.askokcancel("Dados inválidos", "o departamento não existe")
            
        else:
            
            code = int(max(Pessoa.lst))+1
    
            nome=_nome.get()
            phone=_phone.get()
            email=_email.get()
            username=_username.get()
            password=_password.get()
            nome = _nome.get()
            funcao = _funcao.get()
            gender = _gender.get()
            dob =  _dob.get()
            nif = _nif.get()
            salary = _salary.get()
            depcode = _depcode.get()
            
            p1=Pessoa(code, nome, funcao, dob, gender, nif, salary, email, phone, depcode, username, password, 'user')
    
        
    
    
    
            Pessoa.write()
        print(e1.get())
        print(len(str(e1.get())
    
    
    ####################
    
    Label(reg_screen, text="                     Perfil                                                                                  ", bg="#1b2f40", fg='#faa507', font="-weight bold -size 15").place(x=0,y=18)
    
    Label(reg_screen, text="Nome:",bg="#1b6f10",fg="#FFFFFF", font="-size 10").place(x=40,y=70)
    #name textbox
    Entry(reg_screen, textvariable=_nome, width='30' ).place(x=95,y=70)

    # Label(reg_screen, text="Código:",bg="#1b6f10",fg="#FFFFFF", font="-size 10").place(x=300,y=70)
    # #name textbox
    # Entry(reg_screen, textvariable=_code, width='20' ).place(x=365,y=70)

    #contacto Label
    Label(reg_screen, text="Contacto:",bg="#1b6f10",fg="#FFFFFF", font="-size 10").place(x=40,y=110)
    #contacto textbox
    e1 = Entry(reg_screen, textvariable=_phone2,width='17')
    e1.place(x=120,y=110)
    #email label
    Label(reg_screen, text="Email:",fg="#FFFFFF",bg="#1b6f10", font="-size 10").place(x=260,y=110)
    #email textbox
    Entry(reg_screen, textvariable=_email,width='29').place(x=310,y=110)
    # email Label
    
    ## PODE SER IMPORTANTE ESTA LABEL PARA A PARTE DO CRIAR UMA PESSOA NOVA
    
    #Label(reg_screen, text="Preencha na forma:       yyyy-mm-dd",bg="#1b2f40",fg="#faa507", font="-size 7").place(x=90, y=160)
    Label(reg_screen, text="Data de Nascimento:",bg="#1b6f10", fg="#FFFFFF", font="-size 10").place(x=40, y=150)
    # email textbox
    Entry(reg_screen, textvariable=_dob, width=25).place(x=180, y=150)
    
    Label(reg_screen, text="Sexo:",fg="#FFFFFF",bg="#1b6f10", font="-size 10").place(x=40, y=200)
    Entry(reg_screen, textvariable=_gender, width=10).place(x=110, y=200)
    
    
    Label(reg_screen, text="Departamento:",fg="#FFFFFF",bg="#1b6f10", font="-size 10").place(x=310, y=200)
    Entry(reg_screen, textvariable=_depcode, width=10).place(x=420, y=200)

    Label(reg_screen, text="Função:",fg="#FFFFFF",bg="#1b6f10", font="-size 10").place(x=40, y=250)
    Entry(reg_screen, textvariable=_funcao, width=20).place(x=110, y=250)
    
    Label(reg_screen, text="Salário:",fg="#FFFFFF",bg="#1b6f10", font="-size 10").place(x=350, y=250)
    Entry(reg_screen, textvariable=_salary, width=10).place(x=420, y=250)
    
    
    Label(reg_screen, text="Nome utilizador:",fg="#FFFFFF",bg="#1b6f10", font="-size 10").place(x=40, y=300)
    Entry(reg_screen, textvariable=_username,width=25).place(x=150, y=300)
    #Label(reg_screen, text="*Para novo registo, inicie o nome de utilizador com 'es'",bg="#1b2f40",fg="#faa507", font="-size 7").place(x=40, y=260)
    
    Label(reg_screen, text="Palavra-passe:",fg="#FFFFFF", bg="#1b6f10", font="-size 10").place(x=40, y=350)
    Entry(reg_screen, textvariable=_password,width=25).place(x=150, y=350)
    
    
    ###### BOTOES DO FIM
    
    # Button(reg_screen, text="Adicionar pessoa", width=17, height=1, bg="#faa507",font="-weight bold -size 10",borderwidth=2, relief="solid", command=lambda: adicionar()).place(x=70,y=420)
    # Button(reg_screen, text="Editar informações", width=17, height=1, bg="#faa507",font="-weight bold -size 10",borderwidth=2, relief="solid", command=lambda: editar()).place(x=220,y=420)
    # Button(reg_screen, text="Ver staff", width=17, height=1, bg="#faa507",font="-weight bold -size 10",borderwidth=2, relief="solid", command=lambda: staff()).place(x=70,y=450)
    # Button(reg_screen, text="Ver departamentos", width=17, height=1, bg="#faa507",font="-weight bold -size 10",borderwidth=2, relief="solid", command=lambda: dept()).place(x=220,y=450)    
    
    
    #####  ÚNICO BOTAO QUE É PRECISO AQUI
    
    b_save=Button(reg_screen, text="Save", width=17, height=1, bg="#faa507", font="-weight bold -size 10",borderwidth=2, relief="solid", command=lambda: save_ad())
    b_save.place(x=160,y=420)
    
    reg_screen.mainloop()
    
    #ONDE COLOCAR???
    
        

    



# def staff():
#     reg_screen.destroy()
#     from forms.Form_Staff import Staff_tk
#     Staff_tk()

# def dept():
#     reg_screen.destroy()
#     from forms.Form_Departamentos import Dept_tk
#     Dept_tk()




if __name__ == "__main__":
    ap = Adicionar_tk()
