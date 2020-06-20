# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:16:25 2020

@author: Wei Fong
"""

arr_size = int(input())
arr_contents = list(map(int, input().split()))

turns = 0
for i in range(1,arr_size):
    if arr_contents[i] < arr_contents[i-1]:
        diff = (arr_contents[i-1] - arr_contents[i])
        turns += diff
        arr_contents[i] += diff
        
print(turns)

