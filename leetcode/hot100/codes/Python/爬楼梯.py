class Solution:
    def climbStairs(self, n: int) -> int:
        # 创建dp数组，记录爬到当前位置有几种方法
        a = 1
        b = 1
        temp = 0

        for i in range(2, n + 1):
            temp = b
            b = a + b
            a = temp
        
        return b

