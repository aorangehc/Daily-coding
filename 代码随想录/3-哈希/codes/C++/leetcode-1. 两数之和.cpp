//
// https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
//


// 核心代码
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> a;
        vector<int> ans(2, -1);
        for(int i = 0; i < nums.size(); i++){
            if(a.count(target - nums[i]) > 0){
                ans[0] = a[target - nums[i]];
                ans[1] = i;
                break;
            }
            a[nums[i]] = i;
        }
        return ans;
    }
};
