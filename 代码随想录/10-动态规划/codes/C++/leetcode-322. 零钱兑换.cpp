//
// https://leetcode.cn/problems/coin-change/description/?envType=study-plan-v2&envId=top-100-liked
//


//核心代码

//一个测试用例超超时
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        sort(coins.begin(), coins.end());
        vector<int> ans(amount+3, -1);
        ans[0] = 0;
        for(int num:coins){
            if(num<=amount) ans[num] = 1;
        }

        for(int i = 1; i <=amount; i++){
            for(int j = 1; j <= i/2; j++){
                if(ans[i] == -1){
                    if(ans[j] != -1 && ans[i-j] != -1){
                        ans[i] = ans[j] + ans[i-j];
                    }
                }
                else{
                    if(ans[j] != -1 && ans[i-j] != -1){
                        ans[i] = min(ans[i], ans[j] + ans[i-j]);
                    }
                }
            }
        }

        return ans[amount];

    }
};


//能过
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int Max = amount + 1;
        vector<int> dp(amount + 1, Max);
        dp[0] = 0;
        for (int i = 1; i <= amount; ++i) {
            for (int j = 0; j < (int)coins.size(); ++j) {
                if (coins[j] <= i) {
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
