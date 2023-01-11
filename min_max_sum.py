#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:18:56 2022
@author: parisbg

Given five positive integers, 
find the minimum and maximum values that can be calculated by summing exactly 
four of the five integers. Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.
"""

#Sort the array
#label min val
#label max val
#traverse and sum entire array
#subtract min val from array sum and divide be len
#subtract max val from array sum and divide be len
arr = [3,5,6,1,3]
arr.sort()    
low = arr[0]
high = arr[len(arr)-1]
final_min = sum(arr)-low
final_max = sum(arr)-high
print(final_max, final_min)