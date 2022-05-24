from itertools import groupby

def solution(A):
    top_low_list = []
    A = [el for el, _ in groupby(A)]
    for i in range(len(A)):
        if i==0:
            if A[i]>A[i+1]:
                top_low_list.append(A[i])
        elif i==(len(A)-1):
            if A[i]>A[i-1]:
                top_low_list.append(A[i])
        elif (A[i]<A[i-1] and A[i]<A[i+1]) or (A[i]>A[i-1] and A[i]>A[i+1]):
            top_low_list.append(A[i])
    print(top_low_list)
    res = 0
    for i in range(1,len(top_low_list)-1):
        print(f'i = {i} | A = {top_low_list[i]}')
        left_high = 0
        right_high = 0
        low = 0
        if top_low_list[i] < top_low_list[i - 1] and top_low_list[i] < top_low_list[i + 1]:
            low = top_low_list[i]
            for j in range(i):
                print(top_low_list[j], left_high)
                if top_low_list[j]>left_high:
                    print('qwe')
                    left_high=top_low_list[j]
            for j in range(i+1,len(top_low_list)):
                if top_low_list[j]>right_high:
                    right_high=top_low_list[j]
            print(left_high,right_high)
            if left_high>=right_high:
                if (right_high-low)>res:
                    print('new res')
                    res = right_high-low
            else:
                if (left_high-low)>res:
                    print('new res')
                    res = left_high-low
        print(f'Left: {left_high} | Right: {right_high} | Low: {low} | Res: {res}')
    return res

A = [7,1,6,1,7]
print(solution(A))
