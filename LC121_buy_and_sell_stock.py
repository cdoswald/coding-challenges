# -*- coding: utf-8 -*-
"""
Date created: 29 August 2023
Author: Chris Oswald
Challenge: LeetCode #121 - Best Time to Buy and Sell Stock
Description: 
    You are given an array prices where prices[i] is the price of a given stock
    on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock 
    and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you 
    cannot achieve any profit, return 0.

    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List

# Note that this solution works for smaller test cases but times out at test
# case 200/212; see other posted submissions for more efficient solutions
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index, buy_price in enumerate(prices):
            if index == (len(prices)-1):
                return profit
            sell_price = max(prices[index+1:])
            if (sell_price > buy_price) and (sell_price - buy_price > profit):
                profit = sell_price - buy_price
        return profit