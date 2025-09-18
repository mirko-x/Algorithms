#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 02:39:22 2024

@author: mirko
"""
def esz(P,V):
 def zaino(P,V,c,i,sol,val,valR,peso):
    n=len(V)
    if i==n:
        nonlocal val0,sol0
        if val>val0:
            sol0=sol.copy()
            val0=val
    else:
        if val+valR-V[i]>val0:
            sol.append(0)
            zaino(P, V, c, i+1, sol, val, valR-V[i], peso)
            sol.pop()
            
        if peso+P[i]<=c:
            sol.append(1)
            zaino(P, V, c, i+1, sol, val+V[i], valR-V[i], peso+P[i])
            sol.pop()
    
 val0=-1
 sol0=[]
 zaino(P, V, 166, 0, [], 0, sum(V), 0)
 print(sol0,val0)

P=[23,31,29,89,44,53,38,63,85,82]     
V=[92,57,49,87,68,60,43,67,84,72] 

esz(P, V)

print("===================================================================")














