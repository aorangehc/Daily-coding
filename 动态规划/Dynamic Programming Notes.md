# 动态规划笔记

> 说明：本章节内容是动态规划相关题目的解题思路，以及C++、Python、和Go三种语言的解题过程
>
> 相关题目是[代码随想录](https://programmercarl.com/)的跟练，同时解题思路也是动态规划5步法

### [最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/description/)

#### 题目解读

有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

> 这个题目，乍一看很难懂，毫无思路，这跟动态规划有何关系，刚看题目一脸懵，这里面需要数学思维去思考。
>
> 粉碎的过程可以看作一个消耗的过程，粉碎之后有两种情况：一种是啥也不剩，双方都消耗光了，一种是大的一方剩一部分，小的一方完全消耗，大的一方剩的一部分可以继续消耗。这就像有两个阵营，相互进行血量消耗，看看最后剩多少血量。
>
> 显然，人和石头都是不可分的，因此将双方分成两个尽可能相等的阵营，计算双方差的绝对值行。
>
> 即，计算所有石头的总重量，让一堆石头重量达到小于等于总重量一半的最大值，然后用（剩余重量-该最大值）=（总重量-该最大值*2），计算差值，得到答案。
> 
> 通过动态规划对这个“最大值”进行求解。

#### 解题思路

##### 确定dp数组以及下标的含义

假设有dp[i]，则dp[i]表示容量为i的背包，最多可以装价值为dp[i]的石头 

##### 确定递推公式

由之前的推理可以得出：dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

由于石头的重量和价值都是一样的，因此可以将石头的重量和价值都当作价值。

最终递推公式为：dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

##### 初始化dp数组

初始容量都设为0即可

最大容量为总重量的一半，因此dp数组的长度为sum/2 + 1（注：+1是防止出现数组越界）

```C++
C++：vector<int> dp(sum/2 + 1, 0)

Python: dp = [0] * (sum/2 + 1)

Go: dp := make([]int, sum/2 + 1)
```

##### 确定遍历顺序

有两个遍历的维度：物品与背包，这里选择外层遍历物品，然后内层遍历背包。

```C++
for (int i = 0; i < stones.size(); i++) { // 遍历物品
    for (int j = target; j >= stones[i]; j--) { // 遍历背包
        dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);
    }
}
```

##### 打印or推导dp数组

调通代码，查看效果，测试dp数组是否与自己的预期一致。

进行推导，假设：stones = [2,7,4,1,8,1]，sum = 23，target = 11

| 背包容量 | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
|stones[0]|0    |0    |2    |2    |2    |2    |2    |2    |2    |2    |2    |2    |
|stones[1]|0    |0    |2    |2    |2    |2    |2    |7    |7    |9    |9    |9    |
|stones[2]|0    |0    |2    |2    |4    |4    |6    |7    |7   |9    |9    |11    |
|stones[3]|0    |1    |2    |3    |4    |5    |6    |7    |8   |9    |10    |11    |
|stones[4]|0    |1    |2    |3    |4    |5    |6    |7    |8   |9    |10    |11    |
|stones[5]|0    |1    |2    |3    |4    |5    |6    |7    |8   |9    |10    |11    |

[测试代码](leetcode-1049.最后一块石头的重量II.cpp)--打印测试用例的dp数组

#### 代码实现

##### C++

```C++
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum = 0;
        for(int stone : stones){
            sum += stone;
        }
        int target = sum / 2;
        vector<int> dp(target + 1, 0);
        for(int i = 0; i < stones.size(); i++){
            for(int j = target; j >= stones[i]; j--){
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);
            }
        }

        return sum - dp[target] * 2;
    }
};
```

##### Python

```Python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [0] * (target + 1)

        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return total - 2 * dp[target]
```

##### Go

```Go
func lastStoneWeightII(stones []int) int {
    sum := 0
    for i := 0; i < len(stones); i++ {
        sum += stones[i]
    }
    target := sum / 2

    dp := make([]int, target + 1)
    for i := 0; i < len(stones); i++ {
        for j := target; j >= stones[i]; j-- {
            dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        }
    }

    return sum - 2 * dp[target]
}
````