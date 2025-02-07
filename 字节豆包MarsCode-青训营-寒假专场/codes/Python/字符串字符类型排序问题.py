def solution(inp):
    inp_list = list(inp)
    letter_list = []
    digit_list = []

    for c in inp_list:
        if c.isdigit() :
            digit_list.append(c)
        elif c.isalpha() :
            letter_list.append(c)
    
    digit_list = list(reversed(sorted(digit_list)))
    letter_list = sorted(letter_list)

    letter_index = 0
    digit_index = 0

    ans_list = []

    for c in inp_list:
        if c.isdigit() :
            ans_list.append(digit_list[digit_index])
            digit_index += 1
        elif c.isalpha() :
            ans_list.append(letter_list[letter_index])
            letter_index += 1
        else :
            ans_list.append(c)
    return ''.join(ans_list)


if __name__ == "__main__":
    # Add your test cases here

    print(solution("12A?zc") == "21A?cz")
    print(solution("1Ad?z?t24") == "4Ad?t?z21")
    print(solution("???123??zxy?") == "???321??xyz?")
