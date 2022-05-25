# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:59:16 2021

@author: Windows 11
"""
import sys
sys.path.append('C:/Users/rogerio/OneDrive/Rogerio/rogerPythonTkinterApps/rogerEngordaBezerrosPyhon/Working/fullWorking')

'@@@@@@@@@@@@@@@@@@@@@@@@@@@ Dados Importados @@@@@@@@@@@@@@@@@@@@@@@@@@@'       
import json 
with open ('commodities.json', 'r+') as file:
    commodities = file.read()
    commodities = json.loads(commodities)
    print('commodities: ' , commodities)

with open ('choices.json', 'r+') as file:
    choices = file.read()
    choices = json.loads(choices)
    print('choices: ' , choices)
'@@@@@@@@@@@@_____Fim Dados Importados______@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

from logicaPesagem import *

a = logicaDT(10,0, commodities, choices)
a.time()
a.peso_animais()

a.defineNucleo()
a.kgMilho()
a.kgNucleo()
a.custoMilho()
a.custoNucleo()
a.custo_Dia()
#stop= input('stop')
a.custo_acumulado_total()
#stop= input('stop')
 
a. trato_animais()
a.print_trato_animais(60)
a.print_resultados(60)
a.analise_lucratividade(60)
a.print_lucratividade(60)
#print('dictAllStep',  a.dictAll )

print()
print('\n', '====> Fim primeira vez_______________________________')

