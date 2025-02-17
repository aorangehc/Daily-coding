class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # 计算天数
        day = len(pizzas) // 4
        # 排序
        pizzas.sort()
        ji_day = 0
        ou_day = 0
        if day % 2 == 0:
            ji_day = day // 2
            ou_day = day // 2
        else:
            ji_day = day // 2 + 1
            ou_day = day // 2

        ans = 0
        ou = 1
        for i in range(day):
            end = len(pizzas) - 1 - i // 2
            if (i + 1) % 2 == 1:
                ans += pizzas[end]
                # print(end)
            else:
                ans += pizzas[end - ji_day - ou]
                # print(end - ji_day + 1 - ou * 2)
                ou += 1
            
        return ans
            
            