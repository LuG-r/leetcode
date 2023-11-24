"""
Solution to LeetCode problem 1: Two Sum

Link: https://leetcode.com/problems/two-sum/description/

Difficulty: Easy

Description: Given an array of integers nums and an integer target, return
             indices of the two numbers such that they add up to target.
             You may assume that each input would have exactly one solution,
             and you may not use the same element twice. 
             You can return the answer in any order.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       positions = {}

       for index, value in enumerate(nums):
           if target - value in positions.keys():
               return [index, positions[target - value]]
           else:
               positions[value] = index
