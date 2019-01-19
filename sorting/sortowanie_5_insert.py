#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:53:37 2018

@author: piter
"""

list=[5, 8, 3, 2]
print(list)
for j in range(len(list)+1,-1):
    key = list[j]
    i = j-1
    while (i > -1) and key < list[i]:
        list[i+1]=list[i]
        i=i-1
    list[i+1] = key
print(list)