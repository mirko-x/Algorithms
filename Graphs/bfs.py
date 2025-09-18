   #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 05:34:11 2024

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



def bfs(x,G):
    #O(n)*O(n+m) = O(n^2)
    vis=[0]*len(G)
    vis[x]=1
    coda=[x]
    while coda:
        u=coda.pop(0)
        for y in G[u]:
            if not vis[y]:
                vis[y]=1
                coda.append(y)
    return vis

print(bfs(0,G))

def bfsottimo(x,G):
    #O(n+m)
    vis=[0]*len(G)
    vis[x]=1
    coda=[x]
    i=0
    while len(coda)>i:
        u=coda[i]
        i+=1
        for y in G[u]:
            if not vis[y]:
                vis[y]=1
                coda.append(y)
    return vis

print(bfsottimo(0,G))


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
    
print(dist(0,G))


"""Descrivere un algoritmo che, dato un grafo G non diretto e connesso e
due suoi nodi u e v, in tempo O(n + m) trova i nodi che hanno la stessa
distanza da u e la stessa da  v."""

G=[[1,2,3],[0],[0],[0]]

g = nx.Graph()

# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    for vicino in vicini:
        g.add_edge(i, vicino)
        
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()
def ugualdist(u, v, G):
    # Calcola le distanze di tutti i nodi da u e v
    du = dist(u, G)
    dv = dist(v, G)
    print(du,dv)
    # Trova i nodi con la stessa distanza da u e v
    result = []
    for i in range(len(G)):
        if du[i] == dv[i]  :  # Se la distanza da u e v è la stessa
            result.append(i)
    
    return result


print(ugualdist(1,2,G))


"""Descrivere un algoritmo che, dato un grafo G non diretto e connesso e
due suoi nodi u e v, in tempo O(n + m) trova i nodi che hanno la stessa
distanza di {u,v} = k per u,v ."""

G=[[1,2,3],[0],[0],[0]]

g = nx.Graph()

# Aggiunta degli archi al grafo
for i, vicini in enumerate(G):
    for vicino in vicini:
        g.add_edge(i, vicino)
        
pos = nx.spring_layout(g, k=1, seed=42)
# Disegno del grafo
nx.draw(g,pos,edge_color="red", with_labels=True, node_color='yellow', node_size=500, font_size=20, font_color='black', arrows=True)
plt.show()
def ugualdistk(u, v, G):
    # Calcola le distanze di tutti i nodi da u e v
    du = dist(u, G)
    dv = dist(v, G)
    print(du[v],dv[u])
    # Trova i nodi con la stessa distanza da u e v
    result = []
    for i in range(len(G)):
        if du[i] == dv[i] == du[v] ==dv[u]  :  # Se la distanza da u e v è la stessa
            result.append(i)
    
    return result


print(ugualdistk(1,2,G))



