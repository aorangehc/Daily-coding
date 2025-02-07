from collections import defaultdict

def solution(A):
    # 对成绩进行排序
    sorted_A = sorted(A)
    
    # 创建一个字典，用于存储每个成绩小于或等于自己的学生数量
    count_dict = defaultdict(int)
    for i, score in enumerate(sorted_A):
        count_dict[score] = i + 1
    
    # 计算说谎的学生数量
    liars = 0
    for score in A:
        less_or_equal = count_dict[score]
        greater = len(A) - less_or_equal
        if less_or_equal > greater:
            liars += 1
    
    return liars


if __name__ == "__main__":
    # Add your test cases here
    print(solution([100, 100, 100]) == 3)
    print(solution([2, 1, 3]) == 2)
    print(solution([30, 1, 30, 30]) == 3)
    print(solution([19, 27, 73, 55, 88]) == 3)
    print(solution([19, 27, 73, 55, 88, 88, 2, 17, 22]) == 5)
