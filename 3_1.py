#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ## 複素数の三角関数

# import cmath
# import math

# for angle in range(0, 360, 10):
#     theta = math.radians(angle)
#     print(abs(cmath.sin(theta*1j))) #発散してく
    
# ## Unicode(Spyderだと表示してくれない、ターミナルで)
# resultstr = ""
# for ucode in range(0x13000, 0x1342f):
#     if ucode % 16 == 0: print(f"{ucode:5x} ", end = "") #5文字の16進数表示
#     print(chr(ucode), end = "  ")
#     if ucode % 16 == 15: print()
    
# ## BNF記法 バッカス・ナウア記法
#<expression> ::= <factor> + <factor> | <factor> - <factor> | <factor>
#<factor> ::= <element> * <element> | <element> / <element> | <element>
#<element> ::= <canstant> | <variable> | (<expression>)|-<constant>|-<variable>
#<constant> ::= 整数値
#<variable> ::= 変数名

#45 * 23 - 7 / -y
#<factor>        -       <factor>
#<element> * <element>   <element> / <element>
#<constant>  <constant>  <constant>  <constant>

# ## 代入演算子
# := 式の中で=と同じことができる

# ## 整数除算
# print(34 // 4.2) #→8

# for n in range(1, 10):
#     print(34.3 // n)
# print(3.5 // 4.8) #→0
    
# ## 実数を使って剰余算を計算すると誤差が出る
# print(3.4 % 0.7) #→0.6
# print(3.5 % 0.7) #→0.0000...

# # a // b と a % bを出力
# print(divmod(3.4, 0.7)) #→4.0, 0.600...01

# ## 整数を各桁に分解
# value = 123456
# while value > 0:
#     print(value % 10, end = " ")
#     value = value // 10
# print()

# value = 123456
# resultstr = ""
# while value > 0:
#     resultstr = str(value % 10) + resultstr
#     value = value // 10
# print(resultstr)

## n進数の文字列を返す関数(2~10)
# def nstr(value, n):
#     resultstr = ""
     
     
#＃ マイナスが入ると、床関数で計算されるのでマイナスの方に引っ張られる







