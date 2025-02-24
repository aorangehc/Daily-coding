class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                len_word = len(word)
                if len_word <= i and dp[i] == False:
                    sub_str = s[i - len_word:i]
                    if sub_str == word:
                        dp[i] = dp[i - len_word]

        return dp[n]