#!/usr/bin/env python3
# -*- coding: utf-8 -*-

message = "    This is a simple  message for sample   program  "
wordlist = message.split()
print( wordlist )
print( " ".join( wordlist ))

nlist = [12,23,34,45,34,56,67,78,89,12,12]
line = ", ".join( map( str, nlist ))
print( line )

numlist = list( map( int, line.split( ", " ) ) )
print( numlist )

#%% 重複削除
def distinct(nlist):
    look = set()
    result = []
    for item in nlist:
        if item not in look:
            look.add(item)
            result.append(item)
    return result

my_list = [4,1,3,2,3,4]
result = distinct(my_list)
print(result)

#%% 結合
def combineTo(nlist):
    result = "と".join( map( str, nlist ))
    return result
    
my_list = ["あ","い","う",1,2,3,4]
result = combineTo(my_list)
print(result)

#%% 標準偏差
def stdev(nlist):
    mean = sum(nlist) / len(nlist)
    x = 0
    for item in nlist:
        x += (item - mean) ** 2
    return (x / len(nlist)) ** 0.5

my_list = [1,3,5,7]
result = stdev(my_list)
print(result)

#%% 偏差値
def stdev(nlist):
    mean = sum(nlist) / len(nlist)
    x = 0
    for item in nlist:
        x += (item - mean) ** 2
    return (x / len(nlist)) ** 0.5

def deviation(nlist):
    result = []
    mean = sum(nlist) / len(nlist)
    std = stdev(nlist)
    for item in nlist:
        dev = (((item - mean) * 10) / std) + 50
        result.append(dev)
    return result

my_list = [30,80,50,40,20,90]
result = deviation(my_list)
print(result)
