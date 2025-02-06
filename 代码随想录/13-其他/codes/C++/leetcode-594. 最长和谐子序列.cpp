// https://leetcode.cn/problems/longest-harmonious-subsequence/description/
// 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
// 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
// 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
// example
// input nums = [1,3,2,2,5,2,3,7]
// output 5
// 最长的和谐子序列是 [3,2,2,2,3]


// 说明
// 本题要找最长和谐子序列，子序列中最大值和最小值的差值是1，说明序列中只有相邻的两个数字
// 因此本题要求相邻两数数量的最大值
// 先将所有的树进行排列，然后遍历即可


// 核心代码
class Solution {
public:
    int findLHS(vector<int>& nums) {
        // 完成数值由小到大排序
        sort(nums.begin(), nums.end());
        // 初始化指针和数值
        int begin = 0;
        int ans = 0;
        // 遍历数值
        for(int end = 0; end < nums.size(); end++){
            // 当end指向的值比begin指向的值大超过1就继续向前
            while(nums[end] - nums[begin] > 1){
                begin++;
            }
            // 如果两指针指向的值相等，就只更新end指针

            // 找到差值为1，计算相邻两数的数量，更新结果
            if(nums[end] - nums[begin] == 1){
                ans = max(ans, end - begin + 1);
            }
        }

        return ans;
    }
};