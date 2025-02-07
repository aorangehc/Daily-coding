def solution(inp):
    len_inp = len(inp)

    for i in range(len_inp // 2):
        sub_str = inp[0 : i + 1]
        if len_inp % len(sub_str) == 0:
            repeat_count = len_inp // len(sub_str)
            if sub_str * repeat_count == inp:
                    return sub_str
    return ""


if __name__ == "__main__":
    # Add your test cases here

    print(solution("abcabcabcabc") == "abc")
