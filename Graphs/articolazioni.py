#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 03:27:55 2024

@author: mirko
"""

"""Progettare un algoritmo che dato il grafo G restituisce la lista dei suoi
nodi di articolazione in tempo O(m)."""

G=[[1,5,6],[0,5],[3,4],[2,0],[2,6],[0,1],[0,4]]
g = nx.Graph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    if  not vicini :  # Nodo isolato
        g.add_node(i)
    else :
        for vicino in vicini:
         g.add_edge(i, vicino)
        
pos = nx.spring_layout(g, k=1, seed=60)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()



def art(G):
    "O(n*(n+m))."
    A = []
    for u in range(len(G)-1):
     G2 = [adj[:] for adj in G]
     for v in G2[u]:
         if u in G2[v]:
            G2[v].remove(u)  # Rimuove l'arco u-v
     G2[u] = []
     vis=(dfs(u+1,G2,[0]*(len(G))))
     if any(vis[i] == 0 and i != u for i in range(len(G))):
           A.append(u)

    return A

def dfs(v,G,visit):
    #Liste di adiacenza O(n)
    visit[v]=1
    for i in G[v]:
        if not visit[i]:
            dfs(i,G,visit)

    return visit

print(art(G))
