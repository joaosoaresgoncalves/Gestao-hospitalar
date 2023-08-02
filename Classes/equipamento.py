# -*- coding: utf-8 -*-

import os
from Classes.departamento import Departamento
from Classes.tipoequipamento import Tipo_equipamento


class Equipamento:
    
    obj=dict()
    lst=list()
    att = ['_code','_nome','_quantidade',"_qualidade_media","_cod_departamento","_cod_tipo"]
    
    def __init__(self, code,nome, quantidade, qualidade_media, cod_departamento,cod_tipo):
        
        self._code = code
        self._nome=nome
        self._quantidade=quantidade
        self._qualidade_media=qualidade_media
        self._cod_departamento=cod_departamento
        self._cod_tipo=cod_tipo
        
        Equipamento.obj[self._code] = self

        Equipamento.lst.append(self._code)
        
    @classmethod
    def para_o_graf(cls):

        Equipamento.read()

        doacoes=0
        tecnologico=0
        clinico=0
        cirurgia=0


        for key in Equipamento.obj:

            equipamento= Equipamento.obj[key]

            if int(equipamento._cod_tipo)==1:

                doacoes=doacoes + int(equipamento._quantidade)

            elif int(equipamento._cod_tipo)==2:

                tecnologico=tecnologico+int(equipamento._quantidade)

            elif int(equipamento._cod_tipo)==3:

                clinico=clinico+int(equipamento._quantidade)

            elif int(equipamento._cod_tipo)==4:
                cirurgia=cirurgia + int(equipamento._quantidade)

        return [doacoes, tecnologico, clinico, cirurgia]
    
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
        
        #file = path + cls.__name__ + '.csv'
        fh = open(file, 'r')
        fh.readline()
        for p in fh:
            cls.from_string(p.strip())
        fh.close()
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
        
        