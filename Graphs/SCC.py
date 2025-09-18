#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 05:54:15 2024

@author: mirko
"""

import networkx as nx
import matplotlib.pyplot as plt
G=[[1],[2,4,5],[5],[1,6],[0,5,7,8],[],[3],[6,8,9,10],[11],[],[8],[10]]

g = nx.DiGraph()

# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    for vicino in vicini:
        g.add_edge(i, vicino)
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()


def dfs(v,G,visit):
    #Liste di adiacenza O(n)
    visit[v]=1
    for i in G[v]:
        if not visit[i]:
            dfs(i,G,visit)
    return visit   

def G_T(G):
    GT=[[] for _ in G ]
    for i in range (len(G)):
        for v in G[i]:
            GT[v].append(i)
    return GT

def SCC(v,G):
    C=[]
    vis1=dfs(v,G,[0]*len(G))
    GT=G_T(G)
    vis2=dfs(v,GT,[0]*len(G))
    for i in range(len(G)):
        if vis1[i]==vis2[i]==1:
            C.append(i)
    return C


print(SCC(0,G))

