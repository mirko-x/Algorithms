#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 04:14:01 2024

@author: mirko
"""

"""Progettare un algoritmo che stampa stringhe binarie lunghe n"""
def bin_len_n(s,n,sol):
    if  len(s)==n:
        sol.append(s)
        return 
    for char in ["0", "1"]:
        bin_len_n(s+char,n,sol)
        
sol=[]
bin_len_n("",3,sol)    
print(sol,len(sol),"\n")

def bin_len_n2(n,sol):
    if  len(sol)==n:
        print(sol)
        return 
    
    sol.append("0")
    bin_len_n2(n,sol)
    sol.pop()
    
    sol.append("1")
    bin_len_n2(n,sol)
    sol.pop()
        
        
bin_len_n2(3,[])    
print("=================================================================\n")



"""Progettare un algoritmo che stampa stringhe binarie lunghe n tali che 
dato 0<=k<=n la stringa contiene al piu k "uni:1"
""" 
def bink(s, n, k, cont ,sol):
    if len(s) == n:
        sol.append(s)
        return
    for char in ["0", "1"]:
        if char=="1":
            cont+=1
        if cont <= k:
            bink(s + char, n, k, cont,sol)
sol=[]
bink("", 4, 2,0, sol)
print(sol,len(sol),"\n")


def bink2(n, k, cont ,sol):
    if  len(sol)==n:
        print(sol)
        return 
    
    for char in ["0", "1"]:
        if char=="1":
            cont+=1
        if cont<=k:   
          sol.append(char)
          bink2(n, k, cont,sol)
          sol.pop()
        
bink2(4,2,0,[])    
print("=================================================================\n")



"""Progettare un algoritmo che stampa stringhe binarie lunghe n tali che 
dato 0<=k<=n la stringa contiene esattamente k , "uni:1"
""" 
def binkesatto(s, n, k, cont,sol):
    if cont == k and len(s) == n:
        sol.append(s)
        return
    
    if (n-len(s))+cont < k:
        return
    
    binkesatto(s + "0", n, k, cont,sol)
    if cont < k:
        binkesatto(s + "1", n, k, cont + 1,sol)

sol=[]
binkesatto("", 4, 1, 0,sol)
print(sol,len(sol),"\n")

def binkesatto2(n, k, cont,sol):
    if cont == k and len(sol) == n:
        print(sol)
        return
    
    if (n-len(sol))+cont < k:
        return
    
    sol.append("0")
    binkesatto2( n, k, cont,sol)
    sol.pop()
    
    if cont < k:
        sol.append("1")
        binkesatto2( n, k, cont + 1,sol)
        sol.pop()


binkesatto2( 4, 1, 0,[])
print("=================================================================\n")


""" Sia T= ["0", "1", "2"] vogliamo stampare tutte le stringhe di dimensione n
tali che non abbiano 3 elementi uguali o diversi consecutivi"""

def consec(s, n,sol):
    # O(n*s(n) dove s sono tutte valide soluzioni  è ottimale)
    if len(s) == n:
        sol.append(s)
        return 
    for char in ["0", "1", "2"]:
        if len(s) >= 2:
            if s[-1] == s[-2] == char:
                continue  
            if s[-1] != s[-2] and s[-1] != char and s[-2] != char:
                continue 
        
        consec(s + char, n,sol)

sol=[]
consec("", 3,sol)
print(sol,len(sol),"\n")

def consec2(n,sol):
    # O(n*s(n) dove s sono tutte valide soluzioni  è ottimale)
    if len(sol) == n:
        print(sol)
        return 
    for char in ["0", "1", "2"]:
        if len(sol) >= 2:
            if sol[-1] == sol[-2] == char:
                continue  
            if sol[-1] != sol[-2] and sol[-1] != char and sol[-2] != char:
                continue 
            
            
        sol.append(char)
        consec2( n,sol)
        sol.pop()

consec2(3,[])
print("=================================================================\n")

"""Progettare un algoritmo che, dato un intero n, 
stampa tutte le stringhe lunghe n sull’alfabeto dei 3 simboli a, b e c, 
cui il numero delle b supera quello  degli altri due simboli.
L’algoritmo proposto deve avere complessità O(nD(n)) dove D(n) è il numero
di stringhe da stampare.
Ad esempio per n = 2 l’algoritmo deve stampare la sola stringa bb mentre per
n = 3 le stringhe da stampare sono le seguenti:
bbb, abb, bab, bba, cbb, bcb, bbc"""


def conta_b(s, n, count_ac,sol):
    
    if len(s) == n :
        sol.append(s)
        return
    
    if n-(n//2)>count_ac+1:
       conta_b(s + "a", n, count_ac + 1,sol)
       conta_b(s + "c", n, count_ac + 1,sol)
       
    conta_b(s + "b", n, count_ac,sol )

sol=[]
conta_b("", 4, 0,sol)
print(sol,len(sol),"\n")

def conta_b2(n, count_ac,sol):
    
    if len(sol) == n :
        print(sol)
        return
    
    if n-(n//2)>count_ac+1:
       sol.append("a")
       conta_b2(n, count_ac + 1,sol)
       sol.pop()
       sol.append("c")
       conta_b2( n, count_ac + 1,sol)
       sol.pop()
       
    sol.append("b")   
    conta_b2( n, count_ac,sol )
    sol.pop()
       

conta_b2( 4, 0,[])
print("=================================================================\n")

"""Data una sequenza S di elementi una sottosequenza di S si ottiene
eliminando zero o più elementi da S (Nota: le eliminazioni sono casuali )
stampa tutte le sottosequenze di elementi crescenti  """

def increasing_subsequences(s, i,A,sol):
    if i == len(A) :
        if s : sol.append(s)
        return 
    # Includere l'elemento corrente nella sottosequenza se cresce
    if not s or s[-1]< A[i]:
        increasing_subsequences(s+[A[i]],i+1 ,A,sol)
    
    # Non includere l'elemento corrente e passare al prossimo
    increasing_subsequences(s, i+1,A,sol)

# Esempio di utilizzo
A = [9, 3, 2, 4, 1]
sol=[]
increasing_subsequences([], 0 ,A,sol)
print(sol,len(sol),"\n")



def increasing_subsequences2(A,i,sol):
    if  i  == len(A) :
        print(sol)
        return 
    # Includere l'elemento corrente nella sottosequenza se cresce
    if not sol or sol[-1]< A[i]:
        sol.append(A[i])
        increasing_subsequences2(A,i+1,sol)
        sol.pop()
    
    increasing_subsequences2(A,i+1,sol)

# Esempio di utilizzo
A = [9, 3, 2, 4, 1]
increasing_subsequences2(A,0,[])

print("=================================================================\n")

"""Fissiamo n, k e T positivi con T <= nk Definiamo valida una sequenza di
lunghezza n contenente interi da 0 a k e la cui somma è T .
Ad esempio per n = 6, k = 4 e T = 12 allora la sequenza 132042 è valida
mentre 121213 non è valida. Bisogna esplorare solo i nodi che portano al 
risultato di somma T L'algoritmo deve avere complessità 
: O(S(n, k) · h · f (n) + S(n, k) · g(n)) == O(n*k*S(n,k))"""

def seq(s,n,k,T,tot):
    if len(s)==n:
        print(s,sum(s))
        return
    for i in range(k+1):
        if tot + i <= T and tot+i+(n-len(s)-1)*k >=T :
            seq(s+[i],n,k,T,tot+i)
           
seq([],3,3,6,0)
print("\n")


def seq2(sol,n,k,T,tot):
    if len(sol)==n:
        print(sol,sum(sol))
        return
    for i in range(k+1):
        if tot + i <= T and tot+i+(n-len(sol)-1)*k >=T :
            sol.append(i)
            seq2(sol,n,k,T,tot+i)
            sol.pop()
           
seq2([],3,3,6,0)
print("=================================================================\n")


"""Progettare un algoritmo che, data una stringa X lunga n sull’alfabeto n-ario.
stampa tutte le stringhe che è possibile ottenere da X
sostituendo il simbolo ′ *′ ad alcuni dei suoi caratteri in modo che i
caratteri rimanenti risultino in ordine strettamente crescente."""

def change(X,s,sol):
    if len(s) == len(X):
        sol.append(s)
        return
    
    change(X, s + '*' ,sol )
    
    if not s or s[-1] < X[len(s)]:
        change(X, s + X[len(s)],sol)
    
    

sol=[]
X = "0123"
change(X,"",sol)
print(sol,len(sol),"\n")


def change2(X,s,sol):
    if len(sol) == len(X):
        print(sol)
        return
    sol.append("*")
    change2(X,s,sol )
    sol.pop()
    if not s or X[len(sol)]>s : 
        sol.append((X[len(sol)]))
        change2(X,X[len(sol)-1],sol)
        sol.pop()
    

X = "0123"
change2(X,"",[])
print("=================================================================\n")


"""Progettare un algoritmo che, data una stringa X di lunghezza n, sull’alfabeto
dei 3 simboli 0, 1 e 2, stampa tutte le stringhe di lunghezza n sullo stesso alfa-
beto che differiscono da X in ciascuna posizione."""

def diffseq(s,X,n,sol):
    if len(s)==n:
        sol.append(s)
        return 
    
    if X[len(s)] == "0" :
      diffseq(s+"1",X,n,sol)
      diffseq(s+"2",X,n,sol)
      
    elif X[len(s)] == "1":
      diffseq(s+"0",X,n,sol)
      diffseq(s+"2",X,n,sol)
      
    elif X[len(s)] == "2" :
      diffseq(s+"0",X,n,sol)
      diffseq(s+"1",X,n,sol)

sol=[]
diffseq("","020",3,sol)
print(sol,"\n")

def diffseq2(sol,X,n):
    if len(sol)==n:
        print(sol)
        return 
    
    if X[len(sol)] != "0" :
      sol.append("0")
      diffseq2(sol,X,n)
      sol.pop()
      
    if X[len(sol)] != "1":
      sol.append("1")
      diffseq2(sol,X,n)
      sol.pop()
      
    if X[len(sol)] != "2" :
      sol.append("2")
      diffseq2(sol,X,n)
      sol.pop()

diffseq2([],"020",3)
print("=================================================================\n")


"""Progettare un algoritmo che, dato un intero n, stampa tutte le stringhe binarie
lunghe n in cui non appaiono mai k simboli uguali consecutivi.
L’algoritmo proposto deve avere complessità O(nD(n)) dove D(n) è il numero
di stringhe da stampare."""

def bin_cons(s,n,k,cont0=0,cont1=0):
    if len(s)==n:
        print(s)
        return
    
    if cont0+1<k:
      bin_cons(s+"0",n,k,cont0+1,cont1)
      
    if cont1+1<k:
      bin_cons(s+"1",n,k,cont0,cont1+1)
    
bin_cons("",4,3)
print("\n")


def bin_cons2(sol,n,k,cont0=0,cont1=0):
    if len(sol)==n:
        print(sol)
        return
    
    if cont0+1<k:
      sol.append("0")
      bin_cons2(sol,n,k,cont0+1,cont1)
      sol.pop()
      
    if cont1+1<k:
      sol.append("1")
      bin_cons2(sol,n,k,cont0,cont1+1)
      sol.pop()
    
    
bin_cons2([],4,3)
print("=================================================================\n")

"""Data una stringa binaria s, la differenza tra il numero di 1 e il numero di 0
 nelle prime i posizioni di s è detto vantaggio alla posizione i in s.
