# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:56:01 2020

@author: Wei Fong
"""
n = int(input())

while True:
    remainder = round(n%2,2)
    if remainder != 0 and n != 1:
        print(n)
        n = int(n*3 + 1)
        continue
    elif remainder == 0:
        print(n)
        n = int(n/2)
    elif remainder != 0 and n == 1:
        print(n)
        break
