# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:28:07 2021

@author: rogerio
"""
import sys
sys.path.append('C:/Users/rogerio/OneDrive/Rogerio/rogerPythonTkinterApps/rogerEngordaBezerrosPyhon/Working/fullWorking')

from geraPesagem import *
m= 30
a = geraPesagem(choices, dictPeso)
a.dataInConfinamento( m)
a.dataPesagem( m)
a.pesagem( m)