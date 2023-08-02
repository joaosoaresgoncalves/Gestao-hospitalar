# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:15:15 2022

@author: marti
"""
import datetime
from Classes.gclass import Gclass
import os
#from Classes.departamento import Departamento

class Pessoa(Gclass):

    obj = dict()

    lst = list()
    
    pos = 0
    
    att = ['_code','_name','_funcao', '_dob', '_gender','_nif', '_salary', '_email', '_phone', '_depcode', '_username', '_password', '_tipo']
    
    path = os.getcwd()
    path = path.replace("\\", '/')
    a = "/"
    
    while path[-1] != a:
        path = path[:-1]

    
    
    lista_dep=[]
    f1=open(path + '/forms/Departamento' + '.csv', 'r')
    for line in f1:
        m=line.split(';')
        if m[0]!='':
            lista_dep.append(m[0])
    f1.close()
    
    def __init__(self, code, name, funcao, dob, gender, nif, salary, email, phone, depcode, username, password, tipo):
        super().__init__()
        self._code = code
        self._name = name
        self._funcao = funcao
        self._dob = datetime.date.fromisoformat(dob)
        self._gender=gender
        self._nif=nif
        self._salary = float(salary)
        self._email = email
        self._phone=phone
        self._depcode= depcode
        self._username=username

        self._password=password
        
        # self._gerente='Não'
        
        self._tipo=tipo
        
        Pessoa.obj[self._code] = self
        
        Pessoa.lst.append(self._code)
        
        
    
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
        fh = open(file, 'r')
        fh.readline()
        for p in fh:
            cls.from_string(p.strip())
        fh.close()

            
            
    # def __init__(self, *args):
    #     if len(args)==10:
    #         self._code = max(Pessoa.lst)+1
    #         self._name = args[0]
    #         self._dob = datetime.date.fromisoformat(args[1])
    #         self._gender=args[2]
    #         self._firstday = datetime.date.fromisoformat(args[3])
    #         self._nif=args[4]
    #         self._salary = float(args[5])
    #         self._phone=args[6]
    #         self._password=args[9]
    #         self._username=args[8]
            
    #         self._depcode= args[7]
    #         self._gerente='Não'
            
    #     elif len(args)==12:
    #         self._code = args[0]
    #         self._name = args[1]
    #         self._dob = datetime.date.fromisoformat(args[2])
    #         self._gender=args[3]
    #         self._firstday = datetime.date.fromisoformat(args[4])
    #         self._nif=args[5]
    #         self._salary = float(args[6])
    #         self._phone=args[7]
    #         self._password=args[10]
    #         self._username=args[9]
            
    #         self._depcode= args[8]
    #         self._gerente=args[11]
            
    
    # @classmethod
    # def read(cls, path = '../forms/'):
    #     cls.obj = dict()
    #     cls.lst = list()
    #     file = path + cls.__name__ + '.csv'
    #     fh = open(file, 'r')
    #     fh.readline()
    #     for p in fh:
    #         cls.from_string(p.strip())
    #     fh.close()
        # except FileNotFoundError:
        #     print(f"{file} data file not found, a new one will be created")
        # except BaseException as err:
        #     print(f"Error in read method:\n{err}\n{type(err)}")
        


    @property
    def code(self):
        return self._code
    
    @classmethod
    def write(cls):
        if len(cls.lst) > 0:
            fh = open("../forms/Pessoa.csv", 'w')
            p = cls.obj[cls.lst[0]]
            strprint = ""
            for att in list(p.__dict__.keys()):
                strprint += att[1:] + ';'
            fh.write(strprint[:-1] + '\n')
            for p in cls.obj.values():
                fh.write(p.__str__() + '\n')
            fh.close()
            
    @classmethod
    def reset(cls):
        cls.obk = dict()
        cls.lst = list()
        cls.pos = 0

###################################  VERIFICAR, N É PRECISO 
    # @code.setter
    # def code(self, code):
    #     self._code = code
    #     n=Funcionario.lst.index(self._code)
    #     Funcionario.lst.pop(n)
    #     Funcionario.lst.insert(n, code)
        
    # name property getter method
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def funcao(self):
        return self._funcao
    
    @funcao.setter
    def funcao(self, funcao):
        self._funcao = funcao
        
        
    @property    
    def depcode(self):
        return self._depcode
 
#####################################  VERIFICAR
    @depcode.setter
    def depcode(self, depcode):
        if str(depcode) in Pessoa.lista_dep:
            self._depcode=depcode
        else:
            print ('Department does not exist!')
    
    
    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, dob):
        self._dob = datetime.date.fromisoformat(dob)

    @property
    def firstday(self):
        return self._firstday

    @firstday.setter
    def firstday(self, firstday):
        self._firstday = datetime.date.fromisoformat(firstday)
        
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        perc = (salary - self.salary) / self.salary
        if perc < 0 or perc > 0.2:
            print("Salary cannot be reduced or increased by more than 20%")
        else:
            self._salary = salary
            
    @property
    def nif(self):
        return self._nif

    @property
    def gender(self):
        return self._gender
    
    @nif.setter
    def nif(self, nif):
        self._nif=nif
        
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        self._phone=phone
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email=email
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
        
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username
    
    @property
    def tipo(self):
        return self._tipo
    
    # age property getter method
    @property
    def age(self):
        tday = datetime.date.today()
        age = tday.year - self.dob.year
        if tday.month < self.dob.month or \
            (tday.month == self.dob.month and tday.day < self.dob.day):
            age -= 1
        return age
    
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
    def __str__(self):
        strprint = "f'"
        for att in type(self).att:
            strprint += '{self.' + att + '};'
        strprint = strprint[:-1] + "'"
    
        return eval(strprint)

    # @property
    # def years_experience(self):
    #     tday = datetime.date.today()
    #     yrs = tday.year - self.firstday.year
    #     if tday.month < self.firstday.month or \
    #         (tday.month == self.firstday.month and tday.day < self.firstday.day):
    #         yrs -= 1
    #     return yrs


#code; name; dob; gender; firstday; nif; salary; phone; depcode; username; password


# p1=Pessoa(12, 'To', '2013-08-17', 'M', '2013-08-17', 123, 1234, 123, 0, 'm123', '123')

# print(p1.code)

# p1.depcode = 2
# print(p1.depcode)








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

