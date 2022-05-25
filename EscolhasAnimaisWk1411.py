# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:02:25 2021

@author: rogerio
"""
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#___________________________Escolhas dos Animais_________________________________________________________________________________________________

class escolhas():
     def __init__(self,
        choices={},
        print_choices     = {},
        origem_animais    = 'Animal Nascido na Fazenda',
        porte_animais     = 'Menos de 90 kg',
        peso_animais      = 40.00,
        raca_animais      = 'HPB',  
        sexo_animais      =  'Macho',  
        preco_animais     =  50.00,
        qtde_animais      =  100,  
        time_confin       = 3,
        gdp               = 1.7,
        tipo_confina      = 'grão inteiro'):
          #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        '''Inicialização Lista  dasEscolhas da
        Origem, Porte, Peso, Sexo, Raça,Quantidade'''
          
     def checkErrChoice(self, text):
        
        #global b
        while True:
          try:
               b = int(input( text))       
               if b is str:
                   raise ValueError
               elif  b >2 or b<1: 
                   raise ValueError
               break
          except ValueError:
               print('Entrada invalida digite de novo')      
        return b
       
     def checkErrChoiceRaca(self, word):
        
        #global b
        while True:
          try:
               b = int(input(word))       
               if b is str:
                   raise ValueError
               elif  b >3 or b<1: 
                   raise ValueError
               break
          except ValueError:
               print('Entrada invalida digite de novo')
               
        return b
    
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
    
     def checkErrInt(self, texto):
        
        global a
        
        while True:
          try:
               a = int(input("Digite o %s: "%(texto)))
               if a <= 0 or a is  str: 
                    raise ValueError
               break                    
          except ValueError:
               print('Entrada invalida digite de novo')
        return a
    
     def checkErrMamando(self, texto):
        
        global a
        while True:
          try:
               a = float(input("Digite o %s: "%(texto)))
               if a <= 0 or a is  str or a>=90: 
                    raise ValueError
               break                    
          except ValueError:
               print('Entrada invalida digite de novo')
        return a
    
     def checkErrDesmamado(self, texto):
        
        global a
        while True:
          try:
               a = float(input("Digite o %s: "%(texto)))
               if a <= 0 or a is  str or a<90: 
                    raise ValueError
               break                    
          except ValueError:
               print('Entrada invalida digite de novo')
        return a
     
     def entrada_dados(self, m):
        
        self.choices = {}
        self.print_choices = {}
         
        global text
        
         #___________________Origem dos Animais¨do Lote____________________
        print(33*('\n'))
        print (m*'_')
        print('''
         Escolha a Origem dos Animais
         [ 1 ] Animal Nascido na Fazenda
         [ 2 ] Animal Adquirido
         ''')
        self.origem_animais = escolhas().checkErrChoice('Escolha se o animal e proprio ou e adquirido: ')
        if self.origem_animais == 1:
             self.choices['origem'] = ['Fazenda']
                 
        if self.origem_animais == 2:
             self.choices['origem'] = ['Adquirido']
             print(self.choices)
        #print(1*('\n'))
        print (m*'=')
        print(' Origem dos Animais ==>', self.choices.get('origem'))
        print (m*'=')
        print(1*('\n'))
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #___________________Porte dos Animais do Lote______________________
        #print(23*('\n'))
        print (m*'_')  
        print('''Escolha o Porte Médio dos Animais
              [1]  Igual ou Menor que 85 kg
              [2]  Mais de 85 kg
              ''')
        self.origem_animais = escolhas().checkErrChoice('Escolha o  porte medio dos animais:  ')
        if self.origem_animais == 1:
             self.choices['porte'] = [ 'Igual ou Menor que 85 kg']

        if self.origem_animais == 2:
             self.choices['porte'] = [ 'Mais 85 kg']
        #print(1*('\n'))
        print (m*'=')
        print(' Porte dos Animais ==>', self.choices.get('porte'))
        print (m*'=')
        print(1*('\n'))
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #____________________Peso Medio dos Animais do Lote¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #print(23*('\n'))
        print (m*'_')
        if self.origem_animais == 1:
            self.peso_animais = escolhas().checkErrMamando('Digite peso medio dos animais no lote: ')     
            self.choices['peso_medio'] = [ self.peso_animais]
        else:
            self.peso_animais = escolhas().checkErrDesmamado('Digite peso medio dos animais no lote: ')     
            self.choices['peso_medio'] = [ self.peso_animais]
        #print(8*('\n'))
        print (m*'=')
        print(' Peso Medio dos Animais ==>', self.choices.get('peso_medio'))
        print (m*'=')
        print(1*('\n'))
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #____________________Preço Medio dos Animais do Lote¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        print (m*'_')
        self.preco_animais   =  escolhas().checkErrFloat( 'Digite preço medio dos animais no lote: ')     
        self.choices['preço_medio'] = [ self.preco_animais]
        #print(1*('\n'))
        print (m*'=')
        print(' Preço Medio dos Animais ==>', self.choices.get('preço_medio'))
        print (m*'=')
        print(1*('\n'))
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #___________________Sexo dos  Animais do Lote_____________________
        print('''
        Informe o Sexo dos Animais no Lote
        [ 1 ] Macho
        [ 2 ] Femea
        ''')
        self.origem_animais = escolhas().checkErrChoice('Informe o sexo dos animais no lote:')
        if self.origem_animais == 1:
             self.choices['sexo'] = [ 'Macho']
        if self.origem_animais == 2:
             self.choices['sexo'] = [ 'Femea']
        #print(7*('\n'))
        print (m*'=')
        print(' Sexo dos Animais ==>', self.choices.get('sexo'))
        print (m*'=')
        print(1*('\n'))
        print (m*'_')  
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #___________________Raça dos  Animais do Lote_____________________
        print('''
        Informe a Raça dos Animais no Lote
        [ 1 ] Nelore e similares tropicais
        [ 2 ] HPB similares europeias
        [ 3 ] Cruzado
        ''')
        self.origem_animais = escolhas().checkErrChoiceRaca('Informe a raça dos animais no lote:')
        if self.origem_animais == 1:
             self.choices['raça'] = ["Nelore"]
        elif self.origem_animais == 2:
             self.choices['raça'] = [ "HPB"]
        elif self.origem_animais == 3:
             self.choices['raça'] = ["Cruzado"]
        #print(7*('\n'))
        print (m*'=')
        print(' Raça dos Animais ==>', self.choices.get('raça'))
        print (m*'=')
        print(1*('\n'))
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #____________________Quantidade de Animais do Lote_________________
        self.qtde_animais   = escolhas().checkErrInt( 'Informe a Quantidade de Animais do Lote: ')
        self.choices['quantidade'] = [ self.qtde_animais]
        #print(1*('\n'))
        print (m*'=')
        print('Quantidade de Animais ==>', self.choices.get('quantidade'))
        print (m*'=')
        print(1*('\n'))
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #____________________GDP - Ganho de Peso Diário______________________
        self.GDP   = escolhas().checkErrFloat( 'Informe o Ganho de Peso Diário ')     
        self.choices['GDP'] = [ self.GDP]
        #print(1*('\n'))
        print (m*'=')
        print('GDP  ==>', self.choices.get('GDP'))
        print (m*'=')
        print(2*('\n'))
        #print(self.choices)
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        #____________________Tempo de Confinamento em Meses______________________
        self.time_confin   =  escolhas().checkErrInt( 'Informe o Tempo de Confinamento em Meses ')
        self.choices['time'] = [ self.time_confin]
        #print(1*('\n'))
        print (m*'=')
        print('Meses de Confinamento  ==>', self.choices.get('time'))
        print (m*'=')
        print(1*('\n'))
        print('======================Testa Bezerro Mamando ou Desmamado==============')
        #¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        
        ('Calcula o preco medio do bezerro apos atingir 85 kg')
        print(self.choices) #imprime diretorio de escolhas
        
        #choices = self.choices
       
     def print_escolhas(self, m):
         
        import pandas as pd
        print(m*'_')
        print ('{:^75}'.format('Inicio Tabela de Escolhas'))
        print(m*'=')
        a = self.choices
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
        #
      

"""
c = escolhas()
c.entrada_dados(85)
choices=c.choices
'@@@@@@@@@@@@@@@@@__Save Choices___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
import json
choices = c.choices
print(choices)
choices = json.dumps(choices,  indent=True)
with open ("choices.json", 'w+') as file:
    file.write(choices)
'@@@@@@@@@@@@@@@@@__Fim Save Choices___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
"""
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

"""
c.print_escolhas(85)
"""

