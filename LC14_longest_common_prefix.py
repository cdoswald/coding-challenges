# -*- coding: utf-8 -*-
"""
Date created: 23 Jan 2024
Author: Chris Oswald
Challenge: LeetCode #14 - Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/description
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        shortest_word = min(strs, key=len)
        for i, letter in enumerate(shortest_word):
            for word in strs:
                if word[i] != letter:
                    return common_prefix
            common_prefix += letter
        return common_prefix
