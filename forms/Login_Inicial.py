# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:28:37 2022

@author: marti
"""

from Classes.pessoa import Pessoa
from forms.Form_Login import Form_Login
from tkinter import *
from tkinter import ttk

loginResult = "???"

loginf = Form_Login() # VAI VER COMO ESTÁ NO FORM LOGIN ...EXECUTA O FORM
loginResult = loginf.login_Status


if loginResult == 'Not Login':
    print( "not login")
else:
    print('login')


   # 1,filePath=''
   
   #,ncols = 2 ,filePath = './'