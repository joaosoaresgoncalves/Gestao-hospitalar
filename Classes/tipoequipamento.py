# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 19:26:59 2022

@author: marti
"""

import os

class Tipo_equipamento:
    
    obj=dict()
    lst=list()
    att = ["_code","_nome"]
    
    def __init__(self, code,nome):
        
        self._code = code
        self._nome=nome

        
        Tipo_equipamento.obj[self._code] = self

        Tipo_equipamento.lst.append(self._code)
    
    # name property getter method
    @property
    def nome(self):
        return self._nome
        
        
    @classmethod
    def write(cls, path = ''):
        if len(cls.lst) > 0:
            
            path = os.getcwd()
            path = path.replace("\\", '/')
            a = "/"
            while path[-1] != a:
                path = path[:-1]

            #file = path + "forms/" + cls.__name__ + '.csv'
            
            fh = open(path + "forms/" + cls.__name__ + '.csv', 'w')
            
            #fh = open('./forms/Tipo_equipamento' + '.csv', 'w')
            p = cls.obj[cls.lst[0]]
            strprint = ""
            for att in list(p.__dict__.keys()):
                strprint += att[1:] + ';'
            fh.write(strprint[:-1] + '\n')
            for p in cls.obj.values():
                fh.write(p.__str__() + '\n')
            fh.close()
        
    # @classmethod
    # def write2(cls, path = ''):
    #     if len(cls.lst) > 0:
    #         fh = open('../forms/Equipamento2' + '.csv', 'w')
    #         p = cls.obj[cls.lst[0]]
    #         strprint = ""
    #         for att in list(p.__dict__.keys()):
    #             strprint += att[1:] + ';'
    #         fh.write(strprint[:-1] + '\n')
    #         for p in cls.obj.values():
    #             fh.write(p.__str__() + '\n')
    #         fh.close()
        
    @classmethod
    def read(cls, path = ''):
        cls.obj = dict()
        cls.lst = list()
        
        path = os.getcwd()
        path = path.replace("\\", '/')
        a = "/"
        while path[-1] != a:
            path = path[:-1]

        file = path + "forms/" + cls.__name__ + '.csv'
        
        try:
            #file = path + cls.__name__ + '.csv'
            fh = open(file, 'r')
            fh.readline()
            for p in fh:
                cls.from_string(p.strip())
            fh.close()
        except FileNotFoundError:
            print(f"{file} data file not found, a new one will be created")
        except BaseException as err:
            print(f"Error in read method:\n{err}\n{type(err)}")
        
    @classmethod
    def from_string(cls, str_data):
        str_list = str_data.split(";")
        strarg = 'cls(str_list[0]'
        for i in range(1, len(str_list)):
            strarg += ',str_list[' + str(i) + ']'
        strarg += ')'
        return eval(strarg)
    # Reset the class
    def __str__(self):
        strprint = "f'"
        for att in type(self).att:
            strprint += '{self.' + att + '};'
        strprint = strprint[:-1] + "'"
    
        return eval(strprint)
    
    @classmethod
    def remove(cls, p):
        cls.lst.remove(p)
        del cls.obj[p]
    
    def __str__(self):
        strprint = "f'"
        for att in type(self).att:
            strprint += '{self.' + att + '};'
        strprint = strprint[:-1] + "'"
        return eval(strprint)