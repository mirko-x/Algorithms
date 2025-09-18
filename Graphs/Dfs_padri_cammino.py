#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:41:33 2024
@author: mirko
"""
import networkx as nx
import matplotlib.pyplot as plt

M=[[0,1,0,0,0,0,0,0],
   [0,0,1,1,0,1,0,0],
   [0,0,0,0,1,0,0,0],
   [0,0,0,0,0,1,0,0],
   [0,0,0,0,0,0,1,0],
   [0,0,0,0,0,0,0,0],
   [0,0,1,0,0,0,0,0],
   [1,0,0,0,0,0,0,0]]

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



def dfs(v,M,visit):
    #Matrice di adiacenza O(n^2)
    visit[v]=1
    for i in range(len(M)):
        if  M[v][i] and not visit[i]:
            dfs(i,M,visit)
    return visit   
    

def dfs2(v,G,visit):
    #Liste di adiacenza O(n)
    visit[v]=1
    for i in G[v]:
        if not visit[i]:
            dfs2(i,G,visit)
    return visit    


def Padri(v,G,P):
    #lista  padri di un nodo O(n)
    if P[v]==-1: P[v]=v
    for y in G[v]:
        if P[y]==-1:
            P[y]=v
            Padri(y, G, P)
    return P


def Cammino(v,P):
    # percorso da nodo padre y a  nodo di destinazione v
    # Costo O(n) ma necessario vettore padri di un nodo 
    if P[v]==-1 : return []
    path=[]
    while P[v]!=v:
        path.append(v)
        v=P[v]
    path.append(v)
    path.reverse()
    return path

def CamminoRic(v,P):
     if P[v]== -1 : return []
     if P[v]== v  : return [v]
     return CamminoRic(P[v],P)+[v]
 
visit=[0]*len(G) # o len(G)
P=[-1]*(len(G))

v=0
print("dfs matr",v,dfs(v,M,visit))
print("dfs list",v,dfs2(v,G,visit))
v=0
print("Figli Padri",v,Padri(v,G,P))
v=6
print("Cammino",v,Cammino(v,P)) 
v=5
print("CamminoR",v,CamminoRic(v,P)) 




"""In un grafo aciclico T con n nodi gli archi sono stati orientati a caso. 
Vogliamo sapere in quali nodi radicare il grafo 
in modo tale che risulti minimo il numero di archi la cui
direzione va invertita per far si che tutti i nodi siano raggiungibili dalla radice.
Ad esempio in cui è riportato a sinistra il grafo aciclico T 
con gli archi orientati ed a destra si
mostra che radicandolo nel nodo 3 bisogna poi invertire 3 archi.
Progettare un algoritmo che prende come parametro l’albero orientato e in tempo O(n) risolve il
problema restituendo l’insieme di nodi da scegliere come radici.
"""
def nodiragg(G):
    maxx=[len(x)for x in (G)]
    k=max(maxx)
    R=[]
    for i in range(len(maxx)):
        if k==maxx[i]:
            j=i
            R.append(j)
    return R

print(nodiragg(G))

    
        
    


