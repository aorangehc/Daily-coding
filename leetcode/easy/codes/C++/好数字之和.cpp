class Solution {
    public:
        int sumOfGoodNumbers(vector<int>& nums, int k) {
            int ans = 0;
    
            for(int i = 0; i < nums.size(); i++){
                int flag = 0;
                if(i - k >= 0){
                    if(nums[i] <= nums[i - k]){
                        flag = 1;
                    }
                }
                if(i + k  < nums.size()){
                    if(nums[i] <= nums[i + k]){
                        flag = 1;
                    }
                }
                if(flag == 0){
                    ans += nums[i];
                }
            }
    
            return ans;
        }
    };