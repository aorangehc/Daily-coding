class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1
        for i in range(len(arr) - 1, -1, -1):
            x = arr[i]
            arr[i] = maxx
            maxx = max(maxx, x)
        
        return arr