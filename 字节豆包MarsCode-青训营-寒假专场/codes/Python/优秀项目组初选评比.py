def solution(m: int, n: int, a: list) -> int:
    if 2 * n < len(a):
        return -1

    a.sort()
    
    for i in range(len(a)):
        if i + 1 >= m and i + 1 <= n and len(a) - i - 1 >= m and len(a) - i - 1 <= n:
            return a[i]
   

    return -1

if __name__ == '__main__':
    print(solution(2, 3, [1, 2, 3, 5, 6, 4]))
    print(solution(1, 2, [7, 8, 9, 3, 5]))
    print(solution(1, 4, [7, 8, 9, 3, 5]))
