#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 06:26:29 2024

@author: mirko
"""

import networkx as nx
import matplotlib.pyplot as plt
G=[[1],[2,3,5],[4],[5],[6],[],[2],[0]]

g = nx.DiGraph()

# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    for vicino in vicini:
        g.add_edge(i, vicino)
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()


def cicloDag(u,G,vis):
    #O(n+m) True se ha cicli ,false altrimenti G diretto
    vis[u]=1
    for v in G[u]:
        if vis[v]==1: return True
        if vis[v]==0:
            if cicloDag(v,G,vis):
                return True
    vis[u]=2
    return False

vis=[0]*len(G)
print(cicloDag(0, G, vis))


G2=[[1],[0,2],[1]]

g2 = nx.Graph()

# Aggiunta degli archi al grafo
for i, vicini in enumerate(G2):
    for vicino in vicini:
        g2.add_edge(i, vicino)
pos = nx.spring_layout(g2, k=1, seed=42)
# Disegno del grafo
nx.draw(g2,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()


def ciclo(u,padre,G2,vis):
    vis[u]=1
    for v in G2[u]:
        if vis[v]==1 : 
             if  padre != v : return True
        elif ciclo(v,u,G2,vis):
                return True
    return False

def nondag(G2):
 vis=[0]*len(G2)
 for i in range (len(G2)):
    if vis[i]==0:
          if ciclo(i,i,G2,vis):
              return True
 return False

print(nondag(G2))

        