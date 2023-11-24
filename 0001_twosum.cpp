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

