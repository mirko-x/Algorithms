#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 03:50:57 2024

@author: mirko
"""

import networkx as nx
import matplotlib.pyplot as plt


"""Dato un grafo connesso e aciclico G vogliamo trovare in tempo O(n) il suo
diametro (vale a dire la lunghezza del cammino più lungo tra due nodi di
G).
• Prova la correttezza del seguente algoritmo basato su due visite BFS
(o produci un controesempio)
(a) effettua una visita BFS a partire dal nodo 0 alla ricerca del nodo
x più lontano
(b) effettua una visita BFS a partire dal nodo x alla ricerca del nodo
y più lontano
(c) restituisci come diametro la distanza del nodo x dal nodo y."""


G = [[1, 2,6], [0, 3, 4], [0,5], [1], [1],[2],[0]]
g = nx.Graph()
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
def dist(x,G):
    d=[-1]*len(G)
    d[x]=0
    coda=[x]
    i=0
    while len(coda)>i:
        u=coda[i]
        i+=1
        for y in G[u]:
            if d[y]==-1:
                d[y]=d[u]+1
                coda.append(y)
    return d

def diam(G):
    """L'algoritmo si basa sul fatto che il diametro di un albero è il cammino più 
    lungo tra due foglie dell'albero. 
    Distanza Massima da un Nodo Arbitrario:
    La prima visita BFS dal nodo 0 trova il nodo più lontano x. 
    Questo nodo x è garantito essere su uno degli estremi del diametro dell'albero.
    Distanza Massima dal Nodo Estremo:
    La seconda visita BFS a partire da x trova il nodo più lontano y da x. 
    La distanza tra x e y rappresenta il diametro dell'albero perché qualsiasi 
    altro percorso lungo l'albero non sarà più lungo di questo."""
    
    D=(dist(0,G))
    print(max(D))
    x = D.index(max(D))
    D2 = dist(x, G)
    return max(D2)
    
    
print(diam(G))

