class Solution {
    public:
        void nextPermutation(vector<int>& nums) {
            //从后向前找没找第一个非递增的数字
            //第二次找比上一个大的数（由于是递增，第一个就是最小的大数）
            //找到后交换两个数，然后把后面的反转
            int n = nums.size() - 1;
            int i = n - 1;
    
            while(i >= 0 && nums[i] >= nums[i + 1]){
                i--;
            }
            if(i >= 0){
                int j = n;
                while(j >= 0 && nums[j] <= nums[i]){
                    j--;
                }
                swap(nums[i], nums[j]);
            }
    
            reverse(nums.begin() + i + 1, nums.end());
        }
    };