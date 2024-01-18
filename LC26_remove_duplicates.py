# -*- coding: utf-8 -*-
"""
Date created: 17 Jan 2024
Author: Chris Oswald
Challenge: LeetCode #26 - Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array
Description: 
    Given an integer array nums sorted in non-decreasing order, remove the 
    duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. Then return 
    the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, 
    you need to do the following things:

    Change the array nums such that the first k elements of nums contain the 
    unique elements in the order they were present in nums initially. The 
    remaining elements of nums are not important as well as the size of nums.
    
    Return k.
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0; j = 1
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return len(set(nums))
                