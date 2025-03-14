class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ans[i - 1][j] + ans[i - 1][j - 1])
            ans.append(row)
        
        return ans