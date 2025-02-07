def solution(n: int, arr: list[int]) -> list[int]:
    # 初始化最大乘积和对应的区间
    max_product = -1
    best_start, best_end = -1, -1
    
    # 遍历数组，尝试所有可能的区间
    for start in range(n):
        current_product = 1
        for end in range(start, n):
            # 计算当前区间的乘积
            current_product *= arr[end]
            
            # 如果乘积为0，跳过这个区间
            if current_product == 0:
                break
            
            # 如果当前乘积大于最大乘积，更新最大乘积和区间
            if current_product > max_product:
                max_product = current_product
                best_start, best_end = start + 1, end + 1  # 注意区间的起始位置为1
            
            # 如果当前乘积等于最大乘积，比较区间的起始和结束位置
            elif current_product == max_product:
                if start + 1 < best_start or (start + 1 == best_start and end + 1 < best_end):
                    best_start, best_end = start + 1, end + 1
    
    return [best_start, best_end]


if __name__ == "__main__":
    # Add your test cases here
    print(solution(5, [1, 2, 4, 0, 8]) == [1, 3])
    print(solution(7, [1, 2, 4, 8, 0, 256, 0]) == [6, 6])
