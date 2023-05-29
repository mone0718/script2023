#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 22:33:57 2023

@author: mone
"""

#%% 文字列のスライス

# こまるんだ
w = "だるまさんがころんだ"
print(w[-4]+w[2:0:-1]+w[-2:])

#%% 約数
def find_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# テスト用例
number = 10581480
result = find_divisors(number)
print(f"The divisors of {number} are: {result} count:{len(result)}")

#%% 合同
w = 5
z = 12

if w % 7 == z % 7:
    print("yes")
else:
    print("no")
        
