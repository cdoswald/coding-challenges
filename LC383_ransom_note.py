# -*- coding: utf-8 -*-
"""
Date created: 09 September 2023
Author: Chris Oswald
Challenge: LeetCode #383 - Ransom Note
Description: 
    Given two strings ransomNote and magazine, return true if ransomNote can 
    be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

    Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

    Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for magazine_letter in magazine:
            letters[magazine_letter] = letters.get(magazine_letter, 0) + 1
        for ransom_letter in ransomNote:
            if ransom_letter not in letters:
                return False
            else:
                letters[ransom_letter] -= 1
                if letters[ransom_letter] < 0:
                    return False
        return True