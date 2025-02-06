//
// https://leetcode.cn/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-100-liked
//


//核心代码

/* 递归会超时
class Solution {
public:
    int find(int num){
        if(num == 0) return 1;
        if(num < 0) return 0;
        return find(num - 1) + find(num - 2);
    }
    int climbStairs(int n) {
        int ans = find(n);
        return ans;
    }
};
*/
class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 1;
        int ans = 1;
        for(int i = 1; i < n; i++){
            ans = a + b;
            a = b;
            b = ans;
        }
        return ans;
    }
};
