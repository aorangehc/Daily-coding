class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # 直接找
        m = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + m]:
                return arr[i]