def solution(dna_sequence):
    # 将序列加倍，以便可以方便地生成所有旋转序列
    doubled_sequence = dna_sequence + dna_sequence
    n = len(dna_sequence)
    min_sequence = dna_sequence  # 初始化最小序列为原始序列

    # 遍历所有可能的旋转序列
    for i in range(n):
        # 提取从位置 i 开始的长度为 n 的子序列
        candidate = doubled_sequence[i:i+n]
        # 如果当前候选序列比当前最小序列更小，则更新最小序列
        if candidate < min_sequence:
            min_sequence = candidate

    return min_sequence

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("ATCA") == "AATC")
    print(solution("CGAGTC") == "AGTCCG")
    print(solution("TCATGGAGTGCTCCTGGAGGCTGAGTCCATCTCCAGTAG") == "AGGCTGAGTCCATCTCCAGTAGTCATGGAGTGCTCCTGG")