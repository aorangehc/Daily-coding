def solution(N, M, data):
    # Edit your code here
    data1 = data * M
    ans = data1[0]

    cnt = 0
    for i in range(len(data1)):
        cnt += data1[i]
        if cnt > 0:
            ans = max(ans, cnt)
        else:
            cnt = 0

    return ans


if __name__ == "__main__":
    # Add your test cases here
    print(solution(5, 1, [1, 3, -9, 2, 4]))
    print(solution(5, 3, [1, 3, -9, 2, 4]))
