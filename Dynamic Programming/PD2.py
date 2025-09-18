#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:43:10 2024

@author: mirko
"""

"""Dato un array A di n ≥ 2 interi positivi vogliamo calcolare la somma
massima per una sottosequenza di elementi di A con elementi che distano
almeno 2 in A.
L’algoritmo deve avere complessità O(n)"""


def max_sum_subsequence(A):
    n = len(A)
    dp = [0] * n
    dp[0] = A[0]
    dp[1] = max(A[0], A[1])
    dp[2]=max (A[0], A[1],A[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-1], A[i] + dp[i-3])
    
    return dp[n-1]

A = [1, 10, 3, 2, 4, 1, 7]
print(max_sum_subsequence(A))  

"""Data una sequenza S di elementi una sottosequenza di S si ottiene
eliminando zero o più elementi da S (Nota: non necessariamente le
eliminazioni devono avvenire in testa o in coda alla sequenza) ritorna la 
max lunghezza di sottosequenze crescenti
"""

def max_len_subsequence(A):
    n=len(A)
    T=[1]*n
    for i in range(1,n):
        for j in range(i):
            if A[i]>A[j]:
              T[i]=max(T[i],T[j]+1)
              
    return(max(T),T)


A = [9, 3, 2, 4, 1, 5, 8, 6, 7, 2]
print(max_len_subsequence(A))

"""Data una sequenza S di elementi una sottosequenza di S si ottiene
eliminando zero o più elementi da S (Nota: non necessariamente le
eliminazioni devono avvenire in testa o in coda alla sequenza) ritorna il
numero di sottosequenze crescenti
"""
def conta_increasing_subsequences(A):
    n = len(A)
    dp = [1] * n 
    
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] += dp[j]
    
    return sum(dp)


A = [9, 3, 2, 4, 1, 5, 8, 6, 7, 2]
print(conta_increasing_subsequences(A)) 

"""Dato un intero n vogliamo sapere quante sono le sequenze di
cifre decimali non decrescenti lunghe n."""
def len_decimal(n):
    T=[[0]*10 for _ in range(n+1)]
    for j in range(10):
        T[1][j]=1
    for i in range(2,n+1):
        for j in range(10):
            for k in range(j+1):
                T[i][j]+=T[i-1][k]
         
    return T,sum(T[n])

print(len_decimal(4))

"""Progettare un algoritmo che, dato l’intero positivo n , in tempo O(n) conta il
numero di stringhe ternarie(0,1,2) lunghe n , t.c le cifre adiacenti presenti 
nella stringa differiscono al più di 1 , (ad ex 02 e 20  no!) 
"""

def ternoadj(n):
    T=[[0]*3 for _ in range(n+1)]
    for j in range(3):
        T[1][j]=1
    for i in range(2,n+1):
           T[i][0]=T[i-1][0]+T[i-1][1]
           T[i][1]=T[i-1][0]+T[i-1][1]+T[i-1][2]
           T[i][2]=T[i-1][1]+T[i-1][2]
           
    return T,sum(T[n])


print(ternoadj(3))


"""Progettare un algoritmo che, dato l’intero positivo n , in tempo O(n) conta il
numero di stringhe k-arie lunghe n  (k<=n) t.c le cifre adiacenti presenti 
nella stringa differiscono al più di 1 , (ad ex 02 e 20  no!) 
"""

def narioadj(n,k):
    dp=[[0]*k for _ in range(n+1)]
    for j in range(k):
        dp[1][j]=1
    for i in range(2, n + 1):
        for j in range(k):
            dp[i][j] = dp[i-1][j]  # Casella centrale
            if j > 0:
                dp[i][j] += dp[i-1][j-1]  # Casella a sinistra
            if j < k - 1:
                dp[i][j] += dp[i-1][j+1]  # Casella a destra
           
           
    return dp,sum(dp[n])


print(narioadj(3,4))



"""Progettare un algoritmo che, dato un intero n ,restituisce il
numero di stringhe lunghe n che è possibile ottenere con i 4 simboli 
0, 1, 2 e 3 facendo in modo che nelle stringhe non compaiano mai 
due cifre dispari adiacenti """

def dispadj(n):
    T=[[0]*4 for _ in range(n+1)]
    for j in range(4):
        T[1][j]=1
    for i in range(2,n+1):
           T[i][0]=sum(T[i-1])
           T[i][1]=T[i-1][0]+T[i-1][2]
           T[i][2]=T[i][0]
           T[i][3]=T[i][1]
    return T,sum(T[n])


print(dispadj(4))


"""Progettare un algoritmo che, dato un intero n ,restituisce il
numero di stringhe lunghe n che è possibile ottenere con k simboli 
0,1...n (3<=k<=n) facendo in modo che nelle stringhe non compaiano mai 
due cifre dispari adiacenti """

def dispadjg(n,k):
    T=[[0]*k for _ in range(n+1)]
    for j in range(k):
        T[1][j]=1
    for i in range(2,n+1):
        for j in range(k):
           if j%2:
               T[i][j]=T[i-1][j-1]*2
               
           else: T[i][j]=sum(T[i-1])
               
    return T,sum(T[n])


print(dispadjg(4,3))