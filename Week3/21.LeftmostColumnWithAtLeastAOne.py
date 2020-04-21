#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:42:59 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/
Problem description: 
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

 

Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
   Hide Hint #1  
1. (Binary Search) For each row do a binary search to find the leftmost one on that row and update the answer.
   Hide Hint #2  
2. (Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner. p can only move left or down. If the value at p is 0, move down. If the value at p is 1, move left. Try to figure out the correctness and time complexity of this algorithm.


"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

# Algorithm:
# 1. Start at the top right corner - 0th row, m-1th column
# 2. examine values:
# a) if value == 1 -> go left, set the flag for found 1 (for case where there is no 1 in matrix), and set the 
# lastOneCol to value of current col -> to know what is the last column where we found 1
# b) if value == 0 -> go down examine the same column but the next row
# 3. repeat second step until we go out of the matrix
# Time: O(n+m), space: O(1)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix) -> int:
        #n, m = len(binaryMatrix), len(binaryMatrix[0])
        n, m = binaryMatrix.dimensions()
        row = 0
        col = m-1
        # last column where we found 1
        lastOneCol = col
        # flag that says if we found 1 at all
        oneFound = False
        while 0 <= row < n and 0 <= col < m:
            #value = binaryMatrix[row][col] 
            value = binaryMatrix.get(row, col)
            # one found - update lastOneCol, go left and set oneFound to True
            if value == 1:
                lastOneCol = col
                col -= 1
                oneFound = True
            # zero found - go down    
            else:
                row += 1
        # one is not found - return -1
        if not oneFound:
            return -1
        # return last column where we met 1
        return lastOneCol
    
sol = Solution()
# Test 1
mat = [[0,0],[1,1]]     
print(sol.leftMostColumnWithOne(mat))    

# Test 2
mat = [[0,0],[0,1]]     
print(sol.leftMostColumnWithOne(mat))   


# Test 3
mat = [[0,0],[0,0]]     
print(sol.leftMostColumnWithOne(mat)) 


# Test 4
mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]     
print(sol.leftMostColumnWithOne(mat))     
            