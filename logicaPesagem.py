"""
Created on Fri Nov 19 11:24:49 2021

@author: rogerio
"""
class logicaDT ():
    
    'commodities, choices, dictPeso,  D, step, dictAll,dictAllStep lDias, lPeso)'
    def __init__(self, 
                 
                 step,
                 D,
                 commodities={},
                 choices={},
                 dictPeso={},
                 dictNucleo={},
                 dictMilhokg={},
                 dictNucleokg={},
                 dictMilhoCost={},
                 dictNucleoCost={},
                 dictCustoDia={},
                 dictCustoAcum={},
                 dictAll={},
                 dictAllStep={},
                 profitAll= {}):
                 '''
                 
                 lMilhokg,
                 lNucleokg,
                 lMilhoCost,
                 lNucleoCost,
                 lCustoDia,
                 lCustoAcum
                 ):
                 '''
                 self.step            = step
                 self.commodities     = commodities       
                 self.choices         = choices
                 self.dictPeso        = dictPeso
                 self.dictNucleo      = dictNucleo
                 self.dictMilhokg     = dictMilhokg 
                 self.dictNucleokg    = dictNucleokg
                 self.dictMilhoCost   = dictMilhoCost
                 self.dictNucleoCost  = dictNucleoCost
                 self.dictCustoDia    = dictCustoDia 
                 self.dictCustoAcum   = dictCustoAcum                
                 self.dictAll         = dictAll
                 self.dictAllStep     = dictAllStep
                 self.profitAll       = profitAll
                 self.D               = D
                 '''
                 
                 self.lMilhokg        = lMilhokg
                 self.lNucleokg       = lNucleokg
                 self.lMilhoCost      = lMilhoCost
                 self.lNucleoCost     = lNucleoCost
                 self.lCustoDia       = lCustoDia
                 self.lCustoAcum      = lCustoAcum
                 '''
    ('===================Fim Init===============================')            
                 
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

    
        #Fun2 Cria lista soma de n elementos de uma lista de xn elements
    def makeList(self, lst, step):
        
        from numpy import median
        lbck = lambda lst,step : [round((median(lst[i:i+step])),2) for i in range(0, len(lst), step)]
        return lbck(lst, step)
    
    def makeListPesagem(self, lOld, lNew, D):
        
        from numpy import median
        lm = lambda lOld,lNew, D: lOld[0:D]+lNew[D:]
        return (lm(lOld, lNew, D))
    
    def transport (self):
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@ Dados Importados @@@@@@@@@@@@@@@@@@@@@@@@@@@'       
        import json 
        with open ('commodities.json', 'r+') as file:
            commodities = file.read()
            commodities = json.loads(commodities)
            print('commodities: ' , commodities)

        with open ('choices.json', 'r+') as file:
            choices = file.read()
            choices = json.loads(choices)
            self.choices = choices
            print('choices: ' , choices)
        '@@@@@@@@@@@@_____Fim Dados Importados______@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        
        #print("commodities imported transp", self.commodities) #precos commodities para todos animais
        print("choices imported trans", self.choices)
        print("a i manezao ====>", self.choices.get('time')[0])
        
        "==================Início funções lucratividade======================="    
        
    def time(self):
                
        print('1','Cria Lista de dias de confinamento')
        #meses=[]
        meses = self.choices.get('time')[0]
        self.lDias = [ dia+1 for dia in range(meses*30)]
        self.lStep = [p for p in range(self.step,meses*30+self.step,self.step)]
        self.lNroStep = [nro for nro in range(1,(len(self.lStep)+1))]
        self.dictStep = dict(zip(self.lNroStep, self.lStep))
    
        '___________________Cria dictAll__________'
        self.dictAll['Dias'] = self.lDias
        self.dictAllStep['Periodos'] = self.lStep
        print('========================= fim time==========================\n')
   
        print('2','Cria lista de pesos medios dos animais para cada dia de confin')
    def peso_animais(self):
        
        GDP = self.choices.get('GDP')[0]
        if  self.D != 0:    
            #lPesoStepOld=[]
            dictPesoOld =dictPeso #inserir self.
            lPesoOld = list(dictPesoOld.values())
        else:
            lPesoOld=[]
            
        lPesonew = lPesoStepnew = []
        
        peso=pesoInicial = self.choices.get('peso_medio')[0]
        if self.D ==0:
            self.GDPnew = GDP = self.choices.get('GDP')[0]
        
        "Cria novas listas de pesos durante toda pesagem "
        for i in self.lDias:   
            peso = peso + self.GDPnew
            lPesonew.append(round((peso),2))
        
        if  self.D != 0: 
            #print('Cria nova lista de Pesos apos pesagem')
            ('________________________________________________________')
            self.lPeso = lPesoOld[:self.D] + lPesonew[self.D:]
            ('________________________________________________________')
        else:
            self.lPeso = lPesonew
        print('self.lPeso', self.lPeso, 2*'\n')
        self.dictPeso = dict(zip(self.lDias, self.lPeso))
        #print ('self.dictPeso = ',self.dictPeso, (2*'\n'))
        
        '___________________Cria PesoStep__________'
        #print('PesoStepOld = ', lPesoStepOld,2*'\n')
        self.lPesoStep =  self.makeList(self.lPeso,self.step)
        print('self.PesoStep = ', self.lPesoStep, (2*'\n'))
        
        
        '___________________Cria dictAll__________'
        self.dictAll['Peso'] = self.dictPeso
        #print('\n')
        self.dictAllStep['Peso Step'] = self.lPesoStep
        print('=================== fim peso_animais======================\n')
        
        print('3','Define a porcentagem de proteinas no Nucleo a cada 10 dias')         
    def defineNucleo(self):
        
        step=self.step
        lN = lNnew = []
        if  self.D != 0:
            dictPesoOld =dictPeso #inserir self.
            dictNucleoOld=self.dictNucleo
        else:
            lNucleoOld=[]
        
        #for peso in list(self.dictPeso.values()):
        for peso in self.lPeso:
            if peso>= 250:
               nucleo = 0.15
               lNnew.append(nucleo)
            elif 120<peso<250:
               nucleo = 0.20
               lNnew.append(nucleo)
            else:
               nucleo = 0.25
               lNnew.append(nucleo)
        #print("lNnew======", lNnew, (2*'\n'))
        
        if  self.D != 0:
            #print('Cria nova lista de proteina nucleo')
            ('________________________________________________________')
            self.lNucleo = lNucleoOld[:self.D]+lNnew[self.D:]        
            ('________________________________________________________')
        else: 
            self.lNucleo = lNnew            
        ('_____Converte 2 listas nroperiodos e nucleo em dict____')
        self.dictNucleo = dict(zip(self.lDias, self.lNucleo))
        
        #print('___________________Cria NucleoStep__________')
        self.lNucleoStep = self.makeList(self.lNucleo, self.step)
        #print('self.lNucleoStep ==', self.lNucleoStep, 2*'\n' )
        '___________________Cria dictAll__________'
        self.dictAll['Proteina Nucleo'] = self.lNucleo
        self.dictAllStep['Proteina Nucleo'] = self.lNucleoStep
        #print(self.dictAll,'\n',self.dictAllStep)
        print('=================== fim defineNucleo==================\n')
                         
        print('4','Calcula a quantidade de Milho por animal / dia a cada periodo')
    def kgMilho(self):
        step =self.step
        if  self.D != 0:
            dictMilhokgOld = dictMilhokg
            lMkgOld = list(dictMilhokgOld.values())
        else:
            lMkgOld=[]
        
        lMkgNew = []
        Cons = 0.026
        #umidM = 1
        #umidN = 1
        for i in range(len(self.lDias)):
           if  i ==0:
              cteM1 = ((1 - self.lNucleo[i])*(Cons/3))
              #print(cteM1)
              mkg = round((self.lPeso[i]*cteM1),2)
              lMkgNew.append(mkg)   
           elif i==1:
              cteMilho = (1 - self.lNucleo[i])*((Cons)/2)
              mkg = round((self.lPeso[i]*cteMilho),2)
              lMkgNew.append(mkg)
           else:
              cteMilho = (1 - self.lNucleo[i])*((Cons))
              mkg = round((self.lPeso[i]*cteMilho),2)
              lMkgNew.append(mkg)
        #print('lMkgNew===', lMkgNew, (2*'\n'))
        
        if self.D !=0:
            #print('Cria a nova lista de Kg de Milho')
            ('________________________________________________________')
            self.lMilhokg = lMkgOld[:self.D] + lMkgNew[self.D:]
            ('________________________________________________________')
        else:
            self.lMilhokg = lMkgNew
        
        ('____Converte 2 listas nroperiodos e Milhokg em dict____')
        self.dictMilhokg = dict(zip(self.lDias, self.lMilhokg))

        print('___________________Cria MilhokgStep__________')
        self.lMilhokgStep = self.makeList(self.lMilhokg, self.step) #*****
        #print('self.lMilhokgStep ==', self.lMilhokgStep, 2*'\n' )
        
        '___________________Cria dictAll__________'
        self.dictAll['Quantidade Milho'] = self.lMilhokg
        self.dictAllStep['Quantidade Milho'] = self.lMilhokgStep
        #print(self.dictAll,'\n',self.dictAllStep)
        
        print('=================== fim kgMilho=======================\n')
        
        print('5','Calcula a quantidade de Nucleo por animal / dia')
    def kgNucleo(self):
       
        step = self.step
        if self.D != 0:
            dictNucleokgOld = dictNucleokg
            lNkgOld = list(dictNucleokgOld.values())
        else:
            lNkgOld = []
            
        lNkgNew = []
        Cons = 0.026
        umidM = 1
        umidN = 1
        for i in range(len(self.lDias)):
            if  i ==0:  
                cten = (self.lNucleo[i])*((Cons/umidN)/3)
                nkg = round((self.lPeso[i]*cten),2)
                lNkgNew.append(nkg)                          
            elif i==1:
                cten = (self.lNucleo[i])*((Cons/umidN)/2)
                nkg = round((self.lPeso[i]*cten),2)
                lNkgNew.append(nkg)
            else:
                cten = (self.lNucleo[i])*((Cons/umidN))
                nkg = round((self.lPeso[i]*cten),2)
                lNkgNew.append(nkg)
        #print('lNkgNew====', lNkgNew, (2*'\n'))
        if self.D != 0:
            #print('Cria lista mixta de Kg de Nucleo')
            ('________________________________________________________')
            self.lNucleokg = lNkgOld[:self.D] + lNkgNew[self.D:]
            ('________________________________________________________')
        else:
            self.lNucleokg = lNkgNew
        ('____Converte 2 listas nroperiodos e Nucleokg em dict____')
        self.dictNucleokg = dict(zip(self.lDias, self.lNucleokg))
        self.dictAll['Qtde Nucleo'] = self.lNucleokg
        
        print('___________________Cria NucleokgStep__________')
        self.lNucleokgStep = self.makeList(self.lNucleokg, self.step) #*******
        
        '___________________Cria dictAll__________'
        self.dictAll['Quantidade Nucleo'] = self.lNucleokg
        self.dictAllStep['Quantidade Nucleo'] = self.lNucleokgStep
        print('=================== fim kgNucleo=====================\n')
        
        print('6','Calcula o  custo do  Milho por animal / dia')
    def custoMilho(self):

        if self.D != 0:
            dictMilhoCostOld = dictMilhoCost
            lMcOld = list(dictMilhoCostOld.values())

        else:
            lMcOld = []
        
        lMcNew =  []
        milhoCost = self.commodities.get('milho')[2]
        self.lMilhokg = list(self.dictMilhokg.values())

        for kg in self.lMilhokg:
            rMilho = round((kg*1*milhoCost),2)
            lMcNew.append(rMilho)
        
        if self.D !=0:
            #print('Cria lista mixta do Custo do Milho')
            ('_________________________________________________________')
            self.lMilhoCost = lMcOld[:self.D] + lMcNew[self.D:]
            ('_________________________________________________________')
        else:
            self.lMilhoCost = lMcNew
        ('___Converte 2 listas nroperiodos e lMilhoCost  em dict____')
        #self.dictMilhoCost = dict(zip(self.lDias, self.lMilhoCost))
        self.dictAll['Custo Milho'] = self.lMilhoCost
        self.lMilhoCostStep = self.makeList(self.lMilhoCost, self.step) #*********
        
        '___________________Cria dictAll__________'
        self.dictAll['Custo Milho'] = self.lMilhoCost
        self.dictAllStep['Custo Milho'] = self.lMilhoCostStep
        print('=================== fim milhoCost=====================\n')
        
        print('7','Calcula o  custo do  Nucleo por animal / dia')    
    def custoNucleo(self):
        
        if self.D != 0:
            
            dictNucleoCostOld = dictNucleoCost
            lNcOld = list(dictNucleoCostOld.values())
        else:
            lNcOld = []
        lNcNew =  []
        nucleoCost = self.commodities.get('nucleo')[2]
        #print(nucleoCost)
        for kg in self.lNucleokg:
            rNucleo = round((kg*1*nucleoCost),2)
            lNcNew.append(rNucleo)
        
        if self.D != 0:
            #print('Cia lista mixta Custo do Nucleo')
            ('_________________________________________________________')
            self.lNucleoCost = lNcOld[:self.D]+lNcNew[self.D:]
            ('_________________________________________________________')
        else:
            self.lNucleoCost = lNcNew
        ('___Converte 2 listas nroperiodos e lNucleoCost  em dict____')
        self.dictNucleoCost = dict(zip(self.lDias, self.lNucleoCost))
        self.dictAll['Custo Nucleo'] = self.lNucleoCost
        self.lNucleoCostStep = self.makeList(self.lNucleoCost, self.step)
        
        '___________________Cria dictAll__________'
        self.dictAll['Custo Nucleo'] = self.lNucleoCost
        self.dictAllStep['Custo Nucleo'] = self.lNucleoCostStep
        print('=================== fim NucleoCost=====================\n')
        
        print('8','Calcula o  Custo por Dia Total por animal / dia')
    def custo_Dia(self):
        
        if self.D != 0:
            dictCustoDiaOld = dictCustoDia
            lcold = list(dictCustoDiaOld.values())
        else:
            lcold = []
        lcnew = []
        lcnew = [round((cmd+cnd),2) for cmd, cnd in zip(self.lMilhoCost, self.lNucleoCost)]
        
        if self.D != 0:
            ('_________________________________________________________')
            self.lCustoDia = lcold[:self.D] + lcnew[self.D:]
            ('_________________________________________________________')
        else:
            self.lCustoDia = lcnew
            
        ('___Converte 2 listas nroperiodos e lMilhoCost  em dict____')
        self.dictCustoDia = dict(zip(self.lDias, self.lCustoDia))
        self.dictAll['Custo Alimentação'] = self.lCustoDia
        self.lCustoDiaStep = self.makeList(self.lCustoDia, self.step)
        
        '___________________Cria dictAll__________'
        self.dictAll['Custo Dia'] = self.lCustoDia
        self.dictAllStep['Custo Dia'] = self.lCustoDiaStep
        print('=================== fim CustoDia=====================\n')
        
        print('9','Calcula o  Custo Acumulado Total por animal / dia')
    def custo_acumulado_total(self):
        
        if self.D != 0:
            dictCustoAcumOld = dictCustoAcum
            lCAold = list(dictCustoAcumOld.values())
        else:
            lCAold = []
        lCAnew = []

        soma = 0
        step = 1
        lCustoStep = []
        lCustoStep = [ round((c*step),2) for c in self.lCustoDia]
        
        for i in lCustoStep:
             a = round((i),2)
             soma += a
             lCAnew.append(round((soma),2))  
        
        if self.D != 0:
            #print('Cria lista Custo Acumulado Total')
            ('________________________________________________________')
            self.lCustoAcum = lCAold[:self.D] + lCAnew[self.D:]
            ('________________________________________________________')
        else:
            self.lCustoAcum = lCAnew
        
        ('___ Cria dictCustoAcum____')
        self.dictCustoAcum = dict(zip(self.lDias, self.lCustoAcum))
        self.dictAll['Custo Acumulado'] = self.lCustoAcum
       
        self.lCustoAcumStep = self.makeList(self.lCustoAcum, self.step)
        
        '___________________Cria dictAll__________'
        self.dictAll['Custo Acumulado'] = self.lCustoAcum
        self.dictAllStep['Custo Acumulado'] = self.lCustoAcumStep
        print(self.dictAll,'\n',self.dictAllStep, 2*'\n')
        print('=================== fim Custo Acumulado=============\n')
        dictAll = self.dictAll
        dictAllStep = self.dictAllStep
        
        '@@@@@@@@@@@@@@@@@__Save dictAll___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        import json
        dictAll = json.dumps(dictAll,  indent=True)
        with open ("dictAll.json", 'w+') as file:
            file.write(dictAll)
        dictAllStep = json.dumps(dictAllStep,  indent=True)
        with open ("dictAllStep.json", 'w+') as file:
            file.write(dictAllStep)
        '@@@@@@@@@@@@@@@@@__Fim Save arq___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        
        print('10', 'Faz a Análise de Lucratividade   \n')
    def analise_lucratividade(self, m):
        
        print(m*'=')
        #w = int(input("Digite o dia que quer a  analise lucratividade: "))
        texto = "Digite o dia que quer a  analise lucratividade: "
        while True:
            try:
                w = int(input(texto ))
                if w > (self.choices.get('time')[0])*30:
                    raise ValueError
                else:
                    break
            except ValueError:
                texto = 'Dia excede o numero dias de confinamento. Digite novamente: '
                #w = int(input("Data excede o numero de dias de confinamento: Digite outro dia "))      
        
        k= w - 1
        self.cTMD = round((self.lCustoAcum[k]),2) + self.choices.get('preço_medio')[0]       #custo do animal em @ no mes desejado
        self.profitAll['Custo do Animal'] = [self.cTMD]
        self.pAMD = round((self.lPeso[k]/30),2)          #peso do animal em @ no mes desejado
        self.profitAll['Peso do Animal'] = [self.pAMD]
        self.pvAMD = round((self.pAMD)*(self.commodities.get('arroba_boi')[1]),2)     #preco de venda animal em R$ no mes desejado
        self.profitAll['Preço de venda'] = [self.pvAMD]
        self.lucroAMD = round((self.pvAMD - self.cTMD),2)   #lucro do animal em R$ no mes desejado)
        self.profitAll['Lucro por Animal'] = [self.lucroAMD]
        lucratividade = round(((((self.pvAMD/self.cTMD)-1)*100)),2)
        self.profitAll['Lucratividade'] = [self.lucroAMD]

        self.listaNomes = ['Custo do Animal', 'Peso do Animal', 'Preço de venda', 'Lucro por Animal',  'Lucratividade']
        self.listaVar = [[self.cTMD, '(R$)'],
                         [self.pAMD, " (@)"], [self.pvAMD, '(R$)'],
                         [self.lucroAMD, '(R$)'],
                         [lucratividade, '(%)'] ]
        
        self.dictLucratividade = dict(zip( self.listaNomes, self.listaVar))
        self.lNomesLote = ['Custo Total do Lote', 'Peso Médio do Lote ', 'Valor de Venda do Lote', 'Lucro Medio Lote',  'Lucratividade Lote']
        cabecas = self.choices.get('quantidade')[0]
        self.lVarLote = [[round((self.cTMD*cabecas),2), ' (R$)'],
                         [round((self.pAMD*cabecas),2), ' (@)'],
                         [round((self.pvAMD*cabecas),2), ' (R$)'],
                         [round((self.lucroAMD*cabecas),2), ' (R$)'],
                         [round(((((self.pvAMD/self.cTMD)-1)*100)),2), ' (%)'] ]
        self.dictLote = dict(zip(self.lNomesLote, self.lVarLote ))
        
        print(m*'=')  
        
    def delta_peso(self, m):
        # Pesagem do Lote numa data especifica  apos o iicio do confinamento
        logicaDT.data_dias( 85)
        
    
    def print_resultados(self, m):
                             
        import pandas as pd   
        #from tabulate import tabulate        
        
        print (2*'\n')
        print(m*'_')
        print ('{:^75}'.format('Tabela de Resultados'))
        print(m*'=')
        df = pd.DataFrame(self.dictAllStep)
        #df = pd.DataFrame(self.dictAllStep)
        
        blankIndex=[''] * len(df)  #Tira a aprimeira coluna
        df.index=blankIndex
        df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
        #print(df.to_markdown(index=False)) 
        #print(df)
        print(df_tr)
        print('')
        #print(df.to_string(index=False))
        print(m*'_')
  
        
         
    def print_lucratividade(self, m):
        
        import pandas as pd
        print(m*'_')
        print ('{:^75}'.format('Inicio Tabela de Lucratividade por Animal'))
        print(m*'=')
        
        #print(self.listaNomes)
        #print(self.listaVar)
        #df = pd.DataFrame(self.dictLucratividade)
        '''
        df = pd.DataFrame(self.listaVar, index=self.listaNomes, columns=['Valores', 'Unidades']) 
        #df['Valores'] = df['Valores'].map('{:,.2f}'.format)
        print(df)
        '''
        df = pd.DataFrame(self.listaVar, index=self.listaNomes, columns=['Valores', 'Unidades']) 
        df['Valores'] = df['Valores'].map('{:,.2f}'.format)
        print(df)
        
        '''
        blankIndex=[''] * len(df)  #Tira a aprimeira coluna
        df.index=blankIndex
        df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
        #print(df.to_markdown(index=False)) 
        print(df_tr)
        '''
        print(m*'_')
        #print('')  
        
        print ('\n')
        print(m*'_')
        print ('{:^75}'.format('Tabela de Lucratividade do Lote'))
        print(m*'=')
        df = pd.DataFrame(self.lVarLote, index=self.lNomesLote, columns=['Valores', 'Unidades']) 
        df['Valores'] = df['Valores'].map('{:,.2f}'.format)
        print(df)
        '''
        df = pd.DataFrame(self.dictLote)
        #df[1] = df[1].map('${:,.2f}'.format)
        blankIndex=[''] * len(df)  #Tira a aprimeira coluna
        df.index=blankIndex
        df_tr = df.transpose() #Inverte Linha x Coluna no Dataframe
        #print(df.to_markdown(index=False)) 
        print(df_tr)
        '''
        print('')
        #print(df.to_string(index=False))
        print(m*'_')
        
        #____________________Print Dados Todos__________________________
        #      
       
    def trato_animais(self):
        periodos = [ round((a/10),2) for a in self.lDias]
        self.timePeso = dict(zip(periodos, self.lPeso))
        print(self.timePeso)
        print (3*'\n')
              
    def print_trato_animais(self, m):
              palavra  = ['Periodos', 'Peso do animal', 'Kg Milho/dia/animal', 'Kg Nucleo/dia/animal']         
    

#commodities ==>  {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]} 

#choices==>  {'origem': ['Adquirido'], 'porte': ['Mais 90 kg'], 'peso_medio': [2.0],             'preço_medio': [2.0], 'sexo': ['Femea'], 'raça': ['HPB'], 'quantidade': [2], 'GDP': [2], 'time': [2]}


print('_______________________FIM___________________________________')

"""
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

a = logicaDT(10,0, commodities, choices)
a.time()
stop= input('stop')

a.peso_animais()

a.defineNucleo()
stop= input('stop')

a.kgMilho()
stop= input('stop')

a.kgNucleo()
stop= input('stop')

a.custoMilho()
stop= input('stop')

a.custoNucleo()
stop= input('stop')

a.custo_Dia()
stop= input('stop')

a.custo_acumulado_total()
stop= input('stop')
 
a. trato_animais()
stop= input('stop')

a.print_trato_animais(75)
stop= input('stop')
a.print_resultados(75)
stop= input('stop')
a.analise_lucratividade(75)
stop= input('stop')
a.print_lucratividade(75)
stop= input('stop')
print('fim')
"""