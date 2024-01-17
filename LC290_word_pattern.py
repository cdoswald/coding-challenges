# -*- coding: utf-8 -*-
"""
Date created: 16 Jan 2024
Author: Chris Oswald
Challenge: LeetCode #290 - Word Pattern
Link: https://leetcode.com/problems/word-pattern/description
Description: 
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between 
    a letter in pattern and a non-empty word in s.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern) or len(set(s)) != len(set(pattern)):
            return False
        hashmap = {}
        # Loop over each letter in pattern
        for idx, letter in enumerate(pattern):
            word = hashmap.get(letter, None)
            if word is None:
                hashmap[letter] = s[idx]
            else:
                if s[idx] != word:
                    return False
        return True
