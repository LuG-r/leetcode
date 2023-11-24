"""
Solution to LeetCode problem 1: Two Sum

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Difficulty: Medium

Description: Given a string s, find the length of the longest substring
             without repeating characters.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        length = 0

        for char in s:
            if char not in substring:
                substring.append(char)
                length = max(length, len(substring))
            else:
                substring = substring[substring.index(char) + 1:]
                substring.append(char)
        return length
