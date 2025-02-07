def judge(num):
    str_num = str(num)
    c = str_num[0]
    for cs in str_num:
        if c != cs:
            return False
    
    return True
def solution(x, y):
    ans = 0

    for num in range(x, y + 1):
        if judge(num):
            ans += 1

    return ans


if __name__ == "__main__":
    # Add your test cases here

    print(solution(1, 10) == 9)
    print(solution(2, 22) == 10)
