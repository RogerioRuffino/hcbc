# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:57:28 2021

@author: rogerio
"""
class entradas():
    
    def __init__(self,
                  commodities = { },  
                  milho = 30.00, milho_kg = 60,
                  nucleo = 50.00, nucleo_kg = 40,
                  silo = 250.00, silo_kg = 1,
                  racao = 64.00, racao_kg = 40,
                  bicarb = 30.00, bicarb_kg = 25,
                  sal = 30.00, sal_kg = 30):

        self.commodities = {}
        self.milho = milho
        self.nucleo = nucleo
        self.silo = silo
        self.racao = racao
        self.bicarb = bicarb
        self.sal = sal 

        self.milho_kg = milho_kg
        self.nucleo_kg = nucleo_kg
        self.silo_kg = silo_kg
        self.racao_kg = racao_kg
        self.bicarb_kg = bicarb_kg
        self.sal_kg =  sal_kg
    
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
        global commodities
        global texto
        global word
        print (5*('\n'))
        #self.commodities['Descrição|'] = ['Preço em R$', 'Peso da Saca', 'Preço por Kg']
        print (m*'_')   #Entrada dados milho
        self.milho = entradas().checkErrFloat('preço saca de Milho')
        self.milho_kg = entradas().checkErrFloat('peso saca de Milho')
        self.commodities['milho'] = [self.milho, self.milho_kg, round((self.milho/self.milho_kg),2)]
        
        print (m*'_')   #Entrada dados nucleo
        self.nucleo = entradas().checkErrFloat('preço saca de nucleo')
        self.nucleo_kg = entradas().checkErrFloat('peso saca de nucleo')
        self.commodities['nucleo'] = [self.nucleo, self.nucleo_kg, round((self.nucleo/self.nucleo_kg),2)]
        
        print (m*'_')   #Entrada dados silo
        self.silo = entradas().checkErrFloat('preço tonelada de silagem')
        self.silo_kg = 1000
        self.commodities['silo'] = [self.silo, self.silo_kg, round((self.silo/self.silo_kg),2)]
        
        print (m*'_')   #Entrada dados ração
        self.ração = entradas().checkErrFloat('preço saca de ração')
        self.ração_kg = entradas().checkErrFloat('peso saca de ração')
        self.commodities['ração'] = [self.ração, self.ração_kg, self.ração/self.ração_kg]
        
        print (m*'_')   #Entrada dados bicarbonato
        self.bicarbonato = entradas().checkErrFloat('preço saca de bicarbonato')
        self.bicarbonato_kg = entradas().checkErrFloat('peso saca de bicarbonato')
        self.commodities['bicarbonato'] = [self.bicarbonato, self.bicarbonato_kg, self.bicarbonato/self.bicarbonato_kg]

        print (m*'_')   #Entrada dados sal_mineral
        self.sal_mineral = entradas().checkErrFloat('preço saca de sal_mineral')
        self.sal_mineral_kg = entradas().checkErrFloat('peso saca de sal_mineral')
        self.commodities['sal_mineral'] = [self.sal_mineral, self.sal_mineral_kg, self.sal_mineral/self.sal_mineral_kg]
        
        print (m*'_')   #Entrada dados arroba_boi_compra
        self.arroba_boi_compra = entradas().checkErrFloat('da arroba do boi compra')
        self.arroba_boi_venda = entradas().checkErrFloat('da arroba do boi venda')
        self.commodities['arroba_boi'] = [self.arroba_boi_compra, self.arroba_boi_venda, 0]
        
        #print('dir commodities é',  self.commodities)
        print(m*'_')
     
    def print_commodities(self, m):
                                  
        import pandas as pd   
        #from tabulate import tabulate        
        print (26*'\n')
        print(m*'_')
        print ('{:^75}'.format('Tabela de Commodities'))
        print(m*'=')
        df = pd.DataFrame(self.commodities)
               
        blankIndex=[''] * len(df)  #Tira a aprimeira coluna
        df.index=blankIndex
        #print(df)
        
        df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
        #print(df.to_markdown(index=False)) 
        print(df_tr)

        print(m*'_')

"""
x = entradas()
x.self_in(85)

x.print_commodities(85)
commodities=x.commodities
"""
