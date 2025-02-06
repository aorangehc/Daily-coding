// https://leetcode.cn/problems/find-the-integer-added-to-array-i/description/
//
//


// 核心代码
class Solution {
public:
    int addedInteger(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        return(nums2[nums2.size() - 1] - nums1[nums1.size() - 1]);
    }
};
