class Solution {
    public:
        vector<vector<int>> generate(int numRows) {
            vector<vector<int>> ans(numRows);
            ans[0] = {1};
    
            for(int i = 1; i < numRows; i++){
                vector<int> a(i + 1, 1);
                ans[i] = a;
                for(int j = 1; j < i; j++){
                    int num = ans[i-1][j-1] + ans[i-1][j];
                    ans[i][j] = num;
                }
            }
    
            return ans;
        }
    };