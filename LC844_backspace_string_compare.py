# -*- coding: utf-8 -*-
"""
Date created: 14 Jan 2024
Author: Chris Oswald
Challenge: LeetCode #844 - Backspace String Compare
Link: https://leetcode.com/problems/backspace-string-compare/description/
Description: 
    Given two strings s and t, return true if they are equal when both are 
    typed into empty text editors. '#' means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # Define function to remove backspaced characters
        def remove_chars(input_str: str) -> str:
            retain_chars = []
            backspace_counter = 0
            i = 0
            while i < len(input_str):
                # Loop through reversed list
                val = input_str[-(i+1):-(i+2):-1]
                if val != "#":
                    if backspace_counter == 0:
                        retain_chars.append(val)
                    else:
                        backspace_counter -= 1
                else:
                    backspace_counter += 1
                i += 1
            return ("".join(retain_chars))

        # Check for equality
        hashmap = {f'{remove_chars(s)}_': True} # Add suffix in case s or t is empty string
        return(hashmap.get(f'{remove_chars(t)}_', False))
