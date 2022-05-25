# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:17:04 2021

@author: Windows 11
"""
import sys
sys.path.append('C:/Users/rogerio/OneDrive/Rogerio/rogerPythonTkinterApps/rogerEngordaBezerrosPyhon/Working/fullWorking')

print(2*'\n')
print('====> Primeira Pesagem===============================')

from geraPesagem import *
'@@@@@@@@@@@@@@@@@@@@@@@@@@@ Dados Importados @@@@@@@@@@@@@@@@@@@@@@@@@@@'       
import json 
with open ('choices.json', 'r+') as file:
    choices = file.read()
    choices = json.loads(choices)
    #print('choices: ' , choices)
with open ('dictAll.json', 'r+') as file:
    dictAll = file.read()
    dictAll = json.loads(dictAll)
    #print('choices: ' , choices)
'@@@@@@@@@@@@_____Fim Dados Importados______@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

dictPeso = dictAll['Peso']
#print('dictPeso', dictPeso, 2*'\n')
a = geraPesagem(choices, dictPeso)
a.dataInConfinamento()
a.dataPesagem()
a.pesagem()



"""
a = logicaDT(step,
                D,
                commodities,
                choices,
                dictPeso,
                dictNucleo,
                dictMilhokg,
                dictNucleokg,
                dictMilhoCost,
                dictNucleoCost,
                dictCustoDia,
                dictCustoAcum,
                dictAll,
                dictAllStep,
                profitAll)

a.time()
#a.peso_animais()

a.defineNucleo()
a.kgMilho()
a.kgNucleo()
a.custoMilho()
a.custoNucleo()
a.custo_Dia()
a.custo_acumulado_total()
 
a. trato_animais()
a.print_trato_animais(75)
a.print_resultados(75)
a.analise_lucratividade(75)
a.print_lucratividade(75)
answer = input('''
    Digite 1 se deseja fazer outra analise de lucratividade em outra data? 
        [ 1 ] Sim
        [ 2 ] Não
       ''')
if answer == "1":
    a.analise_lucratividade(75)
    a.print_lucratividade(75)
"""
"++++++++++++++++++++++++++++Fim Primeira Rodada+++++++++++++++++++"




"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
"""
resp = input(' Digite s pesagem vez ou qq tecla  se  é primeira vez: ')
if resp == 's': 
    print('aki')
    commodities = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
    choices = {'origem': ['Adquirido'], 'porte': ['Mais 85 kg'], 'peso_medio': [100.0], 'preço_medio': [2.0], 'sexo': ['Femea'], 'raça': ['HPB'], 'quantidade': [2], 'GDP': [2.0], 'time': [2]}
    
    dictPeso = {1: 102.0, 2: 104.0, 3: 106.0, 4: 108.0, 5: 110.0, 6: 112.0, 7: 114.0, 8: 116.0, 9: 118.0, 10: 120.0, 11: 122.0, 12: 124.0, 13: 126.0, 14: 128.0, 15: 130.0, 16: 132.0, 17: 134.0, 18: 136.0, 19: 138.0, 20: 140.0, 21: 142.0, 22: 144.0, 23: 146.0, 24: 148.0, 25: 150.0, 26: 152.0, 27: 154.0, 28: 156.0, 29: 158.0, 30: 160.0, 31: 162.0, 32: 164.0, 33: 166.0, 34: 168.0, 35: 170.0, 36: 172.0, 37: 174.0, 38: 176.0, 39: 178.0, 40: 180.0, 41: 182.0, 42: 184.0, 43: 186.0, 44: 188.0, 45: 190.0, 46: 192.0, 47: 194.0, 48: 196.0, 49: 198.0, 50: 200.0, 51: 202.0, 52: 204.0, 53: 206.0, 54: 208.0, 55: 210.0, 56: 212.0, 57: 214.0, 58: 216.0, 59: 218.0, 60: 220.0}
    dict_time = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 28, 29: 29, 30: 30, 31: 31, 32: 32, 33: 33, 34: 34, 35: 35, 36: 36, 37: 37, 38: 38, 39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45, 46: 46, 47: 47, 48: 48, 49: 49, 50: 50, 51: 51, 52: 52, 53: 53, 54: 54, 55: 55, 56: 56, 57: 57, 58: 58, 59: 59, 60: 60}
    dictNucleo = {1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25, 5: 0.25, 6: 0.25, 7: 0.25, 8: 0.25, 9: 0.25, 10: 0.25, 11: 0.2, 12: 0.2, 13: 0.2, 14: 0.2, 15: 0.2, 16: 0.2, 17: 0.2, 18: 0.2, 19: 0.2, 20: 0.2, 21: 0.2, 22: 0.2, 23: 0.2, 24: 0.2, 25: 0.2, 26: 0.2, 27: 0.2, 28: 0.2, 29: 0.2, 30: 0.2, 31: 0.2, 32: 0.2, 33: 0.2, 34: 0.2, 35: 0.2, 36: 0.2, 37: 0.2, 38: 0.2, 39: 0.2, 40: 0.2, 41: 0.2, 42: 0.2, 43: 0.2, 44: 0.2, 45: 0.2, 46: 0.2, 47: 0.2, 48: 0.2, 49: 0.2, 50: 0.2, 51: 0.2, 52: 0.2, 53: 0.2, 54: 0.2, 55: 0.2, 56: 0.2, 57: 0.2, 58: 0.2, 59: 0.2, 60: 0.2}
    dictMilhokg = {1: 0.66, 2: 1.01, 3: 2.07, 4: 2.11, 5: 2.15, 6: 2.18, 7: 2.22, 8: 2.26, 9: 2.3, 10: 2.34, 11: 2.54, 12: 2.58, 13: 2.62, 14: 2.66, 15: 2.7, 16: 2.75, 17: 2.79, 18: 2.83, 19: 2.87, 20: 2.91, 21: 2.95, 22: 3.0, 23: 3.04, 24: 3.08, 25: 3.12, 26: 3.16, 27: 3.2, 28: 3.24, 29: 3.29, 30: 3.33, 31: 3.37, 32: 3.41, 33: 3.45, 34: 3.49, 35: 3.54, 36: 3.58, 37: 3.62, 38: 3.66, 39: 3.7, 40: 3.74, 41: 3.79, 42: 3.83, 43: 3.87, 44: 3.91, 45: 3.95, 46: 3.99, 47: 4.04, 48: 4.08, 49: 4.12, 50: 4.16, 51: 4.2, 52: 4.24, 53: 4.28, 54: 4.33, 55: 4.37, 56: 4.41, 57: 4.45, 58: 4.49, 59: 4.53, 60: 4.58}
    dictNucleokg = {1: 0.22, 2: 0.34, 3: 0.69, 4: 0.7, 5: 0.71, 6: 0.73, 7: 0.74, 8: 0.75, 9: 0.77, 10: 0.78, 11: 0.63, 12: 0.64, 13: 0.66, 14: 0.67, 15: 0.68, 16: 0.69, 17: 0.7, 18: 0.71, 19: 0.72, 20: 0.73, 21: 0.74, 22: 0.75, 23: 0.76, 24: 0.77, 25: 0.78, 26: 0.79, 27: 0.8, 28: 0.81, 29: 0.82, 30: 0.83, 31: 0.84, 32: 0.85, 33: 0.86, 34: 0.87, 35: 0.88, 36: 0.89, 37: 0.9, 38: 0.92, 39: 0.93, 40: 0.94, 41: 0.95, 42: 0.96, 43: 0.97, 44: 0.98, 45: 0.99, 46: 1.0, 47: 1.01, 48: 1.02, 49: 1.03, 50: 1.04, 51: 1.05, 52: 1.06, 53: 1.07, 54: 1.08, 55: 1.09, 56: 1.1, 57: 1.11, 58: 1.12, 59: 1.13, 60: 1.14}
    dictMilhoCost = {1: 0.66, 2: 1.01, 3: 2.07, 4: 2.11, 5: 2.15, 6: 2.18, 7: 2.22, 8: 2.26, 9: 2.3, 10: 2.34, 11: 2.54, 12: 2.58, 13: 2.62, 14: 2.66, 15: 2.7, 16: 2.75, 17: 2.79, 18: 2.83, 19: 2.87, 20: 2.91, 21: 2.95, 22: 3.0, 23: 3.04, 24: 3.08, 25: 3.12, 26: 3.16, 27: 3.2, 28: 3.24, 29: 3.29, 30: 3.33, 31: 3.37, 32: 3.41, 33: 3.45, 34: 3.49, 35: 3.54, 36: 3.58, 37: 3.62, 38: 3.66, 39: 3.7, 40: 3.74, 41: 3.79, 42: 3.83, 43: 3.87, 44: 3.91, 45: 3.95, 46: 3.99, 47: 4.04, 48: 4.08, 49: 4.12, 50: 4.16, 51: 4.2, 52: 4.24, 53: 4.28, 54: 4.33, 55: 4.37, 56: 4.41, 57: 4.45, 58: 4.49, 59: 4.53, 60: 4.58}
    dictNucleoCost = {1: 0.22, 2: 0.34, 3: 0.69, 4: 0.7, 5: 0.71, 6: 0.73, 7: 0.74, 8: 0.75, 9: 0.77, 10: 0.78, 11: 0.63, 12: 0.64, 13: 0.66, 14: 0.67, 15: 0.68, 16: 0.69, 17: 0.7, 18: 0.71, 19: 0.72, 20: 0.73, 21: 0.74, 22: 0.75, 23: 0.76, 24: 0.77, 25: 0.78, 26: 0.79, 27: 0.8, 28: 0.81, 29: 0.82, 30: 0.83, 31: 0.84, 32: 0.85, 33: 0.86, 34: 0.87, 35: 0.88, 36: 0.89, 37: 0.9, 38: 0.92, 39: 0.93, 40: 0.94, 41: 0.95, 42: 0.96, 43: 0.97, 44: 0.98, 45: 0.99, 46: 1.0, 47: 1.01, 48: 1.02, 49: 1.03, 50: 1.04, 51: 1.05, 52: 1.06, 53: 1.07, 54: 1.08, 55: 1.09, 56: 1.1, 57: 1.11, 58: 1.12, 59: 1.13, 60: 1.14}
    dictCustoDia = {1: 0.88, 2: 1.35, 3: 2.76, 4: 2.81, 5: 2.86, 6: 2.91, 7: 2.96, 8: 3.01, 9: 3.07, 10: 3.12, 11: 3.17, 12: 3.22, 13: 3.28, 14: 3.33, 15: 3.38, 16: 3.44, 17: 3.49, 18: 3.54, 19: 3.59, 20: 3.64, 21: 3.69, 22: 3.75, 23: 3.8, 24: 3.85, 25: 3.9, 26: 3.95, 27: 4.0, 28: 4.05, 29: 4.11, 30: 4.16, 31: 4.21, 32: 4.26, 33: 4.31, 34: 4.36, 35: 4.42, 36: 4.47, 37: 4.52, 38: 4.58, 39: 4.63, 40: 4.68, 41: 4.74, 42: 4.79, 43: 4.84, 44: 4.89, 45: 4.94, 46: 4.99, 47: 5.05, 48: 5.1, 49: 5.15, 50: 5.2, 51: 5.25, 52: 5.3, 53: 5.35, 54: 5.41, 55: 5.46, 56: 5.51, 57: 5.56, 58: 5.61, 59: 5.66, 60: 5.72}
    dictCustoAcum = {1: 0.88, 2: 2.23, 3: 4.99, 4: 7.8, 5: 10.66, 6: 13.57, 7: 16.53, 8: 19.54, 9: 22.61, 10: 25.73, 11: 28.9, 12: 32.12, 13: 35.4, 14: 38.73, 15: 42.11, 16: 45.55, 17: 49.04, 18: 52.58, 19: 56.17, 20: 59.81, 21: 63.5, 22: 67.25, 23: 71.05, 24: 74.9, 25: 78.8, 26: 82.75, 27: 86.75, 28: 90.8, 29: 94.91, 30: 99.07, 31: 103.28, 32: 107.54, 33: 111.85, 34: 116.21, 35: 120.63, 36: 125.1, 37: 129.62, 38: 134.2, 39: 138.83, 40: 143.51, 41: 148.25, 42: 153.04, 43: 157.88, 44: 162.77, 45: 167.71, 46: 172.7, 47: 177.75, 48: 182.85, 49: 188.0, 50: 193.2, 51: 198.45, 52: 203.75, 53: 209.1, 54: 214.51, 55: 219.97, 56: 225.48, 57: 231.04, 58: 236.65, 59: 242.31, 60: 248.03}
    dictAll = {} 
    dictAllStep = {}
    
    lMilhokg = list(dictMilhokg.values())
    lNucleokg = list(dictNucleokg.values())
    lMilhoCost = list(dictMilhoCost.values())
    lNucleoCost = list(dictNucleoCost.values())
    lCustoDia   = list(dictCustoDia.values())
    lCustoAcum  = list(dictCustoAcum.values())
    step =10
    D=0
    #stop = input('stop')
    a = logicaDT(step,
                 D,
                 commodities,
                 choices,
                 dictPeso,
                 dictNucleo,
                 dictMilhokg,
                 dictNucleokg,
                 dictMilhoCost,
                 dictNucleoCost,
                 dictCustoDia,
                 dictCustoAcum,
                 dictAll ,
                 dictAllStep )
    a.dataInConfinamento(85)
    a.dataPesagem(85)
    a.pesagem(85)

else:
  
    commodities = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
    choices = {'origem': ['Adquirido'], 'porte': ['Mais 85 kg'], 'peso_medio': [100.0], 'preço_medio': [2.0], 'sexo': ['Femea'], 'raça': ['HPB'], 'quantidade': [2], 'GDP': [2.0], 'time': [2]}
    
    dictPeso = {}
    dict_time = {}
    dictNucleo = {}
    dictMilhokg = {}
    dictNucleokg = {}
    dictMilhoCost = {}
    dictNucleoCost = {}
    dictCustoDia = {}
    dictCustoAcum = {}
    dictAll = {} 
    dictAllStep = {}
    
    lMilhokg = []
    lNucleokg = []
    lMilhoCost = []
    lNucleoCost = []
    lCustoDia = []
    lCustoAcum = []
    step =10
    D=0
        
    print(dictCustoAcum)
    a = logicaDT(
                 10,
                 0,
                 commodities,
                 choices,
                 dictPeso,
                 dictNucleo,
                 dictMilhokg,
                 dictNucleokg,
                 dictMilhoCost,
                 dictNucleoCost,
                 dictCustoDia,
                 dictCustoAcum,
                 dictAll ,
                 dictAllStep )


resp = input(' Digite p se é a  primeira vez ou 0 se  é Pesagem: ')
if resp== "p":
          
    a.dataInConfinamento(85)
    while True:
        try:        
            a.dataPesagem(85)
            if a.D < 0:
               raise ValueError
            else: 
                break
        except ValueError:
            print('Erro: Data de incicio confinamento sao as mesmas. Digite outra data')
    if a.D != 0:
        print('ai manezao', a.D )    
    a.pesagem(85)

a.time()
a.peso_animais()
'''a.defineNucleo() 
a.kgMilho()
a.kgNucleo()
a.custoMilho()
a.custoNucleo()
a.custo_Dia()
a.custo_acumulado_total()
a.analise_lucratividade(85)
a.print_resultados(75)
a.print_lucratividade(75)
'''


#commodities = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
#choices = {'origem': ['Adquirido'], 'porte': ['Mais 85 kg'], 'peso_medio': [222.0], 'preço_medio': [2.0], 'sexo': ['Femea'], 'raça': ['HPB'], 'quantidade': [2], 'GDP': [2.0], 'time': [1]}

#a = logicaDT(commodities, choices, 1,30, 3)
#a.pesagem(85)
"""