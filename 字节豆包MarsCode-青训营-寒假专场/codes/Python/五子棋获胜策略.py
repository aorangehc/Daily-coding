def solution(n, array):
    result = []
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 横、纵、主对角线、副对角线
    
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0:
                is_win = False
                for dx, dy in directions:
                    count = 1
                    # 正方向检查
                    x, y = i + dx, j + dy
                    while 0 <= x < n and 0 <= y < n and array[x][y] == 1:
                        count += 1
                        x += dx
                        y += dy
                    # 反方向检查
                    x, y = i - dx, j - dy
                    while 0 <= x < n and 0 <= y < n and array[x][y] == 1:
                        count += 1
                        x -= dx
                        y -= dy
                    if count >= 5:
                        is_win = True
                        break
                if is_win:
                    result.append([i + 1, j + 1])
    # 按行优先，列优先排序
    result.sort()
    return result


if __name__ == "__main__":
    # Add your test cases here
    array = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    print(solution(6, array) == [[1, 1], [6, 6]])
