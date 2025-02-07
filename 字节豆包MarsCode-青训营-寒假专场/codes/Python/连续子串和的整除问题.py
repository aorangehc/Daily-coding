def solution(n, b, sequence):
    prefix_sum = 0
    mod_count = {0: 1}  # 初始化模0的计数为1，处理从序列开始的子序列
    result = 0

    for num in sequence:
        prefix_sum += num
        mod_value = prefix_sum % b

        if mod_value in mod_count:
            result += mod_count[mod_value]
            mod_count[mod_value] += 1
        else:
            mod_count[mod_value] = 1

    return result

if __name__ == "__main__":
    #  You can add more test cases here
    sequence = [1, 2, 3]
    print(solution(3, 3, sequence) == 3)