#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:27:08 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/
Problem description: 
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
"""
# Time: O(n), space: O(n)
class Solution:
    def stringShift(self, s: str, shift) -> str:
        shiftValue = 0
        n = len(s)
        # take cumulative shift - for left shift subtract, for right shift add
        # left shift is actually same as right, only with negative value (sign)
        for el in shift:
            direction, amount = el
            if direction == 0:
                shiftValue -= amount
            else:
                shiftValue += amount
        chars = list(s)
        # shift values - use mod for index outrange 
        for i in range(n):
            chars[(i+shiftValue)%n] = s[i]
                
        # concat chars
        return "".join(chars)
sol = Solution()    

# Test 1
s = "abc"
shift = [[0,1],[1,2]]
print(sol.stringShift(s, shift))
# Test 2
s = "abcdefg"
shift =  [[1,1],[1,1],[0,2],[1,3]]
print(sol.stringShift(s, shift))

# Test 3
s = "wpdhhcj"
shift = [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]
print(sol.stringShift(s, shift))