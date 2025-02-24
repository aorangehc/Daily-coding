class Solution:
    def numSquares(self, n: int) -> int:
        dp = [[0] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i] = i

            for j in range(1, 1+isqrt(i)):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        
        return dp[n]