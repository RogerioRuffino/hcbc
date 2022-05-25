# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:35:51 2021

@author: rogerio
"""
'''
import sys
sys.path.append('C:/Users/rogerio/Dropbox/My PC (DESKTOP-CGHB6PD)/Documents/Rogerio/rogerPythonTkinterApps/rogerEngordaBezerrosPyhon/App/Spyder/AppsRunning/')
from DtInSpy311021 import *
'''
#global commoditiesBez
commoditiesBez = {'leitePo': [150.0, 10.0, 1.5], 'leite': [2.0, 1.0, 2.0], 'silo': [254.0, 1000, 0.254], 'racao': [85.0, 40.0, 2.125]}

class entradasBez():

    def __init__(self,

                  commoditiesBez = { },
                  
                  leitePo       = 30.00,
                  leitePo_kg    = 60,
                  
                  leite         = 50.00,
                  leite_l       = 40,
                  
                  silo          = 250.00,
                  silo_kg       = 1,
                  
                  racao         = 64.00,
                  racao_kg      = 40,):
                  
                  self.commoditiesBez = {'leitePo': [150.0, 10.0, 1.5], 'leite': [2.0, 1.0, 2.0], 'silo': [254.0, 1000, 0.254], 'racao': [85.0, 40.0, 2.125]}
                  self.leitePo = leitePo
                  self.leitePo_kg = leitePo_kg
                  self.leite = leite
                  self.leite_l =leite_l
                  self.silo = silo
                  self.silo_kg = silo_kg
                  self.racao = racao
                  self.racao_kg = racao_kg
                  
                  print('commoditiesBez =', commoditiesBez)    
    
    def checkErrFloat(self, texto):
        
        global a
        while True:
          try:
               a = float(input("Digite o %s: "%(texto)))
               if a <= 0 or a is  str: 
                    raise ValueError
               break                    
          except ValueError:
               print('Entrada invalida digite de novo')
        return a
    
    def self_in(self, m):
        global texto
        print (5*('\n'))
        #self.commoditiesBez['Descrição|'] = ['Preço em R$', 'Peso da Saca', 'Preço por Kg']
        print (m*'_')   #Entrada dados leite em po
        self.leitePo = entradasBez().checkErrFloat('preço saca de leite em pó')
        self.leitePo_kg = entradasBez().checkErrFloat('peso saca de leite em pó')
        self.commoditiesBez['leitePo'] = [self.leitePo, self.leitePo_kg, (self.leitePo/self.leitePo_kg)/100]
        
        print (5*('\n'))
        print (m*'_')   #Entrada dados leite
        self.leite = entradasBez().checkErrFloat('preço do litro de leite')
        self.leite_l = 1.00
        self.commoditiesBez['leite'] = [self.leite, self.leite_l, self.leite/self.leite_l]
        
        print (5*('\n'))
        print (m*'_')   #Entrada dados Silagem
        self.silo = entradasBez().checkErrFloat('preço saca de silagem')
        self.silo_kg = 1000
        self.commoditiesBez['silo'] = [self.silo, self.silo_kg, self.silo/self.silo_kg]
        print(self.commoditiesBez)
        
        print (5*('\n'))
        print (m*'_')   #Entrada dados Racao
        self.racao = entradasBez().checkErrFloat('preço saca de ração')
        self.racao_kg = entradasBez().checkErrFloat('peso saca de ração')
        self.commoditiesBez['racao'] = [self.racao, self.racao_kg, self.racao/self.racao_kg]
        print(m*'_')
        
        print(self.commoditiesBez)
        print(m*'_')
    
    def print_commoditiesBez(self, m):
        #self.commoditiesBez.update({'Tipos': ['R$', 'Kg', 'R$/Kg'] })
        
        lcommoditiesBezKeys = [ (key) for key in self.commoditiesBez.keys()]
        lcommoditiesBezKeys.insert(0,'Commodities')
        lcommoditiesBezValues = [ (value) for value in self.commoditiesBez.values()]
        lcommoditiesBezValues.insert(0, ['R$', 'Kg', 'R$/Kg'])
        dnew = dict(zip(lcommoditiesBezKeys, lcommoditiesBezValues))
        
        print(m*'_')           
        import pandas as pd   
        #from tabulate import tabulate        
        
        print (2*'\n')
        print(m*'_')
        print ('{:^75}'.format('Tabela de Resultados'))
        print(m*'=')
        
        #df = pd.DataFrame(self.listaVar, index=self.listaNomes, columns=['Valores', 'Unidades']) 
        #df = pd.DataFrame((lcommoditiesBezKeys), index=(lcommoditiesBezValues), columns=[ 'Tipos', R$', 'Kg', 'R$/Kg']) 
        
        df = pd.DataFrame(dnew)
        #print(df)
    
        blankIndex=[''] * len(df)  #Tira a aprimeira coluna
        df.index=blankIndex
        df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
        #print(df.to_markdown(index=False)) 
        
        print(df_tr)
        print('')
        #print(df.to_string(index=False))
      
        print(m*'_')
        
'============================================================================' 
#x = entradasBez()
#x.self_in(85)
#print (x.commoditiesBez)
class logicaBez (entradasBez):
    
    def __init__(self,
                 
                 dictPesoCostBez={},
                 step               = 1,
                 dia                = 0 ,
                 ldias              = [],
                 lPeso1to3          = [],
                 lPeso              = [],
                 lracaoPer100       = [],
                 lracaoPer100_kg    = [],
                 lracao_kg          = [],
                 lracaoCost         = [],
                 lleiteCons         = [],
                 lleitePoCons       = [],
                 
                 lleiteCruCost      = [],
                 lleitePoCost       = [],
                 lleiteAllCost      = [],
                 lCustoTotal        = [],
                 lCustoTotalAcum    = [],
                  
                 cTMD               = 0,
                 pAMD               = 0,
                 pvAMD              = 0,
                 lucroAMD           = 0,
                 timePeso           = {}):
        super().__init__(
                  commoditiesBez,
                  leitePo = 30.00,
                  leitePo_kg = 60,
                  leite = 50.00,
                  leite_l = 40,
                  silo = 250.00,
                  silo_kg = 1,
                  racao = 64.00,
                  racao_kg = 40, )
        
        self.lPeso              = lPeso
        self.lracaoPer100       = lracaoPer100
        self.lracao_kg          = lracao_kg
        self.lracaoPer100_kg    = lracaoPer100_kg
        self.lracaoCost         = lracaoCost
        self.lleiteCons         = lleiteCons
        self.lleitePoCons       = lleitePoCons
        self.lleiteCruCost      = lleiteCruCost
        self.lleitePoCost       = lleitePoCost
        self.lleiteAllCost      = lleiteAllCost
        self.lCustoTotal        = lCustoTotal
        self.lCustoTotalAcum    = lCustoTotalAcum
        
        self.dictPesoCostBez    = dictPesoCostBez
        
        self.step    = step
        self.dia     = dia
        self.cTMD    = cTMD
        self.PAMD    = pAMD
        self.pvAMD   = pvAMD
        self.lucroAMD    = lucroAMD
        self.timePeso    = timePeso
        #self.ldias = [i for i in range(meses*30)]
        
        print(self.commoditiesBez)
        '''
    def checkErrChoiceGDP(self, text):
         
         #global b
         while True:
           try:
                b = int(input(text))       
                if b is str:
                    raise ValueError
                elif  b >3 or b<0: 
                    raise ValueError
                break
           except ValueError:
                print('Entrada invalida digite de novo')
        return b
        '''
         
        print('1','Define o numero de dias aceitavel ate atingir 85 kg')
    def entry(self, m):
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@ Dados Importados @@@@@@@@@@@@@@@@@@@@@@@@@@@'       
        import json 
        with open ('choices.json', 'r+') as file:
            choices = file.read()
            choices = json.loads(choices)
            print('choices: ' , choices)
        '@@@@@@@@@@@@_____Fim Dados Importados______@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        print(m*'=')
        meses = 4
        peso=peso_inicial = 45 #choices.get('peso_medio')[0]
        self.ldias = [i+1 for i in range(meses*30)]   #Dias ate atingir 90 Kg
        print(self.ldias)
        print(85*'_')
        
        print('2','Define os pesos do Bezerro a cada dia')
        peso=peso_inicial = 45 #choices.get('peso_medio')[0]
        pesoBez1 = [ x/100 for x in range(peso*100, 6250, 58)]
        pesoBez2 = [ y/100 for y in range(6250,7600, 52)]     
        pesoBez3 = [ z/100 for z in range(7600,9400, 60)]  
        self.lPeso1to3 = pesoBez1 + pesoBez2 + pesoBez3
        print(m*'_', 1*'\n')
        
        print('3','Define % de racao por peso ')         
        #def definelracaoPer100(self):
      
        for peso in self.lPeso1to3:
                       
            if peso <= 55:
               rpc = 0
               self.lracaoPer100.append(rpc)
            elif  60>peso> 55:
               rpc = 0.5/100
               self.lracaoPer100.append(rpc)
            elif 60<=peso<100:
               rpc = 0.8/100
               self.lracaoPer100.append(rpc)
            else:
               rpc = 1.3/100
               self.lracaoPer100.append(rpc)
        print(m*'_')
                         
        print('4','Calcula a quantidade de Racao por animal / dia a cada periodo')
        #def kgRacao(self):
        self.lracao_kg = [ round((p*pr),2) for pr,p in zip(self.lPeso1to3, self.lracaoPer100)] 
        print(m*'_')

        print('5','Calcula o custo da Racao / animal / dia')
        self.lracaoCost = [  round((rkg*(self.commoditiesBez['racao'][2])),2) for rkg in self.lracao_kg ]
        print(m*'_', 1*'\n')

        print('6','Define % a quantidade de leite e leite em pos animal')         
        for peso in self.lPeso1to3:
            if peso <= 55:
               lp = 0
               l  = 4
               self.lleiteCons.append(l)
               self.lleitePoCons.append(lp)
            elif  60>peso> 55:
               lp = 1
               l  = 3
               self.lleiteCons.append(l)
               self.lleitePoCons.append(lp)
            elif 60<=peso<100:
               lp = 3
               l  = 1
               self.lleiteCons.append(l)
               self.lleitePoCons.append(lp)
            else:
               lp = 0
               l  = 0
               self.lleiteCons.append(l)
               self.lleitePoCons.append(lp)
        print(m*'_', 1*'\n')

        print('7','Calcula o custo do leite e leite em Po / animal / dia')
        self.lleiteCruCost = [  round((l*(self.commoditiesBez['leite'][2])),2) for l in self.lleiteCons ]
        self.lleitePoCost  = [  round((l*(self.commoditiesBez['leitePo'][2])),2) for l in self.lleitePoCons ]
        self.lleiteAllCost    = [  round((l*(self.commoditiesBez['leite'][2])+lpo*(self.commoditiesBez['leitePo'][2])),2) for l,lpo in zip(self.lleiteCons, self.lleitePoCons )]
        print('Custo/dia Leite cru custo')
        print('Custo/dia Leite  Po custo')
        print('Custo total/dia Leite e leite em Po ')
        print(m*'_', 1*'\n')

        print('8','Calcula o  custo Total por animal / dia')
        self.lCustoTotal = [round((cr + clall),2) for cr,clall in zip(self.lracaoCost, self.lleiteAllCost)]
        print(m*'_', '\n')
        
        print('9','Calcula o  custo Total acumulado por animal / dia')
        cac = 0
        for r in self.lCustoTotal:
            cac += r
            self.lCustoTotalAcum.append(round((cac),2)) 
        print(m*'_', '\n')
        
        print('10','Calcula o dia em que bezerro atinge 85 kg')
        dictPesosDia = dict(zip(self.lPeso1to3, self.ldias))
        for peso in dictPesosDia.keys():
            if peso >=86:
                self.dia = dictPesosDia.get(peso)
                break
        
        print(m*'_')        
        print('11','Calcula o custo do bezerro ao atingir 85 kg')
        dictCost = dict(zip(self.lPeso1to3, self.lCustoTotalAcum))
        self.CostBez = dictCost.get(peso)
        choices['peso_medio'] = [peso]
        choices['preço_medio'] = [self.CostBez]
        print(choices)
        
        '@@@@@@@@@@@@@@@@@__Save Choices___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        import json
    
        choices = json.dumps(choices,  indent=True)
        with open ("choices.json", 'w+') as file:
            file.write(choices)
        '@@@@@@@@@@@@@@@@@__Fim Save Choices___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        
        self.dictPesoCostBez['Dia Bezerro >=85']=[self.dia]
        self.dictPesoCostBez['Peso Bezerro >=85']=[peso]
        self.dictPesoCostBez['Custo Bezerro >=85']=[self.CostBez]
        
        import pandas as pd
        print(m*'_')
        print ('{:^75}'.format('Tabela de Bezerro apos 85 kg'))
        print(m*'=')
        a = self.dictPesoCostBez
        df = pd.DataFrame(a)
        #df = pd.DataFrame(a)
        blankIndex=[''] * len(df)  #Tira a aprimeira coluna
        df.index=blankIndex
        df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
        #print(df.to_markdown(index=False)) 
        print(df_tr)
        print(m*'_')
        #print('')     
    
print('_______________________FIM___________________________________')

#fim
"""

'@@@@@@@@@@@@@@@@@@@@@@@@@@@ Dados Importados @@@@@@@@@@@@@@@@@@@@@@@@@@@'       
import json 
with open ('commodities.json', 'r+') as file:
    commodities = file.read()
    commodities = json.loads(commodities)
    #print('commodities: ' , commodities)

with open ('choices.json', 'r+') as file:
    choices = file.read()
    choices = json.loads(choices)
    #print('choices: ' , choices)
'@@@@@@@@@@@@_____Fim Dados Importados______@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

x =  entradasBez()
#x.self_in(85)
x.print_commoditiesBez(45)

y = logicaBez()
y.entry(55)
#y.print_entryLists(85)
print('ai mané' , y.CostBez)
"""





