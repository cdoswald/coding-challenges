# -*- coding: utf-8 -*-
"""
Date created: 24 August 2023
Author: Chris Oswald
Challenge: LeetCode #27 - Remove Element
Description: 
    Given an integer array nums and an integer val, remove all occurrences of 
    val in nums in-place. The order of the elements may be changed. Then return 
    the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, 
    to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the 
    elements which are not equal to val. The remaining elements of nums are not 
    important as well as the size of nums.
    
    Return k.
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remove_indices_list = []
        for index, num in enumerate(nums):
            if num == val:
                remove_indices_list.append(index)
        for index in reversed(sorted(remove_indices_list)):
            del nums[index]
        return len(nums)
