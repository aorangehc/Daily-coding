def solution(n, array):
    ans = 0

    events = []
    for l in array:
        start = l[0]
        end = l[1] + start
        events.append((start, 1))
        events.append((end, -1))
    
    events.sort(key = lambda x : (x[0], x[1]))

    temp = 0

    for e in events:
        temp += e[1]
        ans = max(ans, temp)

    return ans


if __name__ == "__main__":
    # Add your test cases here
    print(
        solution(2, [[1,2], [2,3]]) == 2
    )
    print(
        solution(4, [[1,2], [2,3],[3,5], [4,3]]) == 3
    )

