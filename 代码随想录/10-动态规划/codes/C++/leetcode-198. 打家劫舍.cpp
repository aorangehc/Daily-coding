//
// https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=top-100-liked
//


//核心代码

class Solution {
public:
    int rob(vector<int>& nums) {
        // 基本思路偷第K间房，第K-1间房不能偷，当前的值是（前K-2的最大值）+K的值
        // 第K间房不偷，当前的最大值是，前K-1的最大值

        int prev = 0;//K-2
        int curr = 0;//K-1
        //i是K的值
        for (int i : nums) {
            int temp = max(curr, prev + i);
            prev = curr;
            curr = temp;
        }

        return curr;
    }
};