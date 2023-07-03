#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:49:44 2023

@author: mone
"""

#%% 千桁
def sendigit( value, daiji ):
     meisu = [ "十", "百", "千" ] if not daiji else ["拾", "佰", "仟" ]
     str_value = str(value)  # 整数を文字列に変換
     num_map = {'0':'零', '1':'一', '2':'二', '3':'三', '4':'四', '5':'五', '6':'六', '7':'七', '8':'八', '9':'九'}
     
     kanji_sen = []
     for i, digit_num in enumerate(str_value):
         if digit_num != '0' and i <= 3:
             print(i)
             digit_kanji = num_map[digit_num] + meisu[2 - i]
             kanji_sen.append(digit_kanji)
         elif kanji_sen and kanji_sen[-1][-1] != '零':
             kanji_sen.append('零')
             print(kanji_sen)
     return ''.join(kanji_sen) #4桁のvalueに対応した 漢数字の文字列を返すように定義して下さい
 
print(sendigit(9034,False))

#%% 無量大数まで
def kandigit( value, daiji=False ):
    
    taisu = [ "万" if not daiji else "萬", "億", "兆", "京", "垓", "𥝱", "穣", "溝", "澗", "正", "載", "極",
  "恒河沙", "阿僧祇", "那由他", "不可思議", "無量大数" ]
    return "零"  #valueに対応した 漢数字の文字列を返すように定義して下さい。sendigitを利用して4桁ずつ漢数字の文字列にしていきます。