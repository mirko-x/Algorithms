#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 08:55:21 2024

@author: mirko
"""
import networkx as nx
import matplotlib.pyplot as plt
from math import inf 
from heapq import heappop,heappush

G = [
    [(1, 3), (2, 1),(3,3)],
    [(2, 7),(3,9)],
    [(3, 2)],
    []
]
g = nx.DiGraph()

# Aggiungere i nodi e gli archi con i pesi
for i, edges in enumerate(G):
    for edge in edges:
        g.add_edge(i, edge[0], weight=edge[1])

# Posizioni dei nodi per il layout
pos = nx.spring_layout(g)

# Disegnare il grafo
nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', edge_color='gray', arrowsize=20)

# Disegnare le etichette dei pesi sugli archi
edge_labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels,font_color="red" ,font_size=15)

# Visualizzare il grafico

plt.show()


"""• heappop(h): estrae e restituisce il minimo dall’heap h in tempo O(log(len(h)))
   • heappush(h, x): inserisce l’elemento x nell’heap h in tempo O(log(len(h)))"""
   
def dijkstra(s,dest,G):
    """O(n log n) + O(m log n) + O(m log n) = O((n + m) log n).
    è da preferirsi nel caso di grafi sparsi, presentando in quel
    caso una complessità O(n log n) mentre andrebbe evitata nel caso di
    grafi densi dove la complessità risultante sarebbe O(n^2 log n)"""
    H=[]
    P=[-1]*len(G)
    D=[inf]*len(G)
    P[s],D[s]=s,0
    C=[]
    for y,costo in G[s]:
        heappush(H, (costo,s,y))
    while H:  
        costo,padre,x =heappop(H)
        if P[x]==-1:
           P[x]=padre
           D[x]=costo
           for y,costo in G[x]:
               heappush(H,(D[x]+costo,x,y))
               
               
        
    # Ricostruisci il cammino minimo da s a dest
    if D[dest]==inf :
        return D,inf,P
    
    while dest != s:
         C.append(dest)
         dest = P[dest]
        
    C.append(s)
    C.reverse()  # Il cammino viene ricostruito all'inverso
    
    """ NOTA:
        costo +1 per ogni arco se si vuole cammino super minimo C con meno archi
        costo -1 per ogni arco se si vuole cammino minimo di max archi  """ 
    return D,C,P

print(dijkstra(1,0, G))
           
    
    
    
    
    
    
    
    
    
    
    
    