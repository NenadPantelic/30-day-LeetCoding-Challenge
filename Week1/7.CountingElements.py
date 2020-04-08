#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:25:20 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3289/
Problem description: 
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
Example 3:

Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
Example 4:

Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
"""

from collections import Counter
class Solution:
    def countElements(self, arr) -> int:
        counter = Counter()
        # O(n) - count freqs of every unique element
        for el in arr:
            counter[el] += 1
            
        totalCount = 0
        # O(n)
        for val in counter:
            # if x + 1 is in array
            if (val + 1) in counter:
                # update count with num of occurences of val
                totalCount += counter[val]
        return totalCount
             
    
sol = Solution()
# Test 1
arr = [1,2,3]
print(sol.countElements(arr))


# Test 2
arr = [1,1,3,3,5,5,7,7]
print(sol.countElements(arr))                


# Test 3
arr = [1,3,2,3,5,0]
print(sol.countElements(arr))


# Test 4
arr = [1,1,2,2]
print(sol.countElements(arr))         