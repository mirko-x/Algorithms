#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 05:01:00 2024

@author: mirko
"""
import networkx as nx
import matplotlib.pyplot as plt
G=[[1],[2,3,5],[4],[5],[6],[],[2],[0]]
print(G)
g = nx.DiGraph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    for vicino in vicini:
        g.add_edge(i, vicino)
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()


def G_T(G):
    GT=[[] for _ in G ]
    for i in range (len(G)):
        for v in G[i]:
            GT[v].append(i)
    return GT


GT=G_T(G)
print(GT)

gt = nx.DiGraph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(GT):
    for vicino in vicini:
        gt.add_edge(i, vicino)
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(gt,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()