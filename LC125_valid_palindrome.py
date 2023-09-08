# -*- coding: utf-8 -*-
"""
Date created: 08 September 2023
Author: Chris Oswald
Challenge: LeetCode #125 - Valid Palindrome
Description: 
    A phrase is a palindrome if, after converting all uppercase letters into 
    lowercase letters and removing all non-alphanumeric characters, it reads 
    the same forward and backward. Alphanumeric characters include letters and 
    numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
"""
# More readable, slightly faster, but more memory intensive
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        chars = [char.lower() for char in s if char.isalnum()]
        forward = "".join(chars)
        return forward == forward[::-1]

# Memory efficient
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True