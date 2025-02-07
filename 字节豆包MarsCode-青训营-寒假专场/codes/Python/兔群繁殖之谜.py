def solution(A: int) -> int:
    s_rabbits = 1 # 当前月份新繁殖的
    b_rabbits = 0 # 已经成年的
    # 下一个月份成年的：b_rabbits + s_rabbits
    # 下一个月新生的：b_rabbits

    for i in range(A):
        temp = b_rabbits
        b_rabbits += s_rabbits
        s_rabbits = temp

    return b_rabbits + s_rabbits


if __name__ == "__main__":
    # Add your test cases here
    print(solution(1) == 1)
    print(solution(5))
    print(solution(15) == 987)
