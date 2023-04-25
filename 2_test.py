#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot

rlist, imlist = [], []

for tx in range(1, 3):
    x = tx / 1.0
    for ty in range(0, 10, 2):
        y = ty / 10.0
        for tu in range(1, 91):
            u = tu / 10.0
            
            p = (2.0 + y*1j) ** (u*1j)
            
            rlist.append(p.real)
            imlist.append(p.imag)
            
            print("x:" + str(x) + " y:" + str(y) + " u:" + str(u) + " p:" + str(round(p.real,2)) + " " + str(round(p.imag,2)))
            
pyplot.plot(rlist, imlist,lw=0,marker='o',ms=3)
pyplot.show()



# value = (1+1j)*(1/2**0.5)*1.02
# rlist, imlist = [], []

# for n in range( 100 ):
#     p = 1 + 0.2 * n
#     rlist.append( (value**p).real )
#     imlist.append( (value**p).imag )
#     print( value**p )
    
# pyplot.plot( rlist, imlist )
# pyplot.show()

    
    
