# -*- coding: utf-8 -*-
"""
Date created: 22 Jan 2024
Author: Chris Oswald
Challenge: LeetCode #859: Buddy Strings
Link: https://leetcode.com/problems/buddy-strings/
Description:
    Given two strings s and goal, return true if you can swap two letters in s 
    so the result is equal to goal, otherwise, return false.

    Swapping letters is defined as taking two indices i and j (0-indexed) 
    such that i != j and swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if set(s) != set(goal):
            return False

        nonmatching_idxs = [idx for idx in range(len(s)) if s[idx] != goal[idx]]
        if len(nonmatching_idxs) > 2 or len(nonmatching_idxs) == 1:
            return False
        if len(nonmatching_idxs) == 2:
            idx1 = nonmatching_idxs[0]
            idx2 = nonmatching_idxs[1]
            if s[idx1] == goal[idx1] and s[idx2] == goal[idx2]:
                return True
            if s[idx1] == goal[idx2] and s[idx2] == goal[idx1]:
                return True
        if len(nonmatching_idxs) == 0:
            letter_count = {}
            for letter in s:
                letter_count[letter] = letter_count.get(letter, 0) + 1
            if max(letter_count.values()) > 1:
                return True
        return False
