def solution(version1, version2):
    v1_list = version1.split('.')
    v2_list = version2.split('.')

    while len(v1_list) < max(len(v1_list), len(v2_list)):
        v1_list.append('0')
    while len(v2_list) < max(len(v1_list), len(v2_list)):
        v2_list.append('0')

    for i in range(len(v1_list)):
        if v1_list[i] > v2_list[i]:
            return 1
        elif v1_list[i] < v2_list[i]:
            return -1

    return 0


if __name__ == "__main__":
    # Add your test cases here

    print(solution("0.1", "1.1") == -1)
    print(solution("1.0.1", "1"))
    print(solution("7.5.2.4", "7.5.3") == -1)
    print(solution("1.0", "1.0.0") == 0)
