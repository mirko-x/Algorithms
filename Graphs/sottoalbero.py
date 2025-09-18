#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:49:11 2024

@author: mirko
Sia P vettore padri di un albero con n nodi e sia x un nodo vogliamo il sotto albero 
radicato in x , ritornato come lista dei nodi 
"""

P=[0,3,4,3,5,3,4,5,1]

def radx(x,P,SA):
    SA.append(x)
    for i in range (len(P)):
        if P[i]==x :
            radx(i,P,SA)
    return SA
    
print(radx(5,P,[]))
    