# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:43:44 2021

@author: Windows 11
"""
"""
#Fun1 Dado uma data de inicio confinamento e da pesagem, calcular o delta D
def dataInConfinamento(self, m):
    from datetime import date
    
    print('====Data Inicio Confinamento====')
    diaMaxC = self.choices.get('time')[0]*30
    #print(diaMaxC)
    
    while True:  
        
        try:
            ano = int(input("digite o ano do Inicio Confinamento "))
            data = date.today().year
            if ano >data or ano < data -2:
                raise ValueError
            else:
                break
        except ValueError:
                print('Data invalida digite de novo')
    print(ano)
    
    while True:
        try:
            mes = int(input("digite o mes do Inicio Confinamento "))
            data = date.today().month
            if  mes  < 1 or mes > data:
                raise ValueError
            else:
                break
        except ValueError:
            print('Data invalida digite de novo')        
    print(mes)
    while True:
        
        try:
            try:
                dia = int(input("digite o dia do Inicio Confinamento "))
                #data = date.month
                if dia > 31 or dia  < 1:
                    raise ValueError                              
            except ValueError:
                print('Data errada tente novamente')
                    
            diaInit = date(ano, mes, dia)
            #print('diaInit: ', diaInit)
            diah = date.today()
            #print('diah: ', diah)
            delta = int((diah - diaInit).days)
            print('delta: ', delta)
            
            if delta > diaMaxC:
                raise ValueError
            else:
                break   
        except ValueError:
            print('Data excede 0s dias de confinamento, tente de novo')
    
    self.diaInit = diaInit
    print("Dia Inicio Confinamento: ", diaInit)   
    print('____Fim Data Inicio Confinamento_____')
    print('_____________________________________________________')
    
    print('======================Data Pesagem=====================================')
def dataPesagem(self, m):    
    
    from datetime import date
    resp = input('Se a pesagem e hoje digite s, do contrário digite qq tecla ')
    #resp = 's'     #######tirar
    if resp == 's' or resp == 'S':
        diap = date.today()
    else:
        while True:
            try:
                ano = int(input("digite o ano da Pesagem "))
                data = date.today().year
                if ano != data:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Data invalida digite de novo')
        while True:
            try:
                mes = int(input("digite o mes da Pesagem "))
                data = date.today().month
                if mes > data or mes  < 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Data invalida digite de novo')
        while True:        
            try:
                dia = int(input("digite o dia da Pesagem "))
                data = date.today().day
                if dia > 31 or dia  < 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Data invalida digite de novo') 
        diap = date(ano, mes, dia)  
    
    self.D = int((diap - self.diaInit).days) 
    print('self.diaInit====> ', self.diaInit)
    print('diap====> ', diap)
    print('self.D====> ', self.D, '\n')

def pesagem(self, m):          
    
    print('===Imprime peso médio teórico para a data da pesagem e o real==')
    pesoMedioTeorico = int(dictPeso.get(self.D))
    print('peso medio Teorico :', pesoMedioTeorico, '\n')
   
    #self.pesoNaPesagem =300 #tirar isto
    self.pesoNaPesagem =  int(input('Digite o peso medio dos animais encontrado na pesagem: '))
    print('peso na pesagem no dia D; ', self.pesoNaPesagem, '\n')
    
    self.DP = (self.pesoNaPesagem-pesoMedioTeorico)
    print('Delta: ', self.DP, '\n')
    
    print('peso Inicial', self.choices.get('peso_medio')[0])
    self.GDPnew = (self.pesoNaPesagem-self.choices.get('peso_medio')[0])/(self.D)
    print('self.GDPnew', self.GDPnew, '\n')
    #print(self.choices)
    print('_____Fim Funcao 1 de Pesagem_____')
    """

