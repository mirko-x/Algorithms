#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 05:53:17 2024

@author: mirko
"""
"""Il problema dello zaino: Abbiamo uno zaino di capacità c ed n oggetti,
ognuno con un peso pi e un valore vi.
Vogliamo sapere il valore massimo che si può inserire nello zaino tc 
la somma dei pesi degli oggetti inseriti sia <= capacita
"""

def zaino(P,V,c):
    n=len(P)
    T=[[0]*(c+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            if j<P[i-1]:
                T[i][j]=T[i-1][j]
            else: 
                T[i][j]=max(T[i-1][j],V[i-1]+T[i-1][j-P[i-1]])
                
    return T,T[n][c]
    
V=[1,6,18,22,28]
P=[1,4 ,5, 5, 7]                
print(zaino(P,V,10))           

"""Abbiamo una matrice quadrata binaria M di dimensione
n × n e vogliamo sapere qual è la dimensione massima per
le sottomatrici quadrate di soli uni contenute in M"""

def matsqrt(M):
    n=len(M)
    T=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j]==0:
                T[i][j]=0
            else: 
                T[i][j]=min(T[i][j-1],T[i-1][j-1],T[i-1][j])+1
    m=0
    for i in range(n):
        m=max(m,max(T[i]))
        
    return m,T

M=[[1,0,1,0],
   [0,1,1,1],
   [1,1,1,1],
   [0,1,1,1]]
print(matsqrt(M))


"""Il problema del resto: Ho n diversi tagli di banconote ed un resto c da
dare. Voglio sapere quanti modi ci sono di produrre il resto c se ho
quantità illimitata di banconote dei vari tagli."""

def tagli(A,c):
    n=len(A)
    T=[[0]*(c+1) for _ in range(n+1)]
   
    for i in range (n+1):
            T[i][0]=1
            
    for i in range(1,n+1):
        for j in range(1,c+1):
            if j<A[i-1]:
                T[i][j]=T[i-1][j]
            else: 
                T[i][j]=T[i-1][j]+T[i][j-A[i-1]]
                
    return T[n][c]
    
A=[1,2,3]              
print(tagli(A,5)) 


"""Una transazione è l’acquisto di un oggetto seguito dalla sua vendita (che
non può ovviamente avvenire prima del giorno dell’acquisto).
Disponiamo di un vettore A di interi dove A[i] è la quotazione dell'oggetto
nel giorno i.
Dato il vettore A con le quotazione dei prossimi n giorni e dovendo eseguire
una singola transazione vogliamo sapere qual è il guadagno massimo cui
possiamo aspirare.
nota che se il vettore è decrescente il guadagno massimo è 0."""


def transazione(A):
    n=len(A)
    T=[0]*n
    B=[0]*n
    B[0]=A[0]
    for i in range(1,n):
        B[i]=min(A[i],B[i-1])
        
    for i in range(1,n):
            T[i]=A[i]-B[i]   
            
    return T,max(T)
        
        

A = [7, 9, 5, 6, 3, 22]
print(transazione(A))
"""data una matrice M binaria n × n vogliamo verificare se nella matrice
è possibile raggiungere la cella in basso a destra partendo da quella in alto a
sinistra senza mai toccare celle che contengono il numero 0. Si può assumere che
M[0][0] = 1.
Si tenga conto che ad ogni passo ci si può spostare solo di un passo verso destra
o un passo verso il basso."""

def camminomat(M):
    n = len(M)
    T = [[0] * n for _ in range(n)] 
    T[0][0] = M[0][0]
    
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                if i == 0 and j > 0:  #riga 0
                    T[i][j] = T[i][j-1]
                elif j == 0 and i > 0: # colonna 0
                    T[i][j] = T[i-1][j]
                elif i > 0 and j > 0: 
                    T[i][j] = T[i-1][j] or T[i][j-1]
    
    return T,T[n-1][n-1]

# Esempio d'uso
M = [
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1]
]

print(camminomat(M))  # Output: True (c'è un cammino possibile)

       

"""dato un intero positivo k ed una matrice M con interi
positivi di dimensione n × n contare i cammini di costo k che in M
partono dalle cella in alto a sinistra e raggiungono la cella in basso a
destra.
Si tenga conto che ad ogni passo ci si può spostare solo di un passo
verso destra o un  verso il basso e che il costo di un cammino è
dato dalla somma dei valori delle celle toccate.
Ad esempio per la matrice A di seguito a sinistra con k = 12 la
risposta è 2. un algoritmo che in tempo Θ(n^2*k) risolve il problema.
"""

def cammini_di_costo_k(M, k):
    n = len(M)
    
    # Tabella dp di dimensioni (n x n x (k+1))
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    # Caso base: il cammino che parte dalla cella (0, 0)
    dp[0][0][M[0][0]] = 1
    
    # Riempimento della tabella dp
    for i in range(n):
        for j in range(n):
            for cost in range(k + 1):
                if dp[i][j][cost] > 0:
                    # Movimento verso il basso
                    if i + 1 < n:
                        new_cost = cost + M[i + 1][j]
                        if new_cost <= k:
                            dp[i + 1][j][new_cost] += dp[i][j][cost]
                    
                    # Movimento verso destra
                    if j + 1 < n:
                        new_cost = cost + M[i][j + 1]
                        if new_cost <= k:
                            dp[i][j + 1][new_cost] += dp[i][j][cost]
    
    # La risposta è il numero di cammini che raggiungono (n-1, n-1) con costo esattamente k
    return dp, dp[n-1][n-1][k]

# Esempio d'uso
M = [
    [1, 2, 3],
    [4, 6, 5],
    [3, 2, 1]
]
k = 12
print(cammini_di_costo_k(M, k))  # Output: 2
