# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:28:05 2020

@author: Wei Fong
"""
#dna_str = 'AAAAAAAAAA'
#dna_str = 'AAAACCCGGT'
#dna_str = 'ACCGGGTTTT'
dna_str=input()

count_list = []
count = 1

for i in range(1,len(dna_str)+1):
    try:
        if dna_str[i-1] == dna_str[i]:
            count = count + 1
        elif dna_str[i-1] != dna_str[i]:
            count_list.append(count)
            count = 1
    except:
        count_list.append(count)
            

print(max(count_list))