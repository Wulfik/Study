def solution(S):
    conditions = ['AA','BB','CC']
    while True:
        if (conditions[0] or conditions[1] or conditions[2]) not in S:
            break
        for condition in conditions:
            S = S.replace(condition,'')
    return S

