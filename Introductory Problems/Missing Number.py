# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:24:35 2020

@author: Wei Fong
"""

input_1 = int(input())    #Integer n
input_2 = list(map(int, input().split()))  #List with missing integer

#Test values
#input_1 = 5
#input_2 = sorted([2,3,1,5])
full = list(range(1,input_1+1))

result = list(set(full)-set(input_2))
print(result[0])
