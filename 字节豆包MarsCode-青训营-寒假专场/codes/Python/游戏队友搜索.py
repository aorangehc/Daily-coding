def solution(id, num, array):
    user_dic = {}

    # 使用集合来存储比赛记录，以便快速进行交集操作
    for row in array:
        if row[0] in user_dic:
            user_dic[row[0]].add(row[1])
        else:
            user_dic[row[0]] = {row[1]}

    ans = []

    # 获取指定玩家的比赛记录
    target_games = user_dic.get(id, set())

    for user, games in user_dic.items():
        if user != id:
            # 计算交集的大小
            common_games = target_games & games
            if len(common_games) >= 2:
                ans.append(user)

    ans.sort()
    return ans


if __name__ == "__main__":
    # Add your test cases here

    print(
        solution(
            1,
            10,
            [
                [1, 1],
                [1, 2],
                [1, 3],
                [2, 1],
                [2, 4],
                [3, 2],
                [4, 1],
                [4, 2],
                [5, 2],
                [5, 3],
            ],
        )
        == [4, 5]
    )