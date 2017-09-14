# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:05:25 2017

@author: python88
"""
#%%
def read_data(file_name):
    
    file = open(file_name, 'r')
    lines = file.readLines()
    return lines

lines = read_data('matrix.txt')

#%%
    