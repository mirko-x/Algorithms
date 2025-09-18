#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:52:56 2024

@author: mirko
"""

import networkx as nx
import matplotlib.pyplot as plt

G=[[1],[2,3],[4],[5],[6],[],[],[0]]
g = nx.DiGraph()

for n, vicini in enumerate(G):
    for vicino in vicini:
        g.add_edge(n, vicino)
pos = nx.spring_layout(g, k=1, seed=42)

colori=[-1 for v in G]

def Bicolor(v,G,colori,rgb):
    # O(n+m) = O(m) dato che m>=n-1
    colori[v]=rgb
    for i in G[v]:
        if colori[i]==-1:
            if not Bicolor(i,G,colori,1-rgb): return False
        elif colori[i]==rgb : return False
    return colori  

print(Bicolor(7, G, colori, 0))


# Disegno del grafo
color_map = ['red' if c == 0 else 'green'  for c in colori]

# Disegno del grafo con i colori specificati
nx.draw(g, pos, edge_color="black", with_labels=True, node_color=color_map, node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()
