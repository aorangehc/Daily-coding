def check_conditions(user_exp, query):
    for q in query[1:]:
        # print(q, user_exp)
        if q > 0 and q not in user_exp:
            return False
        if q < 0 and -q in user_exp:
            return False
    return True
def solution(n, m, q, arrayN, arrayQ):
    # Edit your code here
    result = []
    user_experiments = []

    for user in arrayN:
        experiments = set()
        for exp in user[1:]:
            experiments.add(exp)
        user_experiments.append(experiments)
    
    for query in arrayQ:
        count = 0
        for user_exp in user_experiments:
            if check_conditions(user_exp, query):
                count += 1
        result.append(count)

    return result


if __name__ == "__main__":
    # Add your test cases here

    print(
        solution(
            3,
            3,
            3,
            [[2, 1, 2], [2, 2, 3], [2, 1, 3]],
            [[2, 1, -2], [2, 2, -3], [2, 3, -1]],
        )
        
    )
