#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:09:53 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3283/

Problem description: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

from collections import Counter
# Time: O(n); space: O(n)
class Solution:
    def singleNumber(self, nums) -> int:
        counter = Counter()
        for val in nums:
            counter[val] += 1
        
        for val in counter:
            if counter[val] == 1:
                return val
        
sol = Solution()
# Test 1
nums = [2,2,1]
print(sol.singleNumber(nums))

# Test 2
nums = [4,1,2,1,2]
print(sol.singleNumber(nums))


        
