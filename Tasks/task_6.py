def solution(A):
    amount = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j])
            if i==len(A)-1:
                if j == 0:
                    if A[i][j + 1] != A[i][j]:
                        amount += 1
                elif j == 1:
                    if A[i][j + 1] != A[i][j]:
                        amount += 1
                elif j == 2:
                    amount += 1
            else:
                if j==0:
                    if A[i+1][j]!=A[i][j] and A[i][j+1]!=A[i][j]:
                        amount+=1
                elif j==1:
                    if A[i+1][j]!=A[i][j] and A[i][j+1]!=A[i][j]:
                        amount+=1
                elif j==2:
                    if A[i+1][j]!=A[i][j]:
                        amount+=1
            print(f'amount = {amount}')
    return amount


A = [[5,4,4],[4,3,4],[3,2,4],[2,2,2],[3,3,4],[1,4,4,],[4,1,1],[1,4,4]]
print(f'\namount = {solution(A)}')