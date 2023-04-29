#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%% 実数の小数部の3桁分だけを整数として取り出す
#4.254683 → 254

y = 4532.21
print(int((y % 1) * 1000 // 1))

#%% 四捨五入
def schoolround(x):
    return int(x + 0.5)

print(schoolround(4.4))

#%% n! 実数と整数
n = 0
ans = 1
x = 0.0
ans_x = 1.0

for i in range(1, 30):
    n = n + 1
    ans = ans * n
    print(ans, end = " ")
    
    x = x + 1.0
    ans_x = ans_x * x
    print(ans_x)
    

