def solution(n, m, str1, str2):
    max_len = 0
    for c in 'abcdefghijklmnopqrstuvwxyz':
        left = 0
        cost = 0
        current_max = 0
        for i in range(n):
            if str1[i] != c:
                if str2[i] == '1':
                    cost += 1
                else:
                    left = i + 1
                    cost = 0
                    continue
            # 调整左指针以维持cost不超过m
            while cost > m:
                if str1[left] != c and str2[left] == '1':
                    cost -= 1
                left += 1
            current_max = max(current_max, i - left + 1)
        max_len = max(max_len, current_max)
    return max_len

if __name__ == "__main__":
    # Add your test cases here
    print(solution(5, 2, "abcda", "01110"))  # 输出: 3
    print(solution(7, 2, "abbaccb", "1001001"))  # 输出: 4
    print(solution(3, 0, "aab", "101") == 2)  # 输出: True