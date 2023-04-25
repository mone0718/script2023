# 授業url:https://web.sfc.keio.ac.jp/~minohara/lectureslide/computation/NumericAnalysis2.pdf

#!/usr/bin/python 
# で何かができるらしい
# -*- coding:utf-8 -*-
# 何かを指定するらしい

# import sys
# print(sys.version)

# # 虚数と複素数
# print(1j)
# print(0.5j)
# print(2+2j)
# print(2.3-7.j)

# # 共役複素数と実部、虚部の取り出し
# print((1+1j).conjugate())
# print((3+4j).real)
# print((3+4j).imag)

# # 極形式
# import cmath
cvalue = 3 + 4j
# print(abs(cvalue)) #絶対値
# print(cmath.phase(cvalue)) #偏角
# print(cmath.polar(cvalue)) #絶対値と偏角
# print(cmath.rect(2, cmath.pi)) #絶対値と偏角から複素数(極形式)を返す

# 複素数の演算
dvalue = 5 + 2j
print(cvalue + dvalue) #複素数平面上ではベクトルの足し算
print(cvalue - dvalue) #ベクトルの引き算
print(cvalue * dvalue) #*実数は絶対値の掛け算、*虚数は90度回転
print(cvalue / dvalue) #掛け算の逆
print(cvalue ** 2) #ド・モアブルの定理




