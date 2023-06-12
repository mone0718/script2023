#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:33:47 2023

@author: mone
"""

def is_perfect_number(num):
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sum(divisors) == num

def print_perfect_numbers(n):
    count = 0
    num = 6  # 最初の完全数は6から始まる

    while count < n:
        if is_perfect_number(num):
            print(num)
            count += 1
        num += 1

# 最初の5つの完全数を出力
print_perfect_numbers(5)
