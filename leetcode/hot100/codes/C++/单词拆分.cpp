class Solution {
    public:
        bool wordBreak(string s, vector<string>& wordDict) {
            int n = s.size();
            vector<bool> dp(n + 1, false);
    
            dp[0] = true;
            for(int i = 1; i <= n; i++){
                for(string word : wordDict){
                    int len_word = word.size();
                    if(len_word <= i && dp[i] == false){
                        string sub_str = s.substr(i - len_word, len_word);
                        if(sub_str == word){
                            dp[i] = dp[i - len_word];
                        } 
                    }
                }
            }
    
            return dp[n];
        }
    };