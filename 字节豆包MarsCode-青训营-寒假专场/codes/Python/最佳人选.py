def solution(m, n, target, array):
    scores = []
    for i in range(n):
        cand = array[i]
        score = 0
        for j in range(m):
            if (cand[j] == 'A' and target[j] == 'E') or (cand[j] == 'E' and target[j] == 'A'):
                score = 255
                break
            elif (cand[j] == 'B' and target[j] == 'D') or (cand[j] == 'D' and target[j] == 'B'):
                score = 255
                break
            elif (cand[j] == 'C' and target[j] == 'E') or (cand[j] == 'E' and target[j] == 'C'):
                score = 255
                break
            elif (cand[j] == 'B' and target[j] == 'E') or (cand[j] == 'E' and target[j] == 'B'):
                score = 255
                break
            else:
                score += abs(ord(cand[j])-ord(target[j]))
        scores.append(255-score)
        
    max_score = max(scores)
    if max_score == 0:
        return 'None'
        
    people = []
    for i in range(n):
        if scores[i] == max_score:
            people.append(array[i])
    result = ' '.join(i for i in people)
    return result




if __name__ == "__main__":
    # Add your test cases here
    matrix = [
        "AAAAAA", "BBBBBB", "ABDDEB"
    ]
    print(solution(6, 3, "ABCDEA", matrix) == "ABDDEB")
