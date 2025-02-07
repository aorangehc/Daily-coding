def solution(inputArray):
    # 使用 sorted 函数和 lambda 表达式进行排序
    sorted_array = sorted(inputArray, key=lambda x: (x[0], -x[1]))
    # 返回排序后的结果
    lenth = len(sorted_array)
    L, R = sorted_array[0][0], sorted_array[0][1]
    ans = 0
    for i in range(1, lenth):
        l, r = sorted_array[i][0], sorted_array[i][1]
        if l <= R:
            R = max(R, r)
        else :
            ans += R - L + 1
            L, R = l , r
 
    # print(sum)
    ans += R - L + 1 
    return ans

if __name__ == "__main__":
    #  You can add more test cases here
    testArray1 = [[1,4], [7, 10], [3, 5]]
    testArray2 = [[1,2], [6, 10], [11, 15]]

    print(solution(testArray1) == 9 )
    print(solution(testArray2) )