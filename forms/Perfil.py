# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 01:23:34 2022

@author: marti
"""

#import tkinter as tk
from tkinter import *
from  tkinter import ttk
from tkinter import messagebox
from Classes.pessoa import Pessoa


def Perfil_tk(codigo):
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Perfil")
    #setting height and width of screen
    reg_screen.geometry("520x520")
    
    reg_screen.configure(bg="#89CFF0")
    
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
    global _phone
    global _depcode    
    global _username
    global _password
    
    
    obj = Pessoa.obj[codigo]
    print(obj)
    
    _code = IntVar()
    _nome = StringVar()
    _funcao = StringVar()
    _phone = IntVar()
    _email=StringVar()
    _gender=StringVar()
    _dob=StringVar()
    _nif=IntVar()
    _salary=IntVar()
    _depcode=IntVar()
    _username=StringVar()
    _password=StringVar()
 
    _code.set(obj.code)
    _nome.set(obj.name)
    _funcao.set(obj.funcao)
    _phone.set(obj.phone)
    _email.set(obj.email)
    _gender.set(obj.gender)
    _dob.set(obj.dob)
    _nif.set(obj.nif)
    _salary.set(obj.salary)
    _depcode.set(obj.depcode)
    _username.set(obj.username)
    _password.set(obj.password)
    
    print(_code.get())
    
 


    def editar(code):
            
        #from Classes.pessoa import Pessoa
        ########## É PRECISO DAR ENABLE A 4 TEXTBOXES
        #print(type(code))
        #obj = Pessoa.current()
        #obj = Pessoa.obj[code]
        #print(obj)
        #self.state_entries('normal')
       
        # obj.code = _code.get()
        # obj.nome = _nome.get()
        # obj.funcao = _funcao.get()
        # obj.gender = _gender.get()
        # obj.dob =  _dob.get()
        # obj.nif = _nif.get()
        # obj.salary = _salary.get()
        # obj.depcode = _depcode.get()

        t1['state']='disabled'
        t2['state']='disabled'
        t3['state']='normal'
        t4['state']='normal'
        t5['state']='disabled'
        t6['state']='disabled'
        t7['state']='disabled'
        t8['state']='disabled'
        t9['state']='disabled'
        t10['state']='normal'
        t11['state']='normal'
        
        b_save['state']='normal'
        b_editar['state']='disabled'
        
        # obj.phone = _phone.get()
        # obj.email = _email.get()
        # obj.username = _username.get()
        # obj.password = _password.get()
        
    def save():
        # Pessoa.read()
        #obj=Pessoa.obj[code]
        obj=Pessoa.obj[codigo]
        
        if   len(str(_phone.get())) !=9:
           # top = Tkinter.Tk()
            messagebox.askokcancel("Nova pessoa", "O número tem de ter 9 algarismos.")
            
        else:
            
            obj.phone=_phone.get()
            obj.email=_email.get()
            obj.username=_username.get()
            obj.password=_password.get()
                
            #Pessoa.phone=_phone.get()
            #Pessoa.email=_email.get()
            #Pessoa.username=_username.get()
            #Pessoa.password=_password.get()
                
            #obj=Pessoa.current()
            
            Pessoa.write()
            
            
        t1['state']='readonly'
        t2['state']='readonly'
        t3['state']='readonly'
        t4['state']='readonly'
        t5['state']='readonly'
        t6['state']='readonly'
        t7['state']='readonly'
        t8['state']='readonly'
        t9['state']='readonly'
        t10['state']='readonly'
        t11['state']='readonly'
        
        b_save['state']='disabled'
        b_editar['state']='normal'

#######################

    
    message=StringVar()
    
    Label(reg_screen, text="                     Perfil                                                                                  ", bg="#1b2f40", fg='#faa507', font="-weight bold -size 15").place(x=0,y=18)
    
    Label(reg_screen, text="Nome:",bg="#1b2f40",fg="#FFFFFF", font="-size 10").place(x=40,y=70)
    #name textbox
    t1=Entry(reg_screen, textvariable=_nome, width='30', state='readonly' )
    t1.place(x=95,y=70)

    Label(reg_screen, text="Código:",bg="#1b2f40",fg="#FFFFFF", font="-size 10").place(x=300,y=70)
    #name textbox
    t2=Entry(reg_screen, textvariable=_code, width='20' ,state='readonly')
    t2.place(x=365,y=70)

    #contacto Label
    Label(reg_screen, text="Contacto:",bg="#1b2f40",fg="#FFFFFF", font="-size 10").place(x=40,y=110)
    #contacto textbox
    t3=Entry(reg_screen, textvariable=_phone,width='17',state='readonly')#.place(x=120,y=110)
    t3.place(x=120,y=110)
    #email label
    Label(reg_screen, text="Email:",fg="#FFFFFF",bg="#1b2f40", font="-size 10").place(x=260,y=110)
    #email textbox
    t4=Entry(reg_screen, textvariable=_email,width='29',state='readonly')
    t4.place(x=310,y=110)
    # email Label
    
    ## PODE SER IMPORTANTE ESTA LABEL PARA A PARTE DO CRIAR UMA PESSOA NOVA
    
    #Label(reg_screen, text="Preencha na forma:       yyyy-mm-dd",bg="#1b2f40",fg="#faa507", font="-size 7").place(x=90, y=160)
    Label(reg_screen, text="Data de Nascimento:",bg="#1b2f40", fg="#FFFFFF", font="-size 10").place(x=40, y=150)
    # email textbox
    t5=Entry(reg_screen, textvariable=_dob, width=25,state='readonly')
    t5.place(x=180, y=150)
    
    Label(reg_screen, text="Sexo:",fg="#FFFFFF",bg="#1b2f40", font="-size 10").place(x=40, y=200)
    t6=Entry(reg_screen, textvariable=_gender, width=10,state='readonly')
    t6.place(x=110, y=200)
    
    
    Label(reg_screen, text="Departamento:",fg="#FFFFFF",bg="#1b2f40", font="-size 10").place(x=310, y=200)
    t7=Entry(reg_screen, textvariable=_depcode, width=10,state='readonly')
    t7.place(x=420, y=200)

    Label(reg_screen, text="Função:",fg="#FFFFFF",bg="#1b2f40", font="-size 10").place(x=40, y=250)
    t8=Entry(reg_screen, textvariable=_funcao, width=20,state='readonly')
    t8.place(x=110, y=250)
    
    Label(reg_screen, text="Salário:",fg="#FFFFFF",bg="#1b2f40", font="-size 10").place(x=350, y=250)
    t9=Entry(reg_screen, textvariable=_salary, width=10,state='readonly')
    t9.place(x=420, y=250)
    
    
    Label(reg_screen, text="Nome utilizador:",fg="#FFFFFF",bg="#1b2f40", font="-size 10").place(x=40, y=300)
    t10=Entry(reg_screen, textvariable=_username,width=25,state='readonly')
    t10.place(x=150, y=300)
    #Label(reg_screen, text="*Para novo registo, inicie o nome de utilizador com 'es'",bg="#1b2f40",fg="#faa507", font="-size 7").place(x=40, y=260)
    
    Label(reg_screen, text="Palavra-passe:",fg="#FFFFFF", bg="#1b2f40", font="-size 10").place(x=40, y=350)
    t11=Entry(reg_screen, textvariable=_password,width=25,state='readonly')
    t11.place(x=150, y=350)
    
    
    ###### BOTOES DO FIM
    
    #Button(reg_screen, text="Adicionar pessoa", width=17, height=1, bg="#faa507",font="-weight bold -size 10",borderwidth=2, relief="solid").place(x=70,y=420)
    b_editar=Button(reg_screen, text="Editar informações", width=17, height=1, bg="#faa507",font="-weight bold -size 10",borderwidth=2, relief="solid", command=lambda: editar(int(_code.get())))
    b_editar.place(x=70,y=420)
    Button(reg_screen, text="Ver staff", width=17, height=1, bg="#faa507",font="-weight bold -size 10",borderwidth=2, relief="solid", command=lambda: staff()).place(x=70,y=450)
    Button(reg_screen, text="Ver departamentos", width=17, height=1, bg="#faa507",font="-weight bold -size 10",borderwidth=2, relief="solid", command=lambda: dept()).place(x=220,y=450)    
    
    #ADICIONAR
    b_save=Button(reg_screen, text="Save", width=17, height=1, bg="#faa507", font="-weight bold -size 10",borderwidth=2, relief="solid", state='disabled', command=lambda: save())
    b_save.place(x=220,y=420)
    reg_screen.mainloop()
        

############################### FUNCOES

def staff():
    reg_screen.destroy()
    from forms.Form_Staff import Staff_tk
    Staff_tk()

def dept():
    reg_screen.destroy()
    from forms.Form_Departamentos import Dept_tk
    Dept_tk()
        
# def adicionar():
#     from forms.Form_Adicionar import Adicionar_tk
#     Adicionar_tk()


        


# def editar(code):
#     print(type(code))
#     obj = Pessoa.current()
#     print(obj)
#     self.state_entries('normal')
    
#     obj.code = _code.get()
#     obj.nome = _nome.get()
#     obj.funcao = _funcao.get()
#     obj.gender = _gender.get()
#     obj.dob self=  _dob.get()
#     obj.nif = _nif.get()
#     obj.salary = _salary.get()
#     obj.depcode = _depcode.get()
#     t1['state']='enabled'
    
#     obj.phone = _phone.get()
#     obj.email = _email.get()
#     obj.username = _username.get()
#     obj.password = _password.get()
    
#     .state_entries('readonly')
        
    
    
    
    
    
    
    
    
    
    
    
    #    from Classes.pessoa import Pessoa
    #     ########## É PRECISO DAR ENABLE A 4 TEXTBOXES
    #     #print(type(code))
    #     #obj = Pessoa.current()
    #     #obj = Pessoa.obj[code]
    #     #print(obj)
    #     #self.state_entries('normal')
       
    #     # obj.code = _code.get()
    #     # obj.nome = _nome.get()
    #     # obj.funcao = _funcao.get()
    #     # obj.gender = _gender.get()
    #     # obj.dob =  _dob.get()
    #     # obj.nif = _nif.get()
    #     # obj.salary = _salary.get()
    #     # obj.depcode = _depcode.get()
    #     ############################## OS QUE FAZ SENTIDO DAR PARA MUDAR
    #     t1['state']='enabled' ########???????????????
    #     # obj.phone = _phone.get()
    #     # obj.email = _email.get()
    #     # obj.username = _username.get()
    #     # obj.password = _password.get()
    
        #self.state_entries('readonly')

    #?




#######################

    
    


###########################
        

# if __name__ == "__main__":
#     ap = Perfil_tk(1)