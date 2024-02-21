#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:41:25 2024

@author: stephenson
"""

N = 0

while N <= 10:
#the above line is essentilly stating that if the var N is above 10, which 
#in this particular case it is...it's been set to zero; execute the given 
#control structure
    print(N)
    #so, whatever is stored at the counter before the data at the var is
    #changed with the code at the statement below
    #is logged to the terminal emulator before it's actually modified
    N = N + 2