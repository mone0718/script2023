#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 17:16:35 2023

@author: mone
"""

#%% 単位分数
import math

def gcd( n, m ):
    more, less = max( m, n ), min( m, n )
    return less if more % less == 0 else gcd( less, more % less )

def fibonatti( bunshi, bumbo ):
    yakubun = gcd( bunshi, bumbo )
    x, y = bunshi//yakubun, bumbo//yakubun
    if x == 1:
        print( f"1/{y}" )
    else:
        yx = math.ceil( y/x )
        print( f"1/{yx}", end="+" )
        fibonatti( x - (y%x), y * yx )

bs = int( input( "分子：" ) )
bb = int( input( "分母：" ) )
print( f"{bs}/{bb}", end="=")
fibonatti( bs, bb )

#%% Romberg積分

def romberg( f, a, b, n, m ):
    if n == 0 and m == 0:
        h = (b - a)/2.0
        return h * (f(a)+f(b))
    elif m == 0:
        h = (b - a)/(2**n)
        summ = 0
        for k in range( 1, 2**(n-1)+1 ):
            summ += f(a+h*(2*k-1))
        summ = summ * h
        return romberg(f,a,b,n-1,0)/2.0 + summ
    else:
        return romberg(f,a,b,n,m-1) + ((romberg(f,a,b,n,m-1) - romberg(f,a,b,n-1,m-1)) / (4**m - 1)) # この部分を書き換える

# 円弧のy座標を求める関数
def f(x):return (1-x**2)**0.5

# 積分してみる
print( romberg( f, 0.0, 1.0, 17, 6) )