Ad esempio per s = 010010111000 il vantaggio nelle dodici posizioni è rispetti-
vamente: -1, 0, -1, -2, -1, -2, -1, 0, -1, 0, -1, -2.
Dati due interi positivi n ed a, a>=1, con S(n, a) definiamo l’insieme di stringhe
binarie di lunghezza n il cui vantaggio in ogni posizione cade nell’intervallo
(-a ; a) oppure [-a ; a]
Ad esempio: S(5, 2) = {01010 01011 01100 01101 10010 10011 10100 10101}
Trovate un algoritmo che dati n ed a stampi tutte le stringhe in S(n, a). La
complessità dell’algoritmo deve essere O(n · |S(n, a)|)."""

def vantaggio(s,n,v,cont):
    #intervallo chiuso (-v ; v)
    if len(s)==n:
        print(s)
        return

          
    if v==cont+1:
          vantaggio(s+"0",n, v,cont-1)
            
    elif -v==cont-1 :
          vantaggio(s+"1",n, v,cont+1)
          
    else: 
        vantaggio(s+"0",n, v,cont-1)
        vantaggio(s+"1",n, v,cont+1)
        
vantaggio("",5,2,0)        
print("\n")

def vantaggio2(sol,n,v,cont):
    #intervallo aperto [-v ; v]
    if len(sol)==n:
        print(sol)
        return
          
    if  v==cont:
          sol.append("0")
          vantaggio2(sol,n, v,cont-1)
          sol.pop()
            
    elif -v==cont :
          sol.append("1")
          vantaggio2(sol,n, v,cont+1)
          sol.pop()
          
    else : 
          sol.append("0")
          vantaggio2(sol,n, v,cont-1)
          sol.pop()
          sol.append("1")
          vantaggio2(sol,n, v,cont+1)
          sol.pop()
          
vantaggio2([],5,2,0)   
print("=================================================================\n")

