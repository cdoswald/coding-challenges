# -*- coding: utf-8 -*-
"""
Date created: 24 August 2023
Author: Chris Oswald
Challenge: LeetCode #169 - Majority Element
Description:
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.

    Example 1:

    Input: nums = [3,2,3]
    Output: 3
    Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_dict = {}
        for i in range(len(nums)):
            counter_dict[nums[i]] = counter_dict.get(nums[i], 0) + 1
        return sorted(counter_dict, key=counter_dict.get, reverse=True)[0]
