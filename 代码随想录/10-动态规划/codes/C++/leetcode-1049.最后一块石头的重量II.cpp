#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum = 0;
        for (int stone : stones) {
            sum += stone;
        }
        int target = sum / 2;
        vector<int> dp(target + 1, 0);
        
        for (int i = 0; i < stones.size(); i++) {
            for (int j = target; j >= stones[i]; j--) {
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);
            }
            // 打印当前的 dp 数组
            cout << "After processing stone " << stones[i] << ": ";
            for (int k = 0; k <= target; k++) {
                cout << dp[k] << " ";
            }
            cout << endl; // 换行
        }

        return sum - dp[target] * 2;
    }
};

// 示例使用
int main() {
    Solution solution;
    vector<int> stones = {2, 7, 4, 1, 8, 1};
    int result = solution.lastStoneWeightII(stones);
    cout << "Result: " << result << endl;
    getchar();
    return 0;
}