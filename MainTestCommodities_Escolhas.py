,
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:56:38 2021

@author: Windows 11
"""
import sys
sys.path.append('C:/Users/rogerio/OneDrive/Rogerio/rogerPythonTkinterApps/rogerEngordaBezerrosPyhon/Working/fullWorking')

def print_escolhas(choices, m):
         
    import pandas as pd
    print(m*'_')
    print ('{:^75}'.format('Inicio Tabela de Escolhas'))
    print(m*'=')
    a = choices
    df = pd.DataFrame(a)
    #df = pd.DataFrame(a)
    blankIndex=[''] * len(df)  #Tira a aprimeira coluna
    df.index=blankIndex
    df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
    #print(df.to_markdown(index=False)) 
    print(df_tr)
    print(m*'_')
    #print('')          
    #____________________Print Dados Todos__________________________
    
def print_commodities(commodities,m):
                              
    import pandas as pd   
    print (26*'\n')
    print(m*'_')
    print ('{:^75}'.format('Tabela de Commodities'))
    print(m*'=')
    comm = {}
    comm['Commodities']= ['Preço R$', 'Peso/Unidade','Peso/Kg']
    l1 = list(commodities.keys())
    l2 = list(commodities.values())
    for i in  range(len(l1)):
        comm[l1[i]]=l2[i]
    df = pd.DataFrame(comm)
    blankIndex=[''] * len(df)  #Tira a aprimeira coluna
    df.index=blankIndex
    #print(df)
    df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
    #print(df.to_markdown(index=False)) 
    print(df_tr)
    print(m*'_')

def checkErrChoice(text):
        
    global resp
    while True:
      try:
           resp = int(input( text ))       
           if resp is str:
               raise ValueError
           elif  resp > 2 or resp < 1: 
               raise ValueError
           break
      except ValueError:
           print('Entrada invalida digite de novo: ')      
    return resp

'@@@@@@@@@@@@@@@@@@@@@@@@@@@ Dados Importados @@@@@@@@@@@@@@@@@@@@@@@@@@@'       
import json 
with open ('commodities.json', 'r+') as file:
    commodities = file.read()
    commodities = json.loads(commodities)
    print('commodities: ' , commodities, '\n')

with open ('choices.json', 'r+') as file:
    choices = file.read()
    choices = json.loads(choices)
    print('choices: ' , choices)
'@@@@@@@@@@@@_____Fim Dados Importados______@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
#stop = input('stop')
print('\n', '====> class commodities============================')
print('\n', '====> Testa se commodities esta atualizada_____________')
print_commodities(commodities, 85)

entry = (input('Deseja atualizar digite s. Do contrário,  digite qualque tecla: '))
if entry == 's' or entry == 'S' :
    #print(entry)
    from CommoditiesAllWk1411 import *
    #global commodities
    #global meses
    
    x = entradas()
    x.self_in(85)
    x.print_commodities(85)

    '@@@@@@@@@@@@@@@@@__Save Commodities___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    commodities = x.commodities
    import json
    #commodities = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
    commodities = json.dumps(commodities,  indent=True)
    with open ("commodities.json", 'w+') as file:
        file.write(commodities)
    '@@@@@@@@@@@@@@@@@__Fim Save Commodities___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print('commodities', commodities)
    print('\n', '====> Fim Commodities-------------------------')
else:
    print('commodities====>', commodities)
print('\n', '====> Fim Commodities__________________________')

print('\n', '====> class EscolhasAnimais===========================')

print('testa se lista de escolhas de animais abaixo esta atualizada')
print_escolhas(choices, 85)

entry = (input('Deseja atualizar digite s. Do contrário,  digite qualque tecla: '))
if entry == 's' or entry == 'S' :
    #print(entry)
    from EscolhasAnimaisWk1411 import *
    #global commodities
    #global meses
    c = escolhas()
    c.entrada_dados(85)
    "+++++++++++++++++"
    choices=c.choices
    "+++++++++++++++++"
    c.print_escolhas(85)
    #choices = c.choices
    print("choices====>", choices,2*'\n')
    '@@@@@@@@@@@@@@@@@__Save Choices___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    import json
    #choices = c.choices
    #print(choices)
    choices = json.dumps(choices,  indent=True)
    with open ("choices.json", 'w+') as file:
        file.write(choices)
    '@@@@@@@@@@@@@@@@@__Fim Save Choices___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print('------------------------------Fim Choices  ----------------------')


print('\n', '====> Fim EscolhasAnimais---------------------')
