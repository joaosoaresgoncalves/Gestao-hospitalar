# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:55:59 2022

@author: marti
"""

# Class Person - generic version with inheritance
#from classes.gclass import Gclass

import datetime
import os
from Classes.gclass import Gclass
from Classes.pessoa import Pessoa

class Departamento:
    obj = dict()
    lst = list()
    # pos = 0
    # sortkey = ''
    # auto_number = 0
    # # Attribute names list, identifier attribute must be the first one
    att = ['_code','_name','_local',"_gerentecode"]
    # auto_number = 1      # Uncomment in case of auto number on
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, local, gerentecode):
        # Object attributes
        self._code = code
        self._name = name
        self._local = local
        self._gerentecode=gerentecode
        
        # Add the new object to the dictionary of objects
        Departamento.obj[code] = self
        # Add the code to the list of object codes
        Departamento.lst.append(code)

    # code property getter method
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, code):
        self._code = code
    # name property getter method
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def local(self):
        return self._local

    @local.setter
    def local(self, local):
        self._local = local
        
    
    @property
    def gerentecode(self):
        return self.gerentecode
    
    def cg_gerente(self, new_gerente):
        obj=Pessoa.obj[new_gerente]
        if obj.depcode != self.code:
            return 0
        else:
            self._gerentecode=new_gerente
            return 1
    
    @classmethod
    def read(cls, path = '../forms/'):
        cls.obj = dict()
        cls.lst = list()
        #file = path + cls.__name__+ '.csv'
        
        path = os.getcwd()
        path = path.replace("\\", '/')
        a = "/"
        while path[-1] != a:
            path = path[:-1]

        file = path + "forms/" + cls.__name__ + '.csv'
        
        fh = open(file, 'r')
        fh.readline()
        for p in fh:
            cls.from_string(p.strip())
        fh.close()
        # except FileNotFoundError:
        #     print(f"{file} data file not found, a new one will be created")
        # except BaseException as err:
        #     print(f"Error in read method:\n{err}\n{type(err)}")
        
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
    def write2(cls, path = ''):
        if len(cls.lst) > 0:
            
            path = os.getcwd()
            path = path.replace("\\", '/')
            a = "/"
            while path[-1] != a:
                path = path[:-1]

            #file = path + "forms/" + cls.__name__ + '.csv'
            
            fh = open(path + "forms/" + cls.__name__ + '.csv', 'w')
            
            #fh = open('../forms/Departamento' + '.csv', 'w')
            p = cls.obj[cls.lst[0]]
            strprint = ""
            for att in list(p.__dict__.keys()):
                strprint += att[1:] + ';'
            fh.write(strprint[:-1] + '\n')
            for p in cls.obj.values():
                fh.write(p.__str__() + '\n')
            fh.close()
    
    @classmethod
    def remove(cls, p):
        cls.lst.remove(p)
        del cls.obj[p]
        
    @classmethod
    def from_string(cls, str_data):
         str_list = str_data.split(";")
         strarg = 'cls(str_list[0]'
         for i in range(1, len(str_list)):
             strarg += ',str_list[' + str(i) + ']'
         strarg += ')'
         return eval(strarg)
     
        
     
     # Reset the class
    # def __str__(self):
    #      strprint = "f'"
    #      for att in type(self).att:
    #          strprint += '{self.' + att + '};'
    #      strprint = strprint[:-1] + "'"
     
    #      return eval(strprint)
     
    #  def __str__(self):
    #      strprint = "f'"
    #      for att in type(self).att:
    #          strprint += '{self.' + att + '};'
    #      strprint = strprint[:-1] + "'"
    #      return eval(strprint)
         
    # def __str__(self):
    #     strprint = "f'"
    #     for att in list(self.__dict__.keys()):
    #         strprint += '{self.' + att + '};'
    #     strprint = strprint[:-1] + "'"
    #     return eval(strprint)
    # @gerentecode.setter 
    # def gerentecode(self, gerentecode):
    #     if gerentecode in Funcionario.lst:
    #         if Funcionario.lst[gerentecode].obj[depcode]==self._code or Funcionario.lst[gerentecode].obj[depcode]=='':
    #             self._gerentecode=gerentecode
    #         else return 'Invalid'
            
    #     else return
        
    
    
    
    






#################################################        
# generic code: no need to change for a new class    
    # Class method to implement constructor overloading
    # @classmethod
    # def from_string(cls, str_data):
    #     str_list = str_data.split(";")
    #     strarg = 'cls(str_list[0]'
    #     for i in range(1, len(str_list)):
    #         strarg += ',str_list[' + str(i) + ']'
    #     strarg += ')'
    #     return eval(strarg)
    # # Reset the class
    # @classmethod
    # def reset(cls):
    #     cls.obk = dict()
    #     cls.lst = list()
    #     cls.pos = 0
    # # Class methods to iterate (forward and backward) through the class objects
    # @classmethod
    # def nextrec(cls):
    #     cls.pos += 1
    #     return cls.current()
    # @classmethod
    # def previous(cls):
    #     cls.pos -= 1
    #     return cls.current()
    # @classmethod
    # def current(cls, code = None):
    #     if code in cls.lst:
    #         cls.pos = cls.lst.index(code)
    #     if cls.pos < 0:
    #         cls.pos = 0
    #         return None
    #     elif cls.pos >= len(cls.lst):
    #         cls.pos = len(cls.lst) - 1
    #         return None
    #     else:
    #         code = cls.lst[cls.pos]
    #         return cls.obj[code]
    # @classmethod
    # def first(cls):
    #     cls.pos = 0
    #     return cls.current()
    # @classmethod
    # def last(cls):
    #     cls.pos = len(cls.lst) - 1
    #     return cls.current()
    # # Object delete method
    # @classmethod
    # def remove(cls, p):
    #     cls.lst.remove(p)
    #     del cls.obj[p]
    # # Sort objects by attribute class methods
    # @classmethod
    # def orderfunc(cls, e):
    #     return getattr(cls.obj[e], cls.sortkey)
    # @classmethod
    # def sort(cls, att, reverse = False):
    #     cls.sortkey = att
    #     cls.lst.sort(key=cls.orderfunc, reverse= reverse)
    # # Find objects having an attribute equal to value
    # @classmethod
    # def find(cls, value, att):
    #     lobj = cls.obj.values()
    #     fobj = [obj for obj in lobj if getattr(obj, att) == value]
    #     return fobj
    # # Get a list of objects attribute values
    # @classmethod
    # def getatlist(cls, att):
    #     return [getattr(obj, att) for obj in list(cls.obj.values())]
    # # Write object to csv file
    # @classmethod
    # def write(cls, path = ''):
    #     if len(cls.lst) > 0:
    #         fh = open(path + cls.__name__ + '.csv', 'w')
    #         p = cls.obj[cls.lst[0]]
    #         strprint = ""
    #         for att in list(p.__dict__.keys()):
    #             strprint += att[1:] + ';'
    #         fh.write(strprint[:-1] + '\n')
    #         for p in cls.obj.values():
    #             fh.write(p.__str__() + '\n')
    #         fh.close()
    # # Read objects from csv file
    # @classmethod
    # def read(cls, path = ''):
    #     cls.obj = dict()
    #     cls.lst = list()
    #     try:
    #         fh = open(path + cls.__name__ + '.csv', 'r')
    #         fh.readline()
    #         for p in fh:
    #             cls.from_string(p.strip())
    #         fh.close()
    #     except:
    #         pass
    # # Instance method to obtain object info
    # def __str__(self):
    #     strprint = "f'"
    #     for att in list(self.__dict__.keys()):
    #         strprint += '{self.' + att + '};'
    #     strprint = strprint[:-1] + "'"
    #     return eval(strprint)

