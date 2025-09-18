#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:24:37 2024

@author: mirko
"""

"""Il problema della massima sottosequenza comune. Date due
sequenze di simboli X e Y , vogliamo trovare una sottosequenza
comune X e Y che abbia lunghezza massima."""


def max_subseq_comune(X, Y):
    n, m = len(X), len(Y)
    T = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                T[i][j] = 0

            elif X[i-1] == Y[j-1]:

                T[i][j] = T[i-1][j-1]+1

            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])

    return T, T[n][m]


print(max_subseq_comune("ABC", "CBA"))

"""Progettare un algoritmo che, dato un intero n , calcola il
numero di stringhe binarie lunghe 2n
per le quali
la somma dei primi n bit è uguale alla somma degli ultimi n bit.
per n = 2 per la risposta dell’algoritmo deve essere 6
infatti le stringhe di lunghezza 2*2=4 che soddisfano il
vincolo sono : 0101, 0110, 1010, 1001, 0000 1111
L’algoritmo proposto deve avere complessità Θ(n).
"""
def conta_stringhe_binarie_equilibrate(n):
    # Inizializzazione della tabella T
    T = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
    
    # Caso base: T[0][n] = 1, rappresenta la differenza 0 con stringa vuota
    T[0][n] = 1
    
    # Popolamento della tabella T
    for i in range(2 * n):
        for j in range(2 * n + 1):
            if T[i][j] > 0:
                if j + 1 <= 2 * n:  # Se aggiungiamo un '1' nei primi n bit
                    T[i + 1][j + 1] += T[i][j]
                if j - 1 >= 0:  # Se aggiungiamo un '1' negli ultimi n bit
                    T[i + 1][j - 1] += T[i][j]
    
    # Risultato: numero di stringhe con differenza 0
    return T,T[2 * n][n]


n = 4
print(conta_stringhe_binarie_equilibrate(n))  # Output: 70
