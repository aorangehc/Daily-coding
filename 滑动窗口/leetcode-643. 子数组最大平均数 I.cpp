// https://leetcode.cn/problems/maximum-average-subarray-i/description/
//
//


// 核心代码
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        vector<double> sum_nums(nums.size(), 0.0);
        sum_nums[0] = nums[0];
        for(int i = 1; i < nums.size(); i++){
            sum_nums[i] = nums[i] + sum_nums[i - 1];
        }
        double max_sum = sum_nums[k - 1];
        for(int i = k; i < nums.size(); i++){
            max_sum = max(max_sum, double(sum_nums[i] - sum_nums[i - k]));
        }
        return max_sum / (k * 1.0);
    }
};