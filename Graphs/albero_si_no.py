#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 01:51:00 2024

@author: mirko
"""

import networkx as nx
import matplotlib.pyplot as plt
"""Progetta un algoritmo che, dato un grafo G, in tempo O(n) verifica se è
un albero o meno."""

G=[[2,1,3,4],[4],[],[],[2]]
G=[[2,1,3],[4],[],[],[0,2]]
G=[[1,2,3],[4],[5],[6],[],[],[]]

g = nx.DiGraph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    if  not vicini :  # Nodo isolato
        g.add_node(i)
    else :
        for vicino in vicini:
         g.add_edge(i, vicino)
         
pos = nx.spring_layout(g, k=1, seed=50)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()

def dfs(r, p , vis):
    vis[r] = True
    for v in G[r]:
        if not vis[v]:
            if not dfs(v, r,vis):
                return False

        elif r != p:
            return False
    return True

def is_tree(G):
    vis = [0] *len(G)
    # Verifica l'aciclicità e la connessione 
    if not dfs(0, 0,vis):
        return False
    
    if not all(vis):
         return False
    
    return True


print(is_tree(G))