def solution(s: str) -> str:
    ans = ''

    for c in s:
        if c == 'a':
            ans += '%100'
        else:
            ans += c
    return ans

if __name__ == '__main__':
    print(solution(s="abcdwa") == '%100bcdw%100')
    print(solution(s="abcdwa"))
    print(solution(s="banana") == 'b%100n%100n%100')
    print(solution(s="apple") == '%100pple')