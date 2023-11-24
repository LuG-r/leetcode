class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       positions = {}

       for index, value in enumerate(nums):
           if target - value in positions.keys():
               return [index, positions[target - value]]
           else:
               positions[value] = index
