// Solution to LeetCode problem 1: Two Sum
//
// Link: https://leetcode.com/problems/two-sum/description/
//
// Difficulty: Easy
//
// Description: Given an array of integers nums and an integer target, return
//              indices of the two numbers such that they add up to target.
//              You may assume that each input would have exactly one solution,
//              and you may not use the same element twice. 
//              You can return the answer in any order.
//
// Time Complexity: O(n)
//
// Space Complexity: O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> answer;
        std::map<int, int> seen;
        for (int i = 0; i < nums.size(); i++){
            int search_target = target - nums[i];
            if (not seen.empty()){
                std::map<int, int>::iterator it = seen.find(search_target);
                if (it != seen.end()){
                    answer = {i, seen[search_target]};
                    break;
                }
            }
            seen.insert(make_pair(nums[i], i));
        }
        return answer;
    }
};

