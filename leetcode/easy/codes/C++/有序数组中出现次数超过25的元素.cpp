class Solution {
    public:
        int findSpecialInteger(vector<int>& arr) {
            int len_arr = arr.size();
            int m = len_arr / 4;
    
            for(int i = 0; i < len_arr; i++){
                if(arr[i] == arr[i + m]){
                    return arr[i];
                }
            }
            return 0;
        }
    };