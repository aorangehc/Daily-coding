//
// https://leetcode.cn/problems/word-break/description/?envType=study-plan-v2&envId=top-100-liked
//


// 核心代码

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> w_set;
        for(string w : wordDict){
            w_set.insert(w);
        }
        vector<bool> dp(s.size()+1, false);
        dp[0] = true;
        for(int i = 1; i <= s.size(); i++){
            for(int j = 0; j < i; j++){
                if(dp[j] && w_set.find(s.substr(j, i - j)) != w_set.end()){
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.size()];
    }
};