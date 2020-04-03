#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:53:32 2020

@author: nenad
"""
"""
Problem URL: https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3285/
Problem description: 
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

class Solution:
    # Kadane's algorithm
    def maxSubArray(self, nums):
        maxSoFar = 0
        maxGeneral = 0
        for val in nums:
            maxSoFar += val
            if maxSoFar < 0:
                maxSoFar = 0
            if maxGeneral < maxSoFar:
                maxGeneral = maxSoFar
        return maxGeneral if maxGeneral > 0 else max(nums)