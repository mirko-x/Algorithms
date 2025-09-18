#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:02:11 2024

@author: mirko
"""

import networkx as nx
import matplotlib.pyplot as plt

"""Ideare un algoritmo che dato un grafo G parzialmente orientato senza cicli
orientati ne orienta gli archi producendo un DAG. L’algoritmo deve avere
complessità O(n + m).
Progettare la funzione python che codifica l’algoritmo per orientare il grafo
G parzialmente orientato. Il grafo G è rappresentato tramite liste di adi-
acenza dove ad ogni nodo x, 0 <= x < n è associata una coppia di liste
(A, B).
• La lista A contiene i vicini di x raggiungibili tramite gli archi diretti
• La lista B contiene i vicini di x raggiungibili tramite gli archi non
diretti."""

#G=[[1],[0,3,2],[1,3],[1,2],]

G=[([ ]+[2,3] ),
   ([0,3]+[2]),
   ([]+[0,1,4]),
   ([2]+[0]),
   ([]+[2])]
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


def orienta(G):
 G2 = [[] for _ in G]
 for u in range(len(G)):
  for v in G[u]:
     if u <= v:
       G2[u].append(v)
 return G2

print(G)

C=orienta(G)

g = nx.DiGraph()
# Aggiunta degli archi al grafo
for i, vicini in enumerate(C):
    if  not vicini :  # Nodo isolato
        g.add_node(i)
    else :
        for vicino in vicini:
         g.add_edge(i, vicino)
         
pos = nx.spring_layout(g, k=1, seed=50)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()

print(orienta(G))



"""Progettare un algoritmo che, dato un grafo diretto G, restituisce in tempo
O(n + m) una tripla di interi con nell’ordine: il numero di archi in avanti,
il numero di archi all’indietro ed il numero di archi di attraversamento che
si incontrano durante una sua visita a partire dal nodo 0."""

def typedge(v, G, visit, forward, backward, cross):
    visit[v] = 1  # Il nodo è ora in corso di visita (visiting)
    for u in G[v]:
        if visit[u] == 0:  # Nodo non visitato
            forward += 1  # Arco in avanti
            typedge(u, G, visit, forward, backward, cross)
        elif visit[u] == 1:  # Nodo già visitato ma ancora in corso di esplorazione
            backward += 1  # Arco all'indietro
        elif visit[u] == 2:  # Nodo già completamente visitato
            cross += 1  # Arco di attraversamento
    visit[v] = 2  # Il nodo è completamente visitato
    return forward, backward, cross

visit = [0] * len(G)  # 0: non visitato, 1: in corso di visita, 2: visitato
forward = 0
backward = 0
cross = 0
    
print(typedge(0, G, visit, forward, backward, cross))
    
    


