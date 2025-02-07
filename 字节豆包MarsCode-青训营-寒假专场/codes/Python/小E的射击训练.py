import math

def solution(x: int, y: int) -> int:
    m = x * x + y * y
    r = math.sqrt(m)
    if math.floor(r) >= 11:
        return 0

    num = math.ceil(r)

    return 11 - num

if __name__ == '__main__':
    print(solution(1, 0) == 10)
    print(solution(1, 1) == 9)
    print(solution(0, 5) == 6)
    print(solution(3, 4) == 6)