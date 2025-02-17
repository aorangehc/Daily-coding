class Solution {
    public:
        void sortColors(vector<int>& nums) {
            // 两个指针，分别指定0和2的位置
            int ptr_0 = 0, ptr_2 = nums.size() - 1;
            for(int i = 0; i <= ptr_2; i++){
                while(i <= ptr_2 && nums[i] == 2) {
                    swap(nums[i], nums[ptr_2]);
                    ptr_2 -= 1;
                }
                if(nums[i] == 0){
                    swap(nums[i], nums[ptr_0]);
                    ptr_0 += 1;
                }
            }
        }
    };