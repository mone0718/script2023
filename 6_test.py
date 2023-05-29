#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:21:24 2023

@author: mone
"""

#%% 5_test
print(len( [ n for n in range( 1, 10581481 ) if 10581480%n == 0 ] ) )

#%% 100~200 sosuu
a = [ n for n in range( 100, 201 ) if all(n % i != 0 for i in range(2, int(n**0.5)+1))]
print(a)

#%% [ 12, 23, 34, 45, 56, 67, 78, 89, 100, 111, 122, 133, 144 ]
b = [ (n+1)*10+n+2 for n in range( 13 ) ]
print(b)

#%% [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0 ]
c = [ 0 if n%3==2 else 1 for n in range( 21 ) ]
print(c)

#%% [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210]
d = [ n*(n+1) for n in range( 1, 15 ) ]
print(d)