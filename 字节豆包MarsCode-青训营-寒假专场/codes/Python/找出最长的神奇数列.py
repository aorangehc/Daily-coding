def solution(inp):
    max_len = 0
    max_str = ''

    for i in range(len(inp)):
        temp = '1' if inp[i] == '0' else '0'
        cnt_len = 1
        for j in range(i + 1, len(inp)):
            if inp[j] != temp:
                break
            temp = '1' if temp == '0' else '0'
            cnt_len += 1
        if cnt_len > max_len:
            max_len = cnt_len
            max_str = inp[i : i + cnt_len]
    if max_len < 3:
        max_str = ''
    return max_str


if __name__ == "__main__":
    # Add your test cases here

    print(solution("0101011101") == "010101")
