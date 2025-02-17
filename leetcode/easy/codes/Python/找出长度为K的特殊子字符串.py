class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                len_cnt = i - start
                if len_cnt == k:
                    return True
                start = i
        if len(s) - start == k:
            return True

        return False