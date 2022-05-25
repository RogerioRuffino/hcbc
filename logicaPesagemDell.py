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
                 dictAllStep={} ):
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
        print("commodities imported transp", self.commodities) #precos commodities para todos animais
        print("choices imported trans", self.choices)
        print("a i manezao ====>", self.choices.get('time')[0])
        "====================================================================="
        "==================Início funções lucratividade======================="    
    def time(self):
        
        print('1','Cria Lista de dias de confinamento')
        #print('self.step',  self.step)
        meses = self.choices.get('time')[0]
        #print(meses)
        self.lDias = [ dia+1 for dia in range(meses*30)]
        self.lStep = [p for p in range(self.step,meses*30+self.step,self.step)]
        self.lNroStep = [nro for nro in range(1,(len(self.lStep)+1))]
        self.dictStep = dict(zip(self.lNroStep, self.lStep))
        
        '____Teste print funcão______'
        #print('self.lDias', self.lDias,2*'\n')
        #print('self.lStep', self.lStep, 2*'\n')
        #print('self.lNroStep', self.lNroStep, 2*'\n')
        #print('self.dictStep', self.dictStep, 2*'\n')
    
        '___________________Cria dictAll__________'
        self.dictAll['Dias'] = self.lDias
        self.dictAllStep['Periodos'] = self.lStep
        #print('self.dictAll -> ', self.dictAll)
        print('========================= fim time==========================\n')
   
        print('2','Cria lista de pesos medios dos animais para cada dia de confin')
    def peso_animais(self):
        
        if  self.D != 0:    
            #lPesoStepOld=[]
            dictPesoOld =dictPeso #inserir self.
            lPesoOld = list(dictPesoOld.values())
            lPesoStepOld = self.makeList(lPesoOld, self.step)
            dictPesoStepOld = dict(zip(self.lNroStep, lPesoStepOld))
            #print ('dictPesoStepOld===',dictPesoStepOld)    
            print('lPesoOld',lPesoOld, 2*'\n')
            #print('lPesoStepOld', lPesoStepOld, 2*'\n')
            #GDP = self.choices.get('GDP')[0]
            #print('self.GDPnew: ',  self.GDPnew)
        else:
            lPesoStepOld=[]
            
            
        lPesonew = lPesoStepnew = []
        ##print('self.step: ', self.step,'\n')
        ##print('self.D: ',  self.D, 2*'\n')
        
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
        #print('self.PesoStep = ', self.lPesoStep, (2*'\n'))
        
        
        '___________________Cria dictAll__________'
        self.dictAll['Peso '] = self.lPeso
        #print('\n')
        self.dictAllStep['Peso Step '] = self.lPesoStep
        print('=================== fim peso_animais======================\n')
        
        print('3','Define a porcentagem de proteinas no Nucleo a cada 10 dias')         
    def defineNucleo(self):
        
        step=self.step
        lN = lNnew = []
        
        dictPesoOld =dictPeso #inserir self.
        ##print('dictPesoOld',  dictPesoOld, (2*'\n'))
        dictNucleoOld=self.dictNucleo
        lNucleoOld = list(dictNucleoOld.values())
        #print(lNucleoOld,'\n')
        ##print('dictNucleoOld', dictNucleoOld, (2*'\n'))
        
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
        ('________________________________________________________')
        self.lNucleo = lNucleoOld[:self.D]+lNnew[self.D:]        
        ('________________________________________________________')
        
        ('_____Converte 2 listas nroperiodos e nucleo em dict____')
        self.dictNucleo = dict(zip(self.lDias, self.lNucleo))
        
        ('_____Converte 2 listas nroperiodos e nucleo em dict____')
        #print('dictNucleoOld', dictNucleoOld, (2*'\n'))
        #print('self.dictNucleo', self.dictNucleo, (2*'\n'))
        
        #print('___________________Cria NucleoStep__________')
        self.lNucleoStep = self.makeList(self.lNucleo, self.step)
        #print('self.lNucleoStep ==', self.lNucleoStep, 2*'\n' )
        '___________________Cria dictAll__________'
        self.dictAll['Proteina Nucleo'] = self.lNucleo
        self.dictAllStep['Proteina Nucleo'] = self.lNucleoStep
        #print(' aki bestalhao dictAllStep','\n',self.dictAllStep)
        print('=================== fim defineNucleo==================\n')
                         
        print('4','Calcula a quantidade de Milho por animal / dia a cada periodo')
    def kgMilho(self):
        step =self.step
        dictMilhokgOld = dictMilhokg
        #print('self.lPeso=====',self.lPeso, (2*'\n'))
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
        lMkgOld = list(dictMilhokgOld.values())
        ('________________________________________________________')
        self.lMilhokg = lMkgOld[:self.D] + lMkgNew[self.D:]
        ('________________________________________________________')
        
        ('____Converte 2 listas nroperiodos e Milhokg em dict____')
        self.dictMilhokg = dict(zip(self.lDias, self.lMilhokg))
        #print ('dictMilhokgOld = ', dictMilhokgOld, (2*'\n'))
        #print('self.dictMilhokg', self.dictMilhokg, (2*'\n'))
        print('self.lMilhokg', self.lMilhokg, (2*'\n'))

        print('___________________Cria MilhokgStep__________')
        self.lMilhokgStep = self.makeList(self.lMilhokg, self.step) #*****
        print('self.lMilhokgStep ==', self.lMilhokgStep, 2*'\n' )
        
        '___________________Cria dictAll__________'
        self.dictAll['Quantidade Milho'] = self.lMilhokg
        self.dictAllStep['Quantidade Milho'] = self.lMilhokgStep
        #print(' aki bestalhao dictAllStep','\n',self.dictAllStep)
        
        print('=================== fim kgMilho=======================\n')
        
        print('5','Calcula a quantidade de Nucleo por animal / dia')
    def kgNucleo(self):
       
        step = self.step
        dictNucleokgOld = dictNucleokg
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
        lNkgOld = list(dictNucleokgOld.values())
        ('________________________________________________________')
        self.lNucleokg = lNkgOld[:self.D] + lNkgNew[self.D:]
        ('________________________________________________________')
        
        ('____Converte 2 listas nroperiodos e Nucleokg em dict____')
        self.dictNucleokg = dict(zip(self.lDias, self.lNucleokg))
        self.dictAll['Qtde Nucleo'] = self.lNucleokg
        #print('dictNucleokgOld', dictNucleokgOld, (2*'\n'))         
        #print('self.dictNucleokg', self.dictNucleokg, (2*'\n'))         
        
        print('___________________Cria NucleokgStep__________')
        self.lNucleokgStep = self.makeList(self.lNucleokg, self.step) #*******
        #print('self.lNucleokgStep ==', self.lNucleokgStep, 2*'\n' )
        
        '___________________Cria dictAll__________'
        self.dictAll['Quantidade Nucleo'] = self.lNucleokg
        self.dictAllStep['Quantidade Nucleo'] = self.lNucleokgStep
        #print(' aki bestalhao dictAllStep','\n',self.dictAllStep, 2*'\n')
        print('=================== fim kgNucleo=====================\n')
        
        print('6','Calcula o  custo do  Milho por animal / dia')
    def custoMilho(self):

        #step = self.step
        dictMilhoCostOld = dictMilhoCost
        #print('dictMilhoCostOld', dictMilhoCostOld, 2*'\n')
        
        lMcNew =  []
        milhoCost = self.commodities.get('milho')[2]
        #print('dictMilhoOld', dictMilhokg,2*'\n')
        #print('dictMilhokg', self.dictMilhokg, 2*'\n')
        self.lMilhokg = list(self.dictMilhokg.values())

        for kg in self.lMilhokg:
            rMilho = round((kg*1*milhoCost),2)
            lMcNew.append(rMilho)
        #print('lMcNew --',lMcNew,2*'\n')
        
        lMcOld = list(dictMilhoCostOld.values())
        #print('lMcOld=', lMcOld,2*'\n')
        ('_________________________________________________________')
        self.lMilhoCost = lMcOld[:self.D] + lMcNew[self.D:]
        ('_________________________________________________________')
        #print('self.MilhoCost', self.lMilhoCost, 2*'\n')
        
        ('___Converte 2 listas nroperiodos e lMilhoCost  em dict____')
        self.dictMilhoCost = dict(zip(self.lDias, self.lMilhoCost))
        self.dictAll['Custo Milho'] = self.lMilhoCost
        #print('dictMilhoCostOld', dictMilhoCostOld, 2*'\n')
        #print('self.dictMilhoCost', self.dictMilhoCost, 2*'\n')         
        #print('=================== fim milhoCost=====================\n')
        
        #print('___________________Cria Custo Milho Step__________')
        self.lMilhoCostStep = self.makeList(self.lMilhoCost, self.step) #*********
        #print('self.lMilhoCostStep ==', self.lMilhoCostStep, 2*'\n' )
        
        '___________________Cria dictAll__________'
        self.dictAll['Custo Milho'] = self.lMilhoCost
        self.dictAllStep['Custo Milho'] = self.lMilhoCostStep
        #print(' aki bestalhao dictAllStep','\n',self.dictAllStep, 2*'\n')
        print('=================== fim milhoCost=====================\n')
        
        print('7','Calcula o  custo do  Nucleo por animal / dia')    
    def custoNucleo(self):
        
        dictNucleoCostOld = dictNucleoCost
        lNcOld = list(dictNucleoCostOld.values())
        #print('dictNucleoCostOld', dictNucleoCostOld, 2*'\n')
        
        lNcNew =  []
        nucleoCost = self.commodities.get('nucleo')[2]
        #print(nucleoCost)
        for kg in self.lNucleokg:
            rNucleo = round((kg*1*nucleoCost),2)
            lNcNew.append(rNucleo)
        ('_________________________________________________________')
        self.lNucleoCost = lNcOld[:self.D]+lNcNew[self.D:]
        ('_________________________________________________________')
        
        ('___Converte 2 listas nroperiodos e lNucleoCost  em dict____')
        self.dictNucleoCost = dict(zip(self.lDias, self.lNucleoCost))
        self.dictAll['Custo Nucleo'] = self.lNucleoCost
        #print('dictNucleoCostOld', dictNucleoCostOld,2*'\n')         
        #print('self.dictNucleoCost', self.dictNucleoCost,2*'\n')         
        
        #print('___________________Cria Custo Nucleo Step__________')
        self.lNucleoCostStep = self.makeList(self.lNucleoCost, self.step)
        #print('self.lNucleoCostStep ==', self.lNucleoCostStep, 2*'\n' )
        
        '___________________Cria dictAll__________'
        self.dictAll['Custo Nucleo'] = self.lNucleoCost
        self.dictAllStep['Custo Nucleo'] = self.lNucleoCostStep
        #print(' aki bestalhao dictAllStep','\n',self.dictAllStep, 2*'\n')
        print('=================== fim NucleoCost=====================\n')
        
        print('8','Calcula o  Custo por Dia Total por animal / dia')
    def custo_Dia(self):
        dictCustoDiaOld = dictCustoDia
        lcold = list(dictCustoDiaOld.values())
        lcnew = []
        lcnew = [round((cmd+cnd),2) for cmd, cnd in zip(self.lMilhoCost, self.lNucleoCost)]
        #print('lcnew===========', lcnew, 2*'\n')
        ('_________________________________________________________')
        self.lCustoDia = lcold[:self.D] + lcnew[self.D:]
        #print('self.lCustoDia', self.lCustoDia, 2*'\n')
        ('_________________________________________________________')
        
        ('___Converte 2 listas nroperiodos e lMilhoCost  em dict____')
        self.dictCustoDia = dict(zip(self.lDias, self.lCustoDia))
        self.dictAll['Custo Alimentação'] = self.lCustoDia
        #print('dictCustoDiaOld', dictCustoDiaOld,2*'\n')         
        #print('self.dictCustoDia', self.dictCustoDia,2*'\n')         
        
        #print('___________________Cria Custo Dia Step__________')
        self.lCustoDiaStep = self.makeList(self.lCustoDia, self.step)
        #print('self.lCustoDiaStep ==', self.lCustoDiaStep, 2*'\n' )
        
        '___________________Cria dictAll__________'
        self.dictAll['Custo Dia'] = self.lCustoDia
        self.dictAllStep['Custo Dia'] = self.lCustoDiaStep
        #print(' aki bestalhao dictAllStep','\n',self.dictAllStep, 2*'\n')
        print('=================== fim CustoDia=====================\n')
        
        print('9','Calcula o  Custo Acumulado Total por animal / dia')
    def custo_acumulado_total(self):
        dictCustoAcumOld = dictCustoAcum
        lCAold = list(dictCustoAcumOld.values())
        #print('lcaold', lCAold, 2*'\n' )
        lCAnew = []

        soma = 0
        step = 1
        lCustoStep = []
        lCustoStep = [ round((c*step),2) for c in self.lCustoDia]
        
        #print('lCustoStep', lCustoStep, 2*'\n' )           
        for i in lCustoStep:
             a = round((i),2)
             soma += a
             lCAnew.append(round((soma),2))  
        #print('lCAnew', lCAnew, 2*'\n' )
        ('________________________________________________________')
        self.lCustoAcum = lCAold[:self.D] + lCAnew[self.D:]
        ('________________________________________________________')
        
        ('___Converte 2 listas nroperiodos e lMilhoCost  em dict____')
        self.dictCustoAcum = dict(zip(self.lDias, self.lCustoAcum))
        self.dictAll['Custo Acumulado'] = self.lCustoAcum
        #print('dictCustoAcumOld', dictCustoAcumOld, 2*'\n' )         
        #print('self.dictCustoAcum', self.dictCustoAcum, 2*'\n' )         
       
        #print('10','Calcula a lucratividade')
        
        #print('___________________Cria Custo Acumulado Step__________')
        self.lCustoAcumStep = self.makeList(self.lCustoAcum, self.step)
        #print('self.lCustoAcumStep ==', self.lCustoAcumStep, 2*'\n' )
        
        '___________________Cria dictAll__________'
        self.dictAll['Custo Acumulado'] = self.lCustoAcum
        self.dictAllStep['Custo Acumulado'] = self.lCustoAcumStep
        #print(' dictAll = ',self.dictAll, 2*'\n')
        #print(' dictAllStep = ',self.dictAllStep, 2*'\n')
        #print('=================== fim CustoDia=====================\n')
        
        print('10', 'Faz a Anákise de Lucratividade   \n')
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
        #print(self.cTMD)
        self.pAMD = round((self.lPeso[k]/30),2)          #peso do animal em @ no mes desejado
        self.profitAll['Peso do Animal'] = [self.pAMD]
        #print(self.pAMD)
        self.pvAMD = round((self.pAMD)*(self.commodities.get('arroba_boi')[1]),2)     #preco de venda animal em R$ no mes desejado
        self.profitAll['Preço de venda'] = [self.pvAMD]
        #print(self.pvAMD)
        self.lucroAMD = round((self.pvAMD - self.cTMD),2)   #lucro do animal em R$ no mes desejado)
        self.profitAll['Lucro por Animal'] = [self.lucroAMD]
        lucratividade = round(((((self.pvAMD/self.cTMD)-1)*100)),2)
        self.profitAll['Lucratividade'] = [self.lucroAMD]

        self.listaNomes = ['Custo do Animal', 'Peso do Animal', 'Preço de venda', 'Lucro por Animal',  'Lucratividade']
        self.listaVar = [[self.cTMD, '(R$)'],
                         [self.pAMD, " (@)"], [self.pvAMD, '(R$)'],
                         [self.lucroAMD, '(R$)'],
                         [lucratividade, '(%)'] ]
        '''
        self.listaVar = [[self.cTMD],
                         [self.pAMD],
                         [self.pvAMD],
                         [self.lucroAMD],
                         [lucratividade] ]
        '''
        self.dictLucratividade = dict(zip( self.listaNomes, self.listaVar))
        #print('listaVar', self.listaVar)
        self.lNomesLote = ['Custo Total do Lote', 'Peso Médio do Lote ', 'Valor de Venda do Lote', 'Lucro Medio Lote',  'Lucratividade Lote']
        #lVarLote = [[(round(self.cTMD*self.commodities.get('quantidade')[0]))+' '+('R$')], [str(self.pAMD*self.commodities.get('quantidade')[0])+' '+(" Kg")], [str(self.pvAMD*self.commodities.get('quantidade')[0])+' '+'R$'], [str(self.lucroAMD*self.commodities.get('quantidade')[0])+' '+'R$'], [str(lucratividade)+'  '+'%'] ]
        cabecas = self.choices.get('quantidade')[0]
        #print(cabecas)
        self.lVarLote = [[round((self.cTMD*cabecas),2), ' (R$)'],
                         [round((self.pAMD*cabecas),2), ' (@)'],
                         [round((self.pvAMD*cabecas),2), ' (R$)'],
                         [round((self.lucroAMD*cabecas),2), ' (R$)'],
                         [round(((((self.pvAMD/self.cTMD)-1)*100)),2), ' (%)'] ]
        self.dictLote = dict(zip(self.lNomesLote, self.lVarLote ))
        
        #print('dictLote', self.dictLote)
        #print('custo =%s %.2f, peso = %.2f, preço venda  %.2f, lucro = %.2f'%('R$' ,self.cTMD, self.pAMD, self.pvAMD, self.lucroAMD))       
        #print(m*'=')  
        
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

commodities = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
choices = {'origem': ['Adquirido'], 'porte': ['Mais 85 kg'], 'peso_medio': [100.0], 'preço_medio': [2.0], 'sexo': ['Femea'], 'raça': ['HPB'], 'quantidade': [2], 'GDP': [2.0], 'time': [2]}

a = logicaDT(10,0, commodities, choices)
a.time()
a.peso_animais()


"""
commodities = {'milho': [2.0, 2.0, 1.0], 'nucleo': [2.0, 2.0, 1.0], 'silo': [2.0, 1000, 0.0], 'ração': [2.0, 2.0, 1.0], 'bicarbonato': [2.0, 2.0, 1.0], 'sal_mineral': [2.0, 2.0, 1.0], 'arroba_boi': [2.0, 2.0, 0]}
choices = {'origem': ['Adquirido'], 'porte': ['Mais 85 kg'], 'peso_medio': [100.0], 'preço_medio': [2.0], 'sexo': ['Femea'], 'raça': ['HPB'], 'quantidade': [2], 'GDP': [2.0], 'time': [2]}

a = logicaDT(commodities, choices, 1,30, 3)
#a = logicaDT(1,30, 3)

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
    stop = input('stop')
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