#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:47:57 2018

@author: piter
"""

list=[5, 8, 3, 2]
print(list)
for x in range(len(list)-1,0,-1):
    for i in range(x):
        klucz = list[i]
        j = i - 1
        
        while j >0 and list[j] > klucz:
            list[j+1] = list [j]
            j = j - 1
        list[j + 1] = klucz
print(list)