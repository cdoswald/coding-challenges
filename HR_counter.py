# -*- coding: utf-8 -*-
"""
Date created: 24 October 2023
Author: Chris Oswald
Link: https://www.hackerrank.com/challenges/no-idea/problem
Description:
    There is an array of  integers. There are also  disjoint sets, A and B, each 
    containing m integers. You like all the integers in set A and dislike all 
    the integers in set B. Your initial happiness is 0. For each integer in 
    the array, if the integer is in A , you add 1 to your happiness. If the
    integer is in B, you add -1 to your happiness. Otherwise, your happiness 
    does not change. Output your final happiness at the end.

    Note: Since  and  are sets, they have no repeated elements. 
    However, the array might contain duplicate elements.

    Constraints

    Input Format

    The first line contains integers  and  separated by a space.
    The second line contains  integers, the elements of the array.
    The third and fourth lines contain  integers,  and , respectively.

    Output Format

    Output a single integer, your total happiness.

    Sample Input
    3 2
    1 5 3
    3 1
    5 7

    Sample Output
    1
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Import packages
from collections import Counter

# Read in inputs
n, m = input().split(sep=" ")
int_array = [int(x) for x in input().split(sep = " ")]
A = set([int(x) for x in input().split(sep=" ")])
B = set([int(x) for x in input().split(sep=" ")])

# Count integers in int_array
count_dict = Counter(int_array)

# Compute happiness
happiness = 0 
for int_val, int_count in count_dict.items():
    if int_val in A:
        happiness += int_count
    elif int_val in B:
        happiness -= int_count
print(happiness)
