# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 14:01:41 2021

@author: rogerio
"""

class geraPesagem():
    
    def __init__(self, choices, dictPeso):
        self.choices  = choices 
        self.dictPeso = dictPeso
        
    #Fun1 Dado uma data de inicio confinamento e da pesagem, calcular o delta D
    def dataInConfinamento(self):
        from datetime import date
        print(60*'=')
        print('Data Inicio Confinamento')
        diaMaxC = self.choices.get('time')[0]*30
        print('Dias totais de confinamento', diaMaxC)
        print(60*'=')
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
        #print(ano)
        
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
        #print(mes)
        print(60*'=')
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
        print(60*'=')
        print("Dia Inicio Confinamento: ", diaInit)
        print(60*'=')
        print('____Fim Data Inicio Confinamento_____')
        
        print(2*'\n','=== Data Pesagem=====================================')
    def dataPesagem(self):    
        
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
        print(60*'=')
        print('Data Pesagem ====> ', self.diaInit)
        print('Dia da Pesagem====> ', diap)
        print('Delta = self.D ====> ', self.D, '\n')
        print(60*'=')
        ('____Fim Data Pesagem_____________________')

        print('______Calcula e gera dados pesagem_______')
    def pesagem(self):          
        #print(self.D)
        #print(self.choices.get('peso_medio')[0])
        #print(self.dictPeso)
        #stop= input('stop')
        print(60*'=')
        print('Imprime peso médio teórico para a data da pesagem e o real==')
        pesoMedioTeorico = self.dictPeso.get(str(self.D))
        self.pesoNaPesagem =  int(input('Digite o peso medio dos animais encontrado na pesagem: '))
        self.DP = round(((self.pesoNaPesagem-pesoMedioTeorico)),2)
        #print('Peso Inicial Animal', self.choices.get('peso_medio')[0])
        self.GDPnew = round(((self.pesoNaPesagem-self.choices.get('peso_medio')[0])/(self.D)),2)
        
        print(60*'=')
        print('Peso medio Teorico no dia D:', pesoMedioTeorico)
        print('Peso na pesagem no dia D: ', self.pesoNaPesagem)
        print('Delta: ', self.DP)
        print('Imprime GDPnew:', self.GDPnew, )
        print(60*'=', 1*'\n')
        
        print('_____Fim Funcao 1 de Pesagem_____')
