#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:35:12 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/
Problem description: 
First Unique Number
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:

Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]

Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1

 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.

"""

class FirstUnique:
    def __init__(self, nums):
        self.head = None
        self.tail = None
        self.cache = {}
        # all elements added in the queue
        self.addedEls = set()
        self._populateMap(nums)

            
    def _populateMap(self, nums):
        for i in range(len(nums)):
            self.add(nums[i])
        
    # private methods
    # reconnect previous and next node of the element we're removing
    # we have three cases - 
    #  a) we're moving head element
    #  b) we're moving tail element - do nothing
    #  c) we're moving internal element - some element between head and tail
    def _removeNodeAndReconnectLinkedListr(self, key):
        previous, next = self.cache[key]
        # only one element - head and tail at the same time
        if key == self.head and key==self.tail:
            self.head = self.tail = None
            return
        # tail case - case b)
        if key == self.tail:
            if previous:
                self.cache[previous][1] = None
            self.tail = previous
            return
        # we're moving head element - case a)
        if key == self.head:
            # set next element as new head
            self.cache[next][0] = None
            self.head = next
        
        # we're moving interal element
        else:
            # connect previous and next of the current node (case c)
            # before: prev -> key -> next
            # after: prev -> next
            self.cache[previous][1] = next
            # prev <- next
            self.cache[next][0] = previous

    # add key to cache - at the end of the linked list        
    def _insert(self, value):
        # cache is empty
        if len(self.cache) == 0:
            self.head = value
        # set new value at the end of ll
        self.cache[value] = [self.tail, None]
        if self.tail is not None:
            self.cache[self.tail][1] = value
        # this is new tail
        self.tail = value
        self.addedEls.add(value)



    def showFirstUnique(self) -> int:
        return self.head if self.head is not None else -1

    
    # Two cases:
    # 1) value is not in addedEls - insert element normally
    # 2) value is present in addedEls:
    # a) value is in cache -> reconnect predecessor and successor of this element; remove this element
    # b) value is not present in cache -> do nothing
    
    def add(self, value: int) -> None:
        if value in self.addedEls:
            if value in self.cache:
                self._removeNodeAndReconnectLinkedListr(value)
                self.cache.pop(value)

        else:
            self._insert(value)

    

            

            
print()
#parseInput(ops, params)
firstUnique = FirstUnique([2,3,5])
print(firstUnique.showFirstUnique())
firstUnique.add(5)
print(firstUnique.showFirstUnique())

firstUnique.add(2)
print(firstUnique.showFirstUnique())

firstUnique.add(3)
print(firstUnique.showFirstUnique())
print()


firstUnique = FirstUnique([7,7,7,7,7,7])
print(firstUnique.showFirstUnique())
firstUnique.add(7)
firstUnique.add(3)
firstUnique.add(3)
firstUnique.add(7)
firstUnique.add(17)
print(firstUnique.showFirstUnique())


firstUnique = FirstUnique([809])
print(firstUnique.showFirstUnique())
firstUnique.add(809)
print(firstUnique.showFirstUnique())


