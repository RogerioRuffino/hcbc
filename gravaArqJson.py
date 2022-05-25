# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:29:38 2021

@author: Windows 11
"""
class gravaJson(arq, text):
    
    
    '@@@@@@@@@@@@@@@@@__Save arq___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    import json
    arquivo = json.dumps(arq,  indent=True)
    with open (text, 'w+') as file:
    #with open ("arq.json", 'w+') as file:
        file.write(arq)
    '@@@@@@@@@@@@@@@@@__Fim Save arq___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
