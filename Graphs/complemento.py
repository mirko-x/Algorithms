#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 06:40:07 2024

@author: mirko
"""
import networkx as nx
import matplotlib.pyplot as plt

G=[[1],[2,3],[1],[1,4],[3]]


g = nx.Graph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    for vicino in vicini:
        g.add_edge(i, vicino)
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()

def complemento (G):
    # Calcola il complemento del grafo in O(n^2)
    GC=[[] for _ in G]
    for j in range (len(G)):
      for i in range (len(G)):
        if i not in G[j] and i!=j:
            GC[j].append(i)
    return GC

print(complemento(G))
GC=(complemento(G))


gc = nx.Graph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(GC):
    for vicino in vicini:
        gc.add_edge(i, vicino)
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(gc,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()