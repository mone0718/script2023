#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 00:29:18 2023

@author: mone
"""

#%% リストの演算

# 各要素ごとの加算
def add( a, b ):
    if len( a ) != len( b ):
        raise Exception( "vector size is different" )
    return [ n + m for n, m in zip( a, b ) ]

# 各要素ごとの減算
def sub( a, b ):
    if len( a ) != len( b ):
        raise Exception( "vector size is different" )
    return [ n - m for n, m in zip( a, b ) ]

# スカラー積
def scalarmul( a, m ): # where m is scalar value
    return [ n*m for n in a ]

# 各要素ごとの乗算
def eachmul( a, b ):
    if len( a ) != len( b ):
        raise Exception( "vector size is different" )
    return [ n * m for n, m in zip( a, b ) ]

# 各要素ごとの減算
def eachdiv( a, b ):
    if len( a ) != len( b ):
        raise Exception( "vector size is different" )
    return [ n / m for n, m in zip( a, b ) ]

# 内積
def dot( a, b ):
    if len( a ) != len( b ):
        raise Exception( "vector size is different" )
    return sum( n * m for n, m in zip( a, b ) )

# クロス積
def cross( a, b ):
    if len( a ) != 3 or len( b ) != 3:
        raise Exception( "vector size 3 only" )    
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

# 直積（デカルト積）
def cartesian( a, b ):
    if len( a ) != len( b ):
        raise Exception( "vector size is different" )
    result = []
    for n in a:
        for m in b:
            result.append( [n, m] )
    return result

# 2ノルム
def norm( a ):
    return sum( map( lambda n:n**2, a ) )**0.5

a = [ 4, 5, 8 ]
b = [ 3, 9, -8 ]

print(dot(a, b))
print(cartesian(a, b))
print(cross(a, b))

# print( a, norm(a) )
# print( b, norm(b) )
# print( add( a, b ), sub( a, b ) )
# print( scalarmul( a, 2.6 ) )
# print( eachmul( a, b ), eachdiv( a, b ) )
# print( dot( a, b ), cross( a, b ) )
# print( cartesian( a, b ) )

#%% 行列の演算

# A, Bの行列の形が同じかどうかチェックする
def check( A, B ):
    if len(A) != len(B) or \
        any( len(A[i]) != len(B[i]) for i in range(len(A))):
        raise Exception( "Matrix sizes are not equal" )

# 各要素同志の加算
def add2( A, B ):
    check( A, B )
    return [ [ n+m for n, m in zip( AR,BR )] for AR, BR in zip( A, B ) ]

# 各要素同志の減算
def sub2( A, B ):
    check( A, B )
    return [ [ n-m for n, m in zip( AR,BR )] for AR, BR in zip( A, B ) ]

# 各要素同志の乗算（アダマール積）
def hadamard( A, B ):
    check( A, B )
    return [ [ n*m for n, m in zip( AR,BR )] for AR, BR in zip( A, B ) ]

# 各要素同志の除算
def sub3( A, B ):
    check( A, B )
    return [ [ n/m for n, m in zip( AR,BR )] for AR, BR in zip( A, B ) ]

# 行列の乗算
def prod( A, B ):
    if len( A[0] ) != len( B ):
        raise Exception( "Matrix sizes are not compatible" )
    result = [ [ 0 for _ in range(len(A[0]))] for _ in range(len(A)) ]
    for i in range( len(A[0]) ):
        for j in range( len(B) ):
            result[ i ][ j ] = sum( A[ i ][ k ] * B[ k ][ j ] for k in range( len(A) ))
    return result

# 転置
def transpose( M ):
    result = []
    for j in range(len(M[0])):
        row = [M[i][j] for i in range(len(M) )]
        result.append( row )
    return result


MA = [ [2, 3, 4, 5], [8, 7, 6, 9], [12, 4, 5, 9 ], [ -1, 3, 5, 2 ] ]
MB = [ [6, 7, 1, 2 ], [8, 9, 1, 3], [5, 7, 9, 11], [8, 10, 2, 4] ]

# print( add2( MA, MB ) )
print( prod( MA, MB ) )
# print( prod( MB, MA ) )
# print()

# numpyでの計算方法
import numpy as np
NMA = np.matrix( MA )
NMB = np.matrix( MB )
# print( NMA+NMB )
# print( NMA@NMB )
# print( NMB@NMA )
# print()

# フロベニウス・ノルム
def norm2( A ):
    return sum( n**2 for row in A for n in row )**0.5

# numpyの線形代数モジュールと比較しながら求めてみる
import numpy.linalg as lin
# print( norm2( MA ) )
# print( lin.norm( NMA ) )
# print( norm2( MB ) )
# print( lin.norm( NMB ) )
# print()

# numpyの転置と比較しながら求めてみる
# print( transpose( MA ) )
# print( np.transpose( NMA ) )
# print( transpose( MB ) )
# print( np.transpose( NMB ) )
# print()

# 2次元の正方行列の行列式
def determinant2( A ):
    #print( A[0][0]*A[1][1] - A[0][1]*A[1][0] )
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

# 正方行列の行列式
def determinant( A ):
    if len(A)==2: return determinant2( A )
    size = len( A[0] )
    summ = 0
    for j in range( size ):
        m = determinant( minor( A, 0, j ) )
        summ += A[0][j] * m if j%2==0 else -A[0][j] * m
    return summ

# 小行列（i行とj列を省いた行列）を返す関数
def minor( A, i, j ):
    size = len(A)
    result = [ ]
    for m in range( size ):
        if m != i:
            row = []    
            for n in range( size ):
                if n != j: row.append( A[m][n] )
            result.append( row )
    #print( result )
    return result

# 行列式をnumpyと比較しながら求める
print( determinant( MA ) * determinant( MB ) )
# print( lin.det( NMA ) )
# print( determinant( MB ) )
# print( lin.det( NMB ) ) 
