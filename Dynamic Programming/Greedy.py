#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
"""
Created on Thu Aug 15 02:49:11 2024

@author: mirko
Abbiamo due liste di interi A e B ciascuna
con 2 ⋅ n elementi. Dobbiamo selezionare n elementi
dalla lista A ed n elementi dalla lista B in modo che
la somma dei 2 ⋅ n elementi selezionati sia massima.
Non è possibile selezionare elementi che nelle due
liste occupino la stessa posizione.
"""
A = [10, 2, 4, 6, 1, 7, 3, 4]
B = [6,  6, 1, 0, 3, 8, 5, 7]

def scelta(A, B) :
  n=len(A)
  sol=[]
  ls=[(A[i]-B[i],i) for i in range(n)]
  ls.sort(reverse=True)
  for i in range((n//2)):
      sol.append(A[ls[i][1]])
      
  for i in range((n//2),n):
      sol.append(B[ls[i][1]])
      
  return sol,sum(sol)
      

print(scelta(A, B))


D=[5,6,3,5,4,7,3]
def file(D,k):
    lista=[(D[i],i) for i in range(len(D))]
    ls=sorted(lista,key=lambda x: x[0])
    space=0
    sol=[]
    som=[]
    for d,i in ls:
        if space+d<=k:
            sol.append(i)
            som.append(d)
            space+=d
        else:
            return sol,som,sum(som)
        
print(file(D,11))


"""abbiamo una lista con le posizioni p0 < p2 < … < pn−1 in cui si
trovano n case lungo una strada rettilinea. Lungo la strada bisogna posizionare
dei cassonetti e si vuole che ciascuna casa abbia almeno un cassonetto ad una
distanza che non superi k.
Ad esempio:
se lista = [2, 5, 7, 11, 14, 16, 18] e k = 3 la soluzione ottima richiede 
3 cassonetti,una possibile dislocazione è [4, 11, 15]"""

def posiziona_cassonetti(case, k):
    n = len(case)
    i = 0
    cassonetti = []
    
    while i < n:
        # Trova il primo punto dove potrebbe andare un cassonetto per coprire la casa corrente
        start = case[i]
        i += 1
        
        # Trova il punto più lontano in cui può essere messo un cassonetto che copra start
        while i < n and case[i] <= start + k:
            i += 1
        
        # Posiziona il cassonetto nella posizione più lontana possibile
        pos = case[i - 1]
        cassonetti.append(pos)
        
        # Salta tutte le case che questo cassonetto può coprire
        while i < n and case[i] <= pos + k:
            i += 1
            
    return cassonetti

case = [2, 5, 7, 11, 14, 16, 18]
k = 3
print(posiziona_cassonetti(case, k))




"""Dato un grafo non diretto G un sottoinsieme dei suoi nodi è detto
indipendente se non contiene vertici adiacenti.
Progettare un algoritmo greedy che, dato un grafo connesso e aciclico T
restituisce un suo insieme indipendente di dimensione massima per T .
T  dunque è sconnesso e ogni componente ha 1 nodo
. """
    
def dominante(G):
  # O(n+m)+O(nlogn)
  G2=[(G[i]) for i in range(len(G))]
  G2=sorted(G2,key=lambda x: len(x))
  T=[]
  vis = [0] * len(G2)
  for nodo in range(len(G2)):
    if not vis[nodo]:
        T.append(nodo)
        vis[nodo] = 1
        for vicino in G[nodo]:
            vis[vicino] = 1
  return T

G = [[4], [2], [8, 1, 4], [5], [2, 9, 0], [8, 7, 6, 3], [5], [5], [2], [4]]
print("Insieme dominante massimo:",dominante(G))



"""Hai due vettori di interi A e B entrambi di lunghezza n. Con un’operazione
puoi scegliere una posizione i, 0 <= i < n, e scambiare il contenuto di A[i]
con quello di B[i].
Progettare un algoritmo greedy che dati i vettori A , B ed un intero k <= n
in tempo O(n log n) determina il massimo valore che si può ottenere dalla
somma degli elementi di A dopo al più k operazioni
"""

def maxA(A,B,k):
    #Banalmente O(nlogn)
    #se tutti  i val di A > B banlmente return A
    C=[(B[i]-A[i],i) for i in range(len(A))]
    C.sort(reverse=True)
    for i in range(k):
        if A[C[i][1]]<B[C[i][1]]:
            A[C[i][1]]=B[C[i][1]]
        
    return A,sum(A)
    
        
A=[2,5,6,1,0,0]
B=[5,1,7,2,4,9]
print(maxA(A, B, 3))






