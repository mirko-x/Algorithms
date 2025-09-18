#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:39:01 2024

@author: mirko
"""
def fib(n):
 F=[-1]*(n+1)
 return fibmem(n, F)

def fibmem(n,F):
    if n<=1 : return 1
    if F[n]==-1:
        F[n]=fibmem(n-1,F)+fibmem(n-2,F)
    return F[n]
        
print(fib(100))

def fibmemit(n):
    F=[-1]*(n+1)
    F[0]=F[1]=1
    for i in range(2,n+1):
        F[i]=F[i-2]+F[i-1]
    return F[n] 

print(fibmemit(100))


def fibmemit2(n):
    a=b=1
    for i in range(2,n+1):
        n=a+b
        a,b=n,n-b
    return n


print(fibmemit2(100))


"""Dato un intero n vogliamo contare quante sono le stringhe binarie
lunghe n in cui non compaiono 2 zeri consecutivi."""

def es1(n):
    T=[0]*(n+1)
    T[0]=1
    T[1]=2
    for i in range (2,n+1):
        T[i]=T[i-1]+T[i-2]
        
    return T[n]

print(es1(5))

"""Dato un intero n vogliamo contare quante sono le stringhe binarie
lunghe n in cui non compaiono 3 zeri consecutivi."""

def es2(n):
    T=[0]*(n+1)
    T[0]=1
    T[1]=2
    T[2]=4
    for i in range (3,n+1):
        T[i]=T[i-1]+T[i-2]+T[i-3]
        
    return T[n]

print(es2(5))

"""Data stringa lunga n verifica che sia palindroma"""
def pal(A):
    n=len(A)
    for i in range(n-1,-1,-1):
        if A[n-i-1]!=A[i]:
            return False
    return True


A="baacaab"
print(pal(A))
            


  