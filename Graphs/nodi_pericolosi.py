#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:51:28 2024

@author: mirko
"""
import networkx as nx
import matplotlib.pyplot as plt

"""Abbiamo un grafo connesso G di n nodi, i nodi sono di due tipi: ”pericolosi”
o meno. Un vettore binario P di n componenti permette di individuare i nodi
pericolosi (P [i] = 1 se e solo se i è pericoloso).

• Progettare un algoritmo che, dato G, un suo nodo s ed il vettore P ,
restituisce in tempo O(n + m) una lista con tutti i nodi irragiungibili da
i senza dover passare per nodi pericolosi.


"""


# Definizione del grafo G e della lista Per
G = [
    [1, 2, 9],     # Nodo 0
    [0, 4, 5],     # Nodo 1
    [0, 5, 6],     # Nodo 2
    [8, 7,10],     # Nodo 3
    [1, 8],        # Nodo 4
    [1, 2, 8],     # Nodo 5
    [2, 9],        # Nodo 6
    [3, 9],        # Nodo 7
    [4, 5, 9,3],   # Nodo 8
    [6, 7, 8,0],   # Nodo 9
    [3]            # Nodo 10 
                   # Nodo 11
]

Per = [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0,0]


# Creazione del grafo
g = nx.Graph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    for vicino in vicini:
        g.add_edge(i, vicino)
# Creazione di una mappatura nodo-colore
node_colors = {i: 'red' if Per[i] == 1 else 'green' for i in range(len(G))}
# Applicazione dei colori ai nodi nel grafo
color_map = [node_colors[node] for node in g.nodes()]
# Poszionamento dei nodi
pos = nx.spring_layout(g, k=1, seed=100)
# Disegno del grafo con i colori specificati
nx.draw(g, pos, edge_color="black", with_labels=True, node_color=color_map, node_size=500, font_size=20, font_color='black')
plt.show()



def dfsper(s,P,G,vis):
    vis[s]=1
    for v in G[s]:
         if (not vis[v]) and P[v]==0 :
             dfsper(v, P, G, vis)
             
    return vis


def dfs(s,G,vis):
    vis[s]=1
    for v in G[s]:
         if not vis[v] :
             dfs(v, G, vis)
             
    return vis
        
def nodiper(s,G,P):
    if P[s]==1:
        return False
    vis=dfs(s,G,[0]*len(G))
    vis2=dfsper(s,P,G,[0]*len(G))
    irrnorm=[]
    irrper=[]
    for i in range(len(G)):
        if vis2[i]==0 and vis[i]==1:
              irrper.append(i)
        elif vis[i]==0:
             irrnorm.append(i)
    return irrnorm,irrper        


print(nodiper(0,G,Per))            


print("============================================================")

"""
Abbiamo un grafo connesso G di n nodi, i nodi sono di due tipi: ”pericolosi”
o meno. Un vettore binario P di n componenti permette di individuare i nodi
pericolosi (P [i] = 1 se e solo se i è pericoloso).
Progettare un algoritmo che, dato G, un suo nodo s ed il vettore P , genera
in tempo O(n + m) un albero dei cammini radicato in s di costo minimo
di G dove il costo di un cammino è dato dal numero di nodi pericolosi
toccati lungo il cammino.

"""
 K = [[(n, Per[n]) for n in l] for l in G]
def dijkstra(s,G):
    
    Calcolato = [0 for _ in range(len(G))]
    from math import inf
    Lista = [(inf, -1) for _ in range(len(G))]
    Lista[s], Calcolato[s] = (0, s), 1
    for y, costo in G[s]:
        Lista[y] = (costo, s)
    while True:
        minimo, x = inf, -1
        for i in range(len(Lista)):
            if Calcolato[i] == 0 and Lista[i][0] < minimo:
                minimo, x = Lista[i][0], i
        if minimo == inf:
            break
        Calcolato[x] = 1
        for y, costo in G[x]:
            if Calcolato[y] == 0 and minimo + costo < Lista[y][0]:
                Lista[y] = (minimo + costo, x)
    D = [costo for costo, _ in Lista]
    P = [padre for _, padre in Lista]
    return D, P


print(dijkstra(0,K)[0])
