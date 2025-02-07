def solution(n: int, m: int, k: int, a: list[int], b: list[int]) -> int:
    k_squared = k ** 2
    min_diff = float('inf')  # 初始化最小差值为正无穷

    for i in range(len(a)):
        for j in range(len(b)):
            diff_squared = (a[i] - b[j]) ** 2
            current_diff = abs(diff_squared - k_squared)
            if current_diff < min_diff:
                min_diff = current_diff

    return int(min_diff)

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(5, 5, 1, [5, 3, 4, 1, 2], [0, 6, 7, 9, 8]) == 0)
    print(solution(5, 5, 0, [5, 3, 4, 1, 2], [0, 6, 7, 9, 8]) == 1)
    print(solution(5, 6, 3, [5, 3, 4, 1, 2], [0, 6, 7, 9, 8, 11]) == 0)
