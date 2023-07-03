#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:57:32 2023

@author: mone
"""

#%% 累積値
alist = [8, 8, 1, 2, 1, 3, 1, 2, 3, 2]
blist = [0] * len(alist)
blist = [ (summ := alist[0]) if i == 0 else (summ := summ + alist[i]) for i in range( len( alist ) ) ]
print(blist)
print(summ)

#%% 中央値
def median( nlist ):
    mlist = sorted( nlist )
    size = len( mlist )
    return (mlist[size//2-1] + mlist[size//2])/2 if size % 2 == 0 else mlist[size//2]

def quantile( nlist ):
    mlist = sorted( nlist )
    size = len( mlist )
    if size % 2 == 1:
        return [median(mlist[:size//2]),median(mlist),median(mlist[size//2+1:])]
    else:
        return [median(mlist[:size//2]),median(mlist),median(mlist[size//2:])]

print(quantile([1, 2, 3, 4, 5]))