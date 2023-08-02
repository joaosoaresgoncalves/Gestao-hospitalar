# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:22:56 2022

@author: marti
"""
from forms.Form_Login import Form_Login
#import tkinter as tk
import tkinter as tk
from tkinter import *
from  tkinter import  ttk
from Classes.departamento import Departamento
from Classes.equipamento import Equipamento
from Classes.tipoequipamento import Tipo_equipamento
from tkinter import messagebox

def Dept_tk():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Departamentos")
    #setting height and width of screen
    reg_screen.geometry("1100x600")
    # filepath = filepath
    # obj = Equipamento.first()
    att = Equipamento.att
    reg_screen.configure(bg="#2b9f90")
    

    
    global name_code
    global name_code2
    global _code
    global _nome
    global _quantidade
    global _qualidade_media
    global _cod_departamento
    global _cod_tipo
    global tipo
    global _n_qnt
    global entr_dep
    global entr_tequi
    name_code2 = StringVar()
    _n_qnt = IntVar()
    _tipo = StringVar()
    _code = IntVar()
    _nome = StringVar()
    _quantidade = IntVar()
    _qualidade_media = StringVar()
    _cod_departamento = IntVar()
    _cod_tipo = IntVar()
    entr_dep = StringVar()
    entr_tequi = StringVar()
    
  
    # Create_Navigation_buttons()
    def writeTree():
        # if len(str(_phone.get())) !=9:
        #     messagebox.askokcancel("Dados inválidos", "o seu número tem de ter 9 algarismos")
        # elif len(lista[0])!=4 or len(lista[1])!=2 or len(lista[2])!=2:
        #     messagebox.askokcancel("Dados inválidos", "a data tem de estar no formato AAAA-MM-DD")
        # elif datetime.date.fromisoformat(_dob.get())>=datetime.date.today():
        #     messagebox.askokcancel("Dados inválidos", "a data ainda não aconteceu")
        try:
            code = len(Equipamento.lst) + 1
            e1 = Equipamento(code,_nome.get(),_quantidade.get(),_qualidade_media.get(),_cod_departamento.get(),_cod_tipo.get())
            Equipamento.write()
            fillTree()
        except:
            messagebox.askokcancel("Erro", "Input mal colocado")
            
    def fillTree():
        x = tv.get_children()
        for item in x:
            tv.delete(item)
        
        
        for n in range(len(Equipamento.obj)):
            p = Equipamento.obj[Equipamento.lst[n]]
            for i in range(len(Tipo_equipamento.obj)):
                t = Tipo_equipamento.obj[Tipo_equipamento.lst[i]]
                if t._code == p._cod_tipo :
                    tipo = t._nome
            try:
                tv.insert(parent='', index ='end',iid=n ,text='', values = (p._code,p._nome,p._quantidade,p._qualidade_media,p._cod_departamento,tipo,p._cod_tipo) )
            except:
                tv.insert(parent='', index ='end',iid=n ,text='', values = (p._code,p._nome,p._quantidade,p._qualidade_media,p._cod_departamento,"NA",p._cod_tipo) )
    def dep():
        Departamento.read()
        for n in range(len(Departamento.obj)):
            d = Departamento.obj[Departamento.lst[n]]
            if d._name == entr_dep.get():
                name_code = d._code
        x = tv.get_children()
        for item in x:
            tv.delete(item)
        # print(name_code)
        Tipo_equipamento.read()
        j = 0
        for n in range(len(Equipamento.obj)):
            p = Equipamento.obj[Equipamento.lst[n]]
            for i in range(len(Tipo_equipamento.obj)):
                t = Tipo_equipamento.obj[Tipo_equipamento.lst[i]]
                if t._code == p._cod_tipo :
                    tipo = t._nome
            if p._cod_departamento == name_code:
                tv.insert(parent='', index ='end',iid=j ,text='', values = (p._code,p._nome,p._quantidade,p._qualidade_media,p._cod_departamento,tipo,p._cod_tipo) )
                j = j+1
                

                
    def selectItem(a):
        index2 = tv.focus()
        p = Equipamento.obj[Equipamento.lst[int(index2)]]
        _code.set(p._code)
        _nome.set(p._nome)
        _quantidade.set(p._quantidade)
        _qualidade_media.set(p._qualidade_media)
        _cod_departamento.set(p._cod_departamento)
        Tipo_equipamento.read()
        for i in range(len(Tipo_equipamento.obj)):
            t = Tipo_equipamento.obj[Tipo_equipamento.lst[i]]
            if t._code == p._cod_tipo :
                _tipo.set(t._nome)


    def alterar():
        index2 = tv.focus()
        p2 = Equipamento(_code.get(),_nome.get(),_n_qnt.get(),_qualidade_media.get(),_cod_departamento.get(),_cod_tipo.get())
        Equipamento.obj[str(Equipamento.lst[int(index2)])] =p2
        _n_qnt.set("")
        # Equipamento.write()
        fillTree()
    
        
    def tequi():
        Tipo_equipamento.read()
        for n in range(len(Tipo_equipamento.obj)):
            t = Tipo_equipamento.obj[Tipo_equipamento.lst[n]]
            if t.nome == entr_tequi.get():
                name_code2 = t._code
        x = tv.get_children()
        for item in x:
            tv.delete(item)
        j = 0
        for n in range(len(Equipamento.obj)):
            p = Equipamento.obj[Equipamento.lst[n]]
            for i in range(len(Tipo_equipamento.obj)):
                t = Tipo_equipamento.obj[Tipo_equipamento.lst[i]]
                if t._code == p._cod_tipo :
                    tipo = t._nome
            if p._cod_tipo == str(name_code2):
                tv.insert(parent='', index ='end',iid=j ,text='', values = (p._code,p._nome,p._quantidade,p._qualidade_media,p._cod_departamento,tipo,p._cod_tipo) )
                j = j+1
        
    def limpar():
        _code.set("")
        _nome.set("")
        _quantidade.set("0")
        _qualidade_media.set("")
        _cod_departamento.set("0")
        _cod_tipo.set("0")
        _tipo.set("")
        
    def abrir():
        #reg_screen.destroy()
        from forms.Form_graf import Graph
        Graph()
            
    def remove2():
        Equipamento.read()
        index2 = tv.focus()
        Equipamento.remove(Equipamento.lst[int(index2)])
        fillTree()
        
    def voltar():
        reg_screen.destroy()
        from forms.Perfil import Perfil_tk
        Perfil_tk(Form_Login.code)

    


    Equipamento.read()
    Tipo_equipamento.read()
    #main frame
    f_main = LabelFrame(reg_screen,text = "Equipamentos",bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_main.grid(row = 0,column = 0)
    
    f_dep =Frame(f_main,bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_dep.grid(row = 0,column = 0)
    
    f_tequi =Frame(f_main,bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_tequi.grid(row = 0,column = 1)
    
    f_add = LabelFrame(f_main,text = "Adicionar",bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_add.grid(row = 1,column = 0)
    
    f_alterar = LabelFrame(f_main,text = "Alterar a quantidade",bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_alterar.grid(row = 0,column = 2)
    
    f_tv = LabelFrame(f_main,text = "Equipamento",bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_tv.grid(row =1,column = 1,pady = 10,columnspan = 2)
    
    f_graf =Frame(f_main,bd = 4,relief = GROOVE,padx = 10,pady = 10)
    f_graf.grid(row = 2,column = 0)

# def Create_Edit_buttons(self):
    # f_main.configure(bg="#2b9f90")
    # f_dep.configure(bg="#2b9f90")
    # f_add.configure(bg="#2b9f90")
    # f_tv.configure(bg="#2b9f90")

    # create a vertical scrollbar
    scrollbar_V = Scrollbar(f_tv)
    scrollbar_V.pack(side = RIGHT , fill = Y)
    
    # create a horizontal scrollbar
    scrollbar_H = Scrollbar(f_tv,orient = 'horizontal')
    scrollbar_H.pack(side = BOTTOM , fill = X)    
    # selectmode = "extended" -> default, multi line select
    # selectmode = "browse" -> one line select
    # selectmode = "none" - desabled
    tv = ttk.Treeview(f_tv ,yscrollcommand = scrollbar_V.set,xscrollcommand = scrollbar_H.set, selectmode = "browse")
    tv.pack(fill = None,expand = True)
    # tv = ttk.Treeview(f_tv)
    # tv.pack()
    
    # Configure  scrollbars
    scrollbar_V.config(command= tv.yview)
    scrollbar_H.config(command= tv.xview)
 

# Binding Treview


    tv["columns"] = ("code","nome","quantidade","qualidade_media","cod_departamento","tipo","cod_tipo")
    tv.column('code',width = 50,minwidth = 0,stretch = False)
    tv.column('nome',width = 50,minwidth = 0,stretch = False)
    tv.column('quantidade',width =100 ,minwidth = 0,stretch = False)
    tv.column('qualidade_media',width = 150,minwidth = 0,stretch = False)
    tv.column('cod_departamento',width = 150,minwidth = 0,stretch = False)
    tv.column('tipo',width = 50,minwidth = 0,stretch = False)
    tv.column('cod_tipo',width = 100,minwidth = 0,stretch = False)

    tv['show'] = 'headings'
    tv.heading("code",text = "code")
    tv.heading("nome",text = "nome")
    tv.heading("quantidade",text = "quantidade")
    tv.heading("qualidade_media",text = "qualidade")
    tv.heading("cod_departamento",text = "cod_departamento")
    tv.heading("tipo",text = "tipo")
    tv.heading("cod_tipo",text = "cod_tipo")
    


    btn_add = Button(f_add,text = "Adicionar",command = lambda: writeTree())
    btn_add.grid(row = 8,column = 0)
    btn_add = Button(f_add,text = "Apagar",command = lambda: remove2())
    btn_add.grid(row = 8,column = 1)
    btn_add = Button(f_alterar,text = "Alterar",command = lambda: alterar())
    btn_add.grid(row = 8,column = 3)
    btn_add = Button(f_add,text = "Clear",command = lambda: limpar())
    btn_add.grid(row = 8,column = 2)
    
    tv.bind('<ButtonRelease-1>',selectItem)
    lbl_dep = Label(f_dep,text  = "Departamento")
    lbl_dep.grid(row = 0,column = 0, padx = 10,pady = 10)
    # entr_dep = Entry(f_dep)
    # entr_dep.grid(row = 0,column = 1)
    btn_ver_dep = Button(f_dep,text = "Ver equipamentos",command = lambda: dep())
    btn_ver_dep.grid(row = 1,column = 0)
    
    lbl_tequi = Label(f_tequi,text  = "Tipo")
    lbl_tequi.grid(row = 0,column = 0, padx = 10,pady = 10)
    # entr_tequi = Entry(f_tequi)
    # entr_tequi.grid(row = 0,column = 1)
    btn_ver_tequi = Button(f_tequi,text = "Ver equipamentos",command = lambda: tequi())
    btn_ver_tequi.grid(row = 1,column = 0)
    
    btn_graf = Button(f_graf,text = "Ver gráfico",command = lambda: abrir())
    btn_graf.grid(row = 1,column = 1)
    btn_voltar = Button(f_graf,text = "<<",command = lambda: voltar())
    btn_voltar.grid(row = 1,column = 0)
    
    # lbl_tipo = Label(f_add,text = "Código")
    # lbl_tipo.grid(row = 1,column = 0, padx = 10,pady = 10)
    lbl_tipo = Label(f_add,text = "Nome")
    lbl_tipo.grid(row = 2,column = 0, padx = 10,pady = 10)
    lbl_qnt = Label(f_add,text = "Quantidade")
    lbl_qnt.grid(row = 3,column = 0, padx = 10,pady = 10)
    lbl_qual = Label(f_add,text = "Qualidade")
    lbl_qual.grid(row = 4,column = 0, padx = 10,pady = 10)
    lbl_cod_dep = Label(f_add,text = "Código Departamento")
    lbl_cod_dep.grid(row = 5,column = 0, padx = 10,pady = 10)
    lbl_cod_tipo = Label(f_add,text = "tipo")
    lbl_cod_tipo.grid(row = 6,column = 0, padx = 10,pady = 10)
    lbl_cod_tipo = Label(f_add,text = "Código Tipo")
    lbl_cod_tipo.grid(row = 7,column = 0, padx = 10,pady = 10)
    lbl_cod_tipo = Label(f_alterar,text = "Nova quantidade:")
    lbl_cod_tipo.grid(row = 0,column = 0, padx = 10,pady = 10)
    
    # entr_cod = Entry(f_add,textvariable = _code)
    # entr_cod.grid(row = 1,column = 1)
    entr_tipo = Entry(f_add,textvariable = _nome)
    entr_tipo.grid(row = 2,column = 1)
    entr_qnt = Entry(f_add,textvariable = _quantidade)
    entr_qnt.grid(row = 3,column = 1)
    entr_qual = Entry(f_add,textvariable = _qualidade_media)
    entr_qual.grid(row = 4,column = 1)
    entr_cod_dep = Entry(f_add,textvariable = _cod_departamento)
    entr_cod_dep.grid(row = 5,column = 1)
    entr_tipo = Entry(f_add,textvariable = _tipo)
    entr_tipo.grid(row = 6,column = 1)
    entr_cod_tipo = Entry(f_add,textvariable = _cod_tipo)
    entr_cod_tipo.grid(row = 7,column = 1)
    entr_nova_qnt = Entry(f_alterar,textvariable = _n_qnt)
    entr_nova_qnt.grid(row = 0,column = 1)
    
    # ldep=Label(f_ger, text='Departamento:')
    # ldep.grid()
    #ldep.grid(row=1, column=1)
    dep_cbox = ttk.Combobox(f_dep,textvariable = entr_dep)
    dep_cbox["values"] = ["Administracao","Urgencia","Cirurgia","Consultas","Analises"]
    dep_cbox2 = ttk.Combobox(f_tequi,textvariable = entr_tequi)
    dep_cbox2["values"] = ["doacoes","tecnologico","clinico","cirurgia"]
    dep_cbox.grid(row = 0,column = 1,padx = 10,pady = 10)
    dep_cbox2.grid(row = 0,column = 1,padx = 10,pady = 10)
    # dep_cbox.bind("<<ComboboxSelected>>",filtrar())
    # btn_add = Button(f_ger,text = "Ver",command = lambda: filtrar())
    # btn_add.grid(row = 1,column = 0)
    

    fillTree()
    # code2 = len(Equipamento.lst) + 1
        
    
    
    
    
        

    # for item in tv.get_children():
    #     tv.delete(item)
    
    # Create_frames()
    # treeview()
    # create_columns()
    # create_headings()
    # labels_entries()
    # fillTree()
    
    # if len(tv.get_children()) > 0:
    #     tv.focus(tv.get_children()[0])
    #     tv.selection_set(tv.get_children()[0])
        
    # Create_Edit_buttons()
    Departamento.read()
    
    
    reg_screen.mainloop()
        

        
        

if __name__ == "__main__":
    ap = Dept_tk()
