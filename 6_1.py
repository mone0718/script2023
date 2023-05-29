#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:40:32 2023

@author: mone
"""
import numpy as np

#%% Pythonのリストからの生成
narray = np.array([23, 34, 45, 56, 67, 78, 89])
nmatrix = np.array( [[1,2,3],[4,5,6],[7,8,9]] )
print( narray )
print( nmatrix )
print( type( narray ), type( nmatrix ) )

#%% ファンシーインデックスと論理値フィルタ
print( narray[ [5, 2, 3, 6] ] )
print( nmatrix[ [1,2] ])
print( narray[ [True, False, True, True, False, True, False]])
print( nmatrix[ [[True,False,True],[False,True,True],[True,False,False]] ])

#%% スライス式
print( narray[ 4:] )
print( narray[ -1:-6:-2] )

#%% 論理式によるフィルタリング
print( narray%2==0 )
print( narray[narray%2==0] )
print( nmatrix%2==0 )
print( nmatrix[nmatrix%2==0] )

#%% 多次元配列のスライス式
print( nmatrix[1:,1:])
print( nmatrix[:,0 ] )
print( nmatrix[:,1:3])