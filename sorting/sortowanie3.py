#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 22:41:08 2018

@author: piter
"""

list=[5, 8, 3, 2]
print(list)
for x in range(len(list)-1,0,-1):
    print("printed ", x)
    for i in range(x):
        if list[i+1] < list[i]:
            print(list[i+1])
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            print(list)
            
        

        