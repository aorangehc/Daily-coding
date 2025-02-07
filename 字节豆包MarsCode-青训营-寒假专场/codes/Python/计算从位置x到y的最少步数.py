def solution(x_position, y_position):
    length = abs(x_position - y_position)
    num = 0  # 当前步长已经使用的次数
    len_now = 1  # 当前步长
    res = 0  # 总步数

    while length > 0:
        if num == 2:  # 如果当前步长已经使用了两次
            len_now += 1  # 增加步长
            num = 0   # 重置步长使用次数
        length -= len_now  # 减少剩余距离
        num += 1       # 增加步长使用次数
        res += 1       # 增加总步数

    return res

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(12, 6) == 4 )
    print(solution(34, 45) == 6)
    print(solution(50, 30) == 8)