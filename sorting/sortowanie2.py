#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:52:18 2018

@author: piter
"""


def sort(list):
    
    for x in range(len(list)-1,0,-1):
        for i in range(x):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list=[102,85,100,50]
sort(list)
print(list)
n = len(list)