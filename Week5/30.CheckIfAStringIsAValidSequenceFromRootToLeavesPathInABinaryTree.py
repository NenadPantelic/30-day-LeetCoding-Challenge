#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:58:00 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/
Problem description:
Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

 

Example 1:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation: 
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -> 1 -> 1 -> 0 
0 -> 0 -> 0


Example 2:


Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false 
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
Example 3:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
 

Constraints:

1 <= arr.length <= 5000
0 <= arr[i] <= 9
Each node's value is between [0 - 9].

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Idea: do BFS and track path sequence
# When we reach a leaf element (both of it's subtrees are None), add this path to paths set
# Check if theg given path is present in paths set
class Solution:
    def DFS(self, root, path, paths):
        if root is None:
            return -1
        # add value of this node to the current path
        path += str(root.val)
        # there are two possible outputes from this function - None or -1 (for leaf case)
        # if left subtree and right subtree are -1, that means that this node is leaf, so we have a path
        # that we should compare with the given path
        leftSubtree = self.DFS(root.left, path, paths)
        rightSubtree = self.DFS(root.right, path, paths)        
        if leftSubtree == -1 and rightSubtree == -1:
            # add this path to path set - we will check if given path is among these paths
            paths.add(path)
        
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        paths = set()
        self.DFS(root, "", paths)
        return "".join(list(map(str, arr))) in paths
# Test 1-3
node1 = TreeNode(0)
node2 = TreeNode(1)
node3 = TreeNode(0)
node1.left = node2
node1.right = node3
node4 = TreeNode(0)
node5 = TreeNode(1)
node2.left = node4
node2.right = node5
node6 = TreeNode(0)
node3.left = node6
node7 = TreeNode(1)
node4.right = node7
node8 = TreeNode(0)
node9 = TreeNode(0)
node5.left = node8
node5.right = node9

sol = Solution()
# Test 1
arr = [0,1,0,1]
print(sol.isValidSequence(node1, arr))

# Test 2
arr = [0,1,1]
print(sol.isValidSequence(node1, arr))

# Test 3
arr = [0,0,1]
print(sol.isValidSequence(node1, arr))


# Test 4
node1 = TreeNode(3)
node2 = TreeNode(0)
node1.left = node2
node3 = TreeNode(2)
node2.left = node3
node4 = TreeNode(2)
node3.right = node4
node5 = TreeNode(9)
node4.left = node5
node6 = TreeNode(3)
node4.right = node6
arr = [3,0]
print(sol.isValidSequence(node1, arr))