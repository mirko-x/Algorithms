#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 17:23:00 2024

@author: mirko
"""
import networkx as nx
import matplotlib.pyplot as plt

G=[[1],[],[1],[1,2],]

g = nx.DiGraph()
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


def sorTop(G):
    n=len(G)
    gradi=[0]*n
    ST=[]
    for i in range(n):
        for j in G[i]:
            gradi[j]+=1
    sorg=[i for i in range(n) if gradi[i]==0]
    print(gradi,sorg)
    while sorg :
        u=sorg.pop()
        ST.append(u)
        for v in G[u]:
            gradi[v]-=1
            if gradi[v]==0:
                sorg.append(v)
    if n==len(ST): return ST
    return []


print(sorTop(G))   


def sorTopdfs(u,G,visit,ST):
    visit[u]=1
    for v in G[u]:
        if visit[v]==0:
            sorTopdfs(v,G,visit,ST)
    ST.append(u)
    return ST
    
visit=[0]*len(G)
ST=[]
for i in range(len(G)):
    if visit[i]==0:
        ST+=(sorTopdfs(i,G,visit,[]))
ST.reverse()

print(ST)