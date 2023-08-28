# -*- coding: utf-8 -*-
"""
Date created: 28 August 2023
Author: Chris Oswald
Description:
    You are given a two lists A and B. Your task is to compute their cartesian 
    product X.
    
    Example
    A = [1, 2]
    B = [3, 4]
    AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

    Note:  and  are sorted lists, and the cartesian product's tuples should be 
    output in sorted order.
        
    The first line contains the space separated elements of list .
    The second line contains the space separated elements of list .
    
    Both lists have no duplicate integer elements.
    
    Output the space separated tuples of the cartesian product.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = tuple([int(x) for x in input().split(' ')])
B = tuple([int(x) for x in input().split(' ')])

print(' '.join([str(x) for x in product(A, B)]))

# OR with unpacking operator

print(*[x for x in product(A, B)])
