//
// https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked
//


// 核心代码

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        vector<string> str2code(strs.size(), "00000000000000000000000000");

        // 将单词转成唯一字符串，字母异位词编码是相同的
        for(int i = 0; i < strs.size(); i++){
            for(int j = 0; j < strs[i].size(); j++){
                str2code[i][strs[i][j] - 'a'] = ((str2code[i][strs[i][j] - 'a'] - '/0') + 1) + '/0';
            }
        }

        // 标记已存储
        int flag[11451] = {0};
        for(int i = 0; i < strs.size(); i++){
            if(flag[i] == 1) continue;
            flag[i] = 1;
            vector<string> b;
            b.push_back(strs[i]);
            for(int j = i + 1; j < strs.size(); j++){
                if(str2code[j] == str2code[i]){
                    b.push_back(strs[j]);
                    flag[j] = 1;
                }
            }
            ans.push_back(b);
        }

        return ans;
    }
};