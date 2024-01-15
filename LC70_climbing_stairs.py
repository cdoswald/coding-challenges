# -*- coding: utf-8 -*-
"""
Date created: 15 Jan 2024
Author: Chris Oswald
Challenge: LeetCode #70 - Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs
Description: 
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways 
    can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        count_ways = 0
        start_range = 0 if (n % 2 == 0) else 1
        for k in range(start_range, n+1, 2):
            count_ways += math.comb(int((n-k)/2 + k), k)
        return(count_ways)
