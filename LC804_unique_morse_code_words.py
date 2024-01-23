# -*- coding: utf-8 -*-
"""
Date created: 22 Jan 2024
Author: Chris Oswald
Challenge: LeetCode #804: Unique Morse Code Words
Link: https://leetcode.com/problems/unique-morse-code-words/description/
Description: 
    International Morse Code defines a standard encoding where each letter is 
    mapped to a series of dots and dashes, as follows:

        'a' maps to ".-",
        'b' maps to "-...",
        'c' maps to "-.-.", and so on.
        
    For convenience, the full table for the 26 letters of the English 
    alphabet is given below:

    [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
     "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
     "-.--","--.."]
    
    Given an array of strings words where each word can be written as a 
    concatenation of the Morse code of each letter.

    For example, "cab" can be written as "-.-..--...", which is the 
    concatenation of "-.-.", ".-", and "-...". We will call such a 
    concatenation the transformation of a word.
    
    Return the number of different transformations among all words we have.
"""
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        import string
        alphabet = string.ascii_letters
        morse_table = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
            ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
            ".--","-..-","-.--","--.."
        ]

        n_unique_words = 0
        words_dict = {}
        for word in words:
            morse_repr = ""
            for letter in word:
                morse_repr += morse_table[alphabet.index(letter)]
            if morse_repr not in words_dict:
                words_dict[morse_repr] = True
                n_unique_words += 1
        return n_unique_words
