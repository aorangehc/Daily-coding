def solution(n: int, s: list, x: list) -> list:
    # 创建一个字典来记录每个人的总金额
    amount_dict = {}
    
    for i in range(n):
        name = s[i]
        amount = x[i]
        if name in amount_dict:
            amount_dict[name] += amount
        else:
            amount_dict[name] = amount
    
    # 创建一个包含参与者信息的列表，每个元素是一个元组 (name, total_amount, first_index)
    participants = [(name, amount_dict[name], s.index(name)) for name in amount_dict]
    
    # 使用sorted函数进行排序，自定义排序规则
    sorted_participants = sorted(participants, key=lambda p: (-p[1], p[2]))
    
    # 提取排序后的名字列表
    result = [p[0] for p in sorted_participants]
    
    return result

if __name__ == '__main__':
    print(solution(4, ["a", "b", "c", "d"], [1, 2, 2, 1]) == ['b', 'c', 'a', 'd'])
    print(solution(3, ["x", "y", "z"], [100, 200, 200]) == ['y', 'z', 'x'])
    print(solution(5, ["m", "n", "o", "p", "q"], [50, 50, 30, 30, 20]) == ['m', 'n', 'o', 'p', 'q'])