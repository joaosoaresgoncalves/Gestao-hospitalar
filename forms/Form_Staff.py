"""
Created on Mon Jun 13 22:55:07 2022

@author: joaog
"""
import datetime
import tkinter as tk
from tkinter import *
from  tkinter import  ttk
# from Classes.departamento import Departamento
# from Classes.equipamento import Equipamento
# from Classes.tipoequipamento import Tipo_equipamento
from forms.Form_Login import Form_Login
from Classes.pessoa import Pessoa
from Classes.departamento import Departamento
from tkinter import messagebox

def  Staff_tk():
    global name_code2
    global reg_screen
    reg_screen = Tk()
    reg_screen.title("Pessoa")
    reg_screen.geometry("1100x600")
    att =Pessoa.att
    reg_screen.configure(bg="#2b9f90")
    global _code
    global _name
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
    global _tipo
    global sel_dep
    global ger_code
    global entr_ger
    global depcode
    global sel_novo_ger
    global novo_ger
    _code = IntVar()
    _name = StringVar()
    _funcao = StringVar()
    _dob = StringVar() ##???
    _gender = StringVar()
    _nif = IntVar()
    _salary = IntVar()
    _email = StringVar()
    _phone = IntVar()
    _depcode = StringVar()
    _username = StringVar()
    _password = StringVar()
    _tipo = StringVar()
    sel_dep = StringVar()
    ger_code = StringVar()
    entr_ger = StringVar()
    depcode = StringVar()
    sel_novo_ger = StringVar()
    novo_ger = StringVar()
    
    
    
    def fillTree():
        x = tv.get_children()
        for item in x:
            tv.delete(item)
     
        for n in range(len(Pessoa.obj)):
            p = Pessoa.obj[Pessoa.lst[n]]
            tv.insert(parent='', index ='end',iid=n ,text='', values = (p._code,p._name,p._funcao) )
        
        
        

    
    
    
    def adicionar():
        l1 = ["Administracao","Urgencia","Cirurgia","Consultas","Analises"]
        lista=_dob.get().strip().split("-")
        if len(str(_phone.get())) !=9:
            messagebox.askokcancel("Dados inválidos", "o seu número tem de ter 9 algarismos")
        elif len(lista[0])!=4 or len(lista[1])!=2 or len(lista[2])!=2:
            messagebox.askokcancel("Dados inválidos", "a data tem de estar no formato AAAA-MM-DD")
        elif not is_valid_date(int(lista[0]),int(lista[1]),int(lista[2])):
            messagebox.askokcancel("Dados inválidos", "a data invalida")
        elif datetime.date.fromisoformat(_dob.get())>=datetime.date.today():
            messagebox.askokcancel("Dados inválidos", "a data ainda não aconteceu")
        elif (_gender.get()!="F" and _gender.get()!="M"):
            messagebox.askokcancel("Dados inválidos", "o género não existe")
        elif _depcode.get() not in l1:
            messagebox.askokcancel("Dados inválidos", "o departamento não existe")
            
        else:
            
            code = len(Pessoa.lst) + 1
            depcode = ""
            for n in range(len(Departamento.obj)):
                d = Departamento.obj[Departamento.lst[n]]
                if d.name == _depcode.get():
                    depcode = d._code
            p1 = Pessoa(code,_name.get(),_funcao.get(),_dob.get(),_gender.get(),_nif.get(),_salary.get(),_email.get(),_phone.get(),depcode,_username.get(),_password.get(),_tipo.get())
            Pessoa.write()
            fillTree()
            
    def is_valid_date(year, month, day):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year%4==0 and (year%100 != 0 or year%400==0):
            day_count_for_month[2] = 29
        return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
            
        
        
        
    def selectItem(a):
        index2 = tv.focus()
        p = Pessoa.obj[Pessoa.lst[int(index2)]]
        _name.set(p._name)
        _dob.set(p._dob)
        _gender.set(p._gender)
        _nif.set(p._nif)
        _funcao.set(p._funcao)
        _salary.set(p._salary)
        _email.set(p._email)
        _phone.set(p._phone)
        _tipo.set(p._tipo)
        _username.set(p._username)
        _password.set(p._password)

        
        name_code2 = ""
        Departamento.read()
        for n in range(len(Departamento.obj)):
            d = Departamento.obj[Departamento.lst[n]]
            if d.code == p._depcode:
                name_code2 = d.name
        _depcode.set(name_code2)
        _code.set(p._code)
        # Tipo_equipamento.read()
        # for n in range(len(Equipamento.obj)):
        #     p = Equipamento.obj[Equipamento.lst[n]]
        #     for i in range(len(Tipo_equipamento.obj)):
        #         t = Tipo_equipamento.obj[Tipo_equipamento.lst[i]]
        #         if t._code == p._cod_tipo :
        #             tipo = t._nome
        # if tipo != "NA":
        #     _tipo.set(tipo)
        # elif tipo == "NA":
        #     tipo.set("")
        # _cod_tipo.set(p._cod_tipo) 
    
    def limpar():
        _name.set("")
        _dob.set("")
        _gender.set("")
        _nif.set("")
        _funcao.set("")
        _salary.set("")
        _email.set("")
        _phone.set("")
        _tipo.set("")
        _username.set("")
        _password.set("")
        _depcode.set("")
        
        
    def change_gerente():
        name_code2 = ""
        name_code3 = ""
        # ger_code = ""
        # cod_ant = ""
        Departamento.read()
        for n in range(len(Departamento.obj)):
            d = Departamento.obj[Departamento.lst[n]]
            if d.name == sel_dep.get():
                name_code2 = d._code
                ger_code = d._gerentecode
            
        
        for n in range(len(Pessoa.obj)):
            p = Pessoa.obj[Pessoa.lst[n]]
            if p._name == novo_ger.get() and p._depcode == name_code2 :
                if p._code != ger_code:
                    cod_ant = p.code
        
        
        try:
            for n in range(len(Departamento.obj)):
                d = Departamento.obj[Departamento.lst[n]]
                if d.name == sel_dep.get():
                    d._gerentecode = cod_ant
        except:
            messagebox.askokcancel("Erro", "O user não existe neste departamento")
        novo_ger.set("")
            
        Departamento.write2()
                    



            
                
        
        
        # obj=Departamento.obj(dep)
        
        # a=obj.cg_gerente(new_gerente)
        # if a == 0:
        #     # e1['text']=###################codigo da pessoa que esta la
        #     messagebox.askokcancel("Dados inválidos", "o novo gerente tem de pertencer ao departamento")
            
        # else:
        #       entr_fdep['text']=obj.name
            
        
            

        
    
    
    # def ger():
    #     Departamento.read()
    #     for n in range(len(Departamento.obj)):
    #         d = Departamento.obj[Departamento.lst[n]]
    #         if d.name == sel_dep.get():
    #             entr_fdep.set(d._code)
                
                
        
        
    def filtrar():
        name_code2 = ""
        Departamento.read()
        for n in range(len(Departamento.obj)):
            d = Departamento.obj[Departamento.lst[n]]
            if d.name == sel_dep.get():
                name_code2 = d._code
                ger_code = d._gerentecode
        x = tv.get_children()
        for item in x:
            tv.delete(item)
        i = 0
        for n in range(len(Pessoa.obj)):
            p = Pessoa.obj[Pessoa.lst[n]]
            # for i in range(len(Tipo_equipamento.obj)):
            #     t = Tipo_equipamento.obj[Tipo_equipamento.lst[i]]
            #     if t._code == p._cod_tipo :
            #         tipo = t._nome
            if p._depcode == str(name_code2):
                tv.insert(parent='', index ='end',iid=i ,text='', values = (p._code,p._name,p._funcao) )
                i = i+1
        i = 0
        for n in range(len(Pessoa.obj)):
            p = Pessoa.obj[Pessoa.lst[n]]
            # for i in range(len(Tipo_equipamento.obj)):
            #     t = Tipo_equipamento.obj[Tipo_equipamento.lst[i]]
            #     if t._code == p._cod_tipo :
            #         tipo = t._nome
            if p._depcode == str(name_code2) and p._code == ger_code:
                entr_ger.set(p.name)

    def remove():
        index2 = tv.focus()
        Pessoa.remove(Pessoa.lst[int(index2)])
        fillTree()
    
    def voltar():
        reg_screen.destroy()
        from forms.Perfil import Perfil_tk
        Perfil_tk(Form_Login.code)
        
    Pessoa.read()   
    f_main = LabelFrame(reg_screen,text = "Pessoas",bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_main.grid(row = 0,column = 0)
    
    f_dep =Frame(f_main,bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_dep.grid(row = 0,column = 0)
    
    f_ger =Frame(f_main,bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_ger.grid(row = 0,column = 1)
    
    f_tv = LabelFrame(f_main,text = "Pessoas",bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_tv.grid(row =1,column = 1,pady = 10,columnspan = 2)
    
    f_add = LabelFrame(f_main,text = "Adicionar",bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_add.grid(row = 1,column = 0)
    
    f_graf =Frame(f_main,bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_graf.grid(row = 2,column = 0)
    
    scrollbar_V = Scrollbar(f_tv)
    scrollbar_V.pack(side = RIGHT , fill = Y)
    
    # create a horizontal scrollbar
    scrollbar_H = Scrollbar(f_tv,orient = 'horizontal')
    scrollbar_H.pack(side = BOTTOM , fill = X)    
    # selectmode = "extended" -> default, multi line select
    # selectmode = "browse" -> one line select
    # selectmode = "none" - desabled
    tv = ttk.Treeview(f_tv ,yscrollcommand = scrollbar_V.set,xscrollcommand = scrollbar_H.set, selectmode = "browse")
    tv.pack()
    # tv = ttk.Treeview(f_tv)
    # tv.pack()
    
    # Configure  scrollbars
    scrollbar_V.config(command= tv.yview)
    scrollbar_H.config(command= tv.xview)
    
    tv["columns"] = ("code","nome","funcao")
    tv.column('code',width = 100,minwidth = 0,stretch = False)
    tv.column('nome',width = 100,minwidth = 0,stretch = False)
    tv.column('funcao',width =100 ,minwidth = 0,stretch = False)
    # tv.column('dob',width = 100,minwidth = 0,stretch = False)
    # tv.column('gender',width = 100,minwidth = 0,stretch = False)
    # tv.column('nif',width = 100,minwidth = 0,stretch = False)
    # tv.column('email',width = 100,minwidth = 0,stretch = False)
    # tv.column('salary',width = 100,minwidth = 0,stretch = False)
    # tv.column('phone',width = 100,minwidth = 0,stretch = False)
    # tv.column('depcode',width = 100,minwidth = 0,stretch = False)
    # tv.column('tipo',width = 50,minwidth = 0,stretch = False)
    
    ##combobox
    ldep=Label(f_ger, text='Departamento:')
    ldep.grid()
    #ldep.grid(row=1, column=1)
    lbl_dep = Label(f_ger,text  = "Departamento:")
    lbl_dep.grid(row = 0,column = 0, padx = 10,pady = 10)
    dep_cbox = ttk.Combobox(f_ger,textvariable = sel_dep)
    dep_cbox["values"] = ["Administracao","Urgencia","Cirurgia","Consultas","Analises"]
    dep_cbox.grid(row = 1,column = 0,padx = 10,pady = 10)
    # dep_cbox.bind("<<ComboboxSelected>>",filtrar())
    btn_add = Button(f_ger,text = "Ver",command = lambda: filtrar())
    btn_add.grid(row = 2,column = 0)
    
    


    tv['show'] = 'headings'
    tv.heading("code",text = "code")
    tv.heading("nome",text = "nome")
    tv.heading("funcao",text = "funcao")
    # tv.heading("dob",text = "dob")
    # tv.heading("gender",text = "gender")
    # tv.heading("nif",text = "nif")
    # tv.heading("salary",text = "salary")
    # tv.heading("phone",text = "phone")
    # tv.heading("email",text = "phone")
    # tv.heading("depcode",text = "depcode")
    # tv.heading("tipo",text = "tipo")
    
    # code, name, funcao, dob, gender, nif, salary, email, phone, depcode, username, password, tipo
    
    lbl_Nome = Label(f_add,text = "Nome")
    lbl_Nome.grid(row = 2,column = 0, padx = 10,pady = 10)
    lbl_funcao = Label(f_add,text = "Função")
    lbl_funcao.grid(row = 3,column = 0, padx = 10,pady = 10)
    lbl_dob = Label(f_add,text = "Data nascimento")
    lbl_dob.grid(row = 4,column = 0, padx = 10,pady = 10)
    lbl_gender = Label(f_add,text = "Genero ")
    lbl_gender.grid(row = 5,column = 0, padx = 10,pady = 10)
    lbl_nif = Label(f_add,text = "NIF")
    lbl_nif.grid(row = 6,column = 0, padx = 10,pady = 10)
    lbl_salary = Label(f_add,text = "Salário")
    lbl_salary.grid(row = 7,column = 0, padx = 10,pady = 10)
    lbl_email = Label(f_add,text = "Email")
    lbl_email.grid(row = 2,column = 2, padx = 10,pady = 10)
    lbl_phone = Label(f_add,text = "Telemóvel")
    lbl_phone.grid(row = 3,column = 2, padx = 10,pady = 10)
    lbl_username = Label(f_add,text = "User")
    lbl_username.grid(row = 4,column = 2, padx = 10,pady = 10)
    # lbl_pass = Label(f_add,text = "password")
    # lbl_pass.grid(row = 5,column = 2, padx = 10,pady = 10)
    lbl_tipo = Label(f_add,text = "Tipo")
    lbl_tipo.grid(row = 5,column = 2, padx = 10,pady = 10)
    lbl_dep = Label(f_add,text = "Departamento")
    lbl_dep.grid(row = 6,column = 2, padx = 10,pady = 10)
    #lbl_dep = Label(f_ger,text  = "Gerente:")
    
    ######################################################### parte de mudar gerente
    lbl_dep = Label(f_dep,text  = "Gerente:")
    lbl_dep.grid(row = 0,column = 0, padx = 10,pady = 10)
    entr_fdep = Entry(f_dep,state='readonly',textvariable = entr_ger)
    entr_fdep.grid(row = 0,column = 1)
    # dep=dep_cbox.get()
    # print(dep)
    
    # lbl_dep = Label(f_dep,text  = "Gerente:")
    # lbl_dep.grid(row = 0,column = 0, padx = 10,pady = 10)
    # entr_fdep = Entry(f_dep, state='readonly', textvariable=dep_cbox.get())
    # entr_fdep.grid(row = 0,column = 1)
    
    

    
    e1=Entry(f_dep,textvariable = novo_ger)
    e1.grid(row = 1,column = 1, padx=5, pady=5)
    
    b1=Button(f_dep, text='Alterar gerente', command= lambda: change_gerente())
    b1.grid(row=1, column=0, padx=5, pady=5)
    
    lbl_dep = Label(f_dep,text  = "Clicar no 'ver' para aplicar")
    lbl_dep.grid(row = 2,column = 0, padx = 10,pady = 10)
    
    # e1=Entry(f_dep, textvariable=dep)
    # e1.grid(row = 1,column = 1, padx=5, pady=5)
    
    
###########################################################

    
# _code = IntVar()
# _name = StringVar()
# _funcao = StringVar()
# _dob = StringVar() ##???
# _gender = StringVar()
# _nif = IntVar()
# _salary = IntVar()
# _email = StringVar()
# _phone = IntVar()
# _depcode = IntVar()
# _username = StringVar()
# _password = StringVar()
# _tipo = StringVar()
    
    # entr_cod = Entry(f_add,textvariable = _code)
    # entr_cod.grid(row = 1,column = 1)
    entr_Nome = Entry(f_add,textvariable = _name)
    entr_Nome.grid(row = 2,column = 1)
    entr_funcao = Entry(f_add,textvariable = _funcao)
    entr_funcao.grid(row = 3,column = 1)
    entr_dob = Entry(f_add,textvariable = _dob)
    entr_dob.grid(row = 4,column = 1)
    entr_gender = Entry(f_add,textvariable = _gender)
    entr_gender.grid(row = 5,column = 1)
    entr_nif = Entry(f_add,textvariable = _nif)
    entr_nif.grid(row = 6,column = 1)
    entr_salary = Entry(f_add,textvariable = _salary)
    entr_salary.grid(row = 7,column = 1)
    entr_email = Entry(f_add,textvariable = _email)
    entr_email.grid(row = 2,column = 3)
    entr_phone = Entry(f_add,textvariable = _phone)
    entr_phone.grid(row = 3,column = 3)
    entr_username = Entry(f_add,textvariable = _username)
    entr_username.grid(row = 4,column = 3)
    #entr_pass = Entry(f_add,textvariable = _password)
    #entr_pass.grid(row = 5,column = 3)
    entr_tipo = Entry(f_add,textvariable = _tipo)
    entr_tipo.grid(row = 5,column = 3)
    entr_dep2 = Entry(f_add,textvariable = _depcode)
    entr_dep2.grid(row = 6,column = 3)


    obj=Pessoa.obj[Form_Login.code]   
    #obj=Form_Login.code
    #print(obj)
    if obj.tipo == 'admin':

        btn_add = Button(f_add,text = "Adicionar",command = lambda: adicionar())
        btn_add.grid(row = 8,column = 0)
        btn_add = Button(f_add,text = "Clear",command = lambda: limpar())
        btn_add.grid(row = 8,column = 1)
        btn_add = Button(f_add,text = "Apagar",command = lambda: remove())
        btn_add.grid(row = 8,column = 2)
        
    btn_voltar = Button(f_graf,text = "<<",command = lambda: voltar())
    btn_voltar.grid(row = 1,column = 0)

    tv.bind('<ButtonRelease-1>',selectItem)
    fillTree()
    reg_screen.mainloop()
    
    
if __name__ == "__main__":
    ap = Staff_tk()
