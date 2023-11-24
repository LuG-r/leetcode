"""
Solution to LeetCode problem 2: Add Two Numbers

Link: https://leetcode.com/problems/add-two-numbers/

Difficulty: Medium

Description: You are given two non-empty linked lists representing 
             two non-negative integers. The digits are stored in reverse
             order, and each of their nodes contains a single digit.
             Add the two numbers and return the sum as a linked list.
             You may assume the two numbers do not contain any leading zero,
             except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str, l2_str = "", ""
        
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next

        l1_str = l1_str[::-1]
        l2_str = l2_str[::-1]
        
        result = str(int(l1_str) + int(l2_str))

        answer = None
        for digit in result:
            current_listnode = ListNode(int(digit), answer)
            answer = current_listnode
        return answer        


