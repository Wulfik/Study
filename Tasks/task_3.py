def solution(A):
    per = 0
    for i in range(len(A)):
        main_r = i+A[i]
        new_i = i + 1
        if new_i < len(A):
            for new_i in range(new_i,len(A),1):
                next = new_i-A[new_i]
                if next<=main_r:
                    per+=1

    return per


solution([1,5,2,1,4,0])

