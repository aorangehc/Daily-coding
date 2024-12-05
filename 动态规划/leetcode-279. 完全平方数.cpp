//
// https://leetcode.cn/problems/perfect-squares/description/?envType=study-plan-v2&envId=top-100-liked
//

//核心代码

class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = 0;
        for(int i = 1; i <= n; i++){
            int num = sqrt(i);
            // 当前的数值就是完全平方数
            if((i == num*num)) dp[i] = 1;
            else{
                dp[i] = dp[i-1] + 1;
                for(int j = 1; j < i; j++){
                    dp[i] = min(dp[i], dp[j] + dp[i-j]);
                }
            }
        }
        return dp[n];
    }
};

