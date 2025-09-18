#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:38:23 2024

@author: mirko
"""

"""Progetta algoritmo che ha input n e stampa tutte le matrici binarie nxn  """
def matrbin(n,sol,i=0,j=0):
  if i==n:
        print(sol)
        return
    
  sol[i][j]=0
  if j<n-1 :matrbin(n,sol,i,j+1)
  else:     matrbin(n,sol,i+1,0)
            
  sol[i][j]=1   
  if j<n-1 :  matrbin(n,sol,i,j+1) 
  else :      matrbin(n,sol,i+1,0)
    
n=2
sol=[ [0]*n for _ in range(n)]
matrbin(n,sol)

print("===================================================================\n")


"""Progetta algoritmo che ha input n e stampa tutte le matrici binarie nxn
tali che righe e colonne sono non decrescenti  """

    
def matrbin_cres(n,sol,i=0,j=0):
  if i==n:
        print(sol)
        return
    
  if  (j==0 or sol[i][j-1]==0 ) and (i==0 or sol[i-1][j]==0 ):
    sol[i][j]=0
    if j<n-1 :matrbin_cres(n,sol,i,j+1)
    else:     matrbin_cres(n,sol,i+1,0)
            
  sol[i][j]=1   
  if j<n-1 :  matrbin_cres(n,sol,i,j+1) 
  else :      matrbin_cres(n,sol,i+1,0)
    
n=2
sol=[ [0]*n for _ in range(n)]
matrbin_cres(n,sol)

print("===================================================================\n")


"""Progetta algoritmo che stampa tutte le matrici binarie nxn tali che 
non abbiano uni:1 adiacenti su stessa riga , colonna e diagonale """

def mb(n):
    sol=[ [-1]*n for _ in range(n)]
    matrbinadj(n,sol)
    
    
def matrbinadj(n,sol,i=0,j=0):
    if i==n:
        print(sol)
        return
    
    sol[i][j]=0
    if j<n-1:
            matrbinadj(n,sol,i,j+1)
    else : 
            matrbinadj(n,sol,i+1,0)
            
    #controlli su riga colonna diagoniali        
    if (j==0 or sol[i][j-1] != 1) and\
       (i==0 or sol[i-1][j]!=1 ) and\
       (i==0 or j==0 or  sol[i-1][j-1]!=1) and\
       (i==0 or j==n-1 or sol[i-1][j+1]!=1):   
        
      sol[i][j]=1    
      if j<n-1:
            matrbinadj(n,sol,i,j+1)
      else : 
            matrbinadj(n,sol,i+1,0)
    
        
print(mb(2))
print("===================================================================\n")


"""Progetta algoritmo che ha input n e stampa tutte le matrici binarie nxn
tali che righe contengono tutti simboli uguali tra l'alfabeto (a,b,c)  """


def matugual(sol,n,i=0,j=0):
    if i==n:
        print(sol)
        return
    
    if (j==0 or sol[i][j-1] =="a") :
        sol[i][j]="a"
        if j<n-1: 
           matugual(sol, n, i,j+1)
        else:  matugual(sol, n, i+1,0)
    
    if (j==0 or sol[i][j-1] =="b") :
        sol[i][j]="b"
        if j<n-1: matugual(sol, n, i,j+1)
        else:  matugual(sol, n, i+1,0)
    
    if (j==0 or sol[i][j-1] =="c") :
        sol[i][j]="c"
        if j<n-1: matugual(sol, n, i,j+1)
        else:  matugual(sol, n, i+1,0)
    
    
n=2
sol=[[0]*n for _ in range(n)]
matugual(sol, n)

print("=================================================================\n")

"""Progetta algoritmo che ha input n e alfabeto s stampa tutte le matrici 
 nxn tali che righe contengono tutti simboli uguali tra l'alfabeto di s """


def matugualk(s, sol, n, i=0, j=0):
    if i == n:
        print(sol)
        return
    
    for char in s:
        if j == 0 or sol[i][j-1] == char:
            sol[i][j] = char
            if j < n-1:
                matugualk(s, sol, n, i, j+1)
            else:
                matugualk(s, sol, n, i+1, 0)

n = 2
sol = [[0] * n for _ in range(n)]
matugualk("abc", sol, n)
print("=================================================================\n")


"""Progettare un algoritmo che prende in input n naturale e stampa tutte le 
permutazioni su n , N! ad es n=4 n!=24   """

def perm(sol,n,p):
    if len(sol)==n:
        print(sol)
        return
    
    for i in range(n):
     if p[i]==0:
        sol.append(i)
        p[i]=1
        perm(sol,n,p)
        sol.pop()
        p[i]=0
        
perm([],3,[0]*3)


print("=================================================================\n")


"""Progettare un algoritmo che prende in input n naturale e stampa tutte le 
permutazioni su n , N! ad es n=4 n!=24  tali che nelle posizioni pari 
ci siano numeri pari """

def perm2(sol,n,p):
    if len(sol)==n:
        print(sol)
        return
    
    for i in range(n):
     if p[i]==0  and i%2 == len(sol)%2:
        sol.append(i)
        p[i]=1
        perm2(sol,n,p)
        sol.pop()
        p[i]=0

n=5
perm2([],n,[0]*n)


print("=================================================================\n")


"""Progettare un algoritmo che prende in input n naturale e stampa tutte le 
permutazioni su n , tali che non ci siano pari o dispari consecutivi   """

def perm3(sol, n, p):
    if len(sol) == n:
        print(sol)
        return
    
    for i in range(n):
        if p[i] == 0 and (len(sol) == 0 or (sol[-1] % 2 != i % 2)):
            sol.append(i)
            p[i] = 1
            perm3(sol, n, p)
            sol.pop()
            p[i] = 0

perm3([], 4, [0] * 4)

print("=================================================================\n")


"""Dare lo pseudocodice di un algoritmo che, dati n e k , con
k ≤ n, stampa tutte le permutazioni dei primi n interi in cui
compaiono almeno k punti fissi.
Per una permutazione un punto fisso è un elemento i che
compare nella posizione i della permutazione. Ad esempio
per n=5 la permutazione 2,1,4,3,0 contiene due punti fissi (1
e 3). 
Ad esempio per n = 4 e k = 2 il programma deve stampare le
seguenti 7 permutazioni:
0123, 0132, 0213, 0321, 1023, 2103, 3120
La complessità dell’algoritmo deve essere O(n^2 *S(n))
dove S(n) sono le permutazioni da stampare."""


def perm4(sol, n, p, k, fissi):
    if len(sol) == n:
        print(sol)
        return
    for i in range(n):
        fix = (i == len(sol))
        
        if p[i] == 0 and (n-len(sol)+fissi+fix > k):
            sol.append(i)
            p[i] = 1
            perm4(sol, n, p, k, fissi + fix)
            sol.pop()
            p[i] = 0
n=4
k=2
perm4([], n, [0] * n, k, 0)


print("=================================================================\n")
