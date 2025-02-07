def solution(plates: list[int], n: int) -> str:
    ans = ''

    count_se = 1
    start = 0

    for i in range(1, n):
        if plates[i] - plates[i - 1] == 1:
            count_se += 1
        else:
            if count_se >= 3:
                ans += str(plates[start]) + '-' + str(plates[i - 1]) + ','
            else:
                for j in range(start, i):
                    ans += str(plates[j]) + ','
            count_se = 1
            start = i
    if count_se >= 3:
        ans += str(plates[start]) + '-' + str(plates[n - 1])
    else:
        for j in range(start, n):
            ans += str(plates[j]) + ','
        ans = ans[:-1] 

    return ans


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], 10)  )
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20], 20) == "-6,-3-1,3-5,7-11,14,15,17-20")
    print(solution([1, 2, 7, 8, 9, 10, 11, 19], 8) == "1,2,7-11,19")
