//
// Chttps://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked
//


// 核心代码

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0;
        unordered_set<int> num_set(nums.begin(), nums.end());

        int len;

        for(int num: num_set){
            if(!num_set.count(num - 1)){
                len = 1;
                while(num_set.count(++num)) len++;
                ans = max(ans, len);
            }
        }

        return ans;

    }
};