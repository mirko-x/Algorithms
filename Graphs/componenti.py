#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 06:21:49 2024

@author: mirko
"""

import networkx as nx
import matplotlib.pyplot as plt

G=[[1,5],[0,5],[4],[],[2],[0,1]]
#G=[[1,3,2],[0,3],[0],[1,0]]
g = nx.Graph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    if  not vicini :  # Nodo isolato
        g.add_node(i)
    else :
        for vicino in vicini:
         g.add_edge(i, vicino)
        
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()


def comp(x,G,C,rgb):
    C[x]=rgb
    for y in G[x]:
        if C[y]==0:
          comp(y, G, C, rgb)         
    return C

def componenti(G):
 C=[0]*len(G)
 rgb=0
 for i in range(len(G)):
    if C[i]==0:
        rgb+=1
        comp(i,G,C,rgb)
 return C

C=(componenti(G))
print(componenti(G))

def connesso(C) :   
 for i in range (len(C)-1):
    if C[i]!=C[-1]:
       return False
 return True
        
print(connesso(C))