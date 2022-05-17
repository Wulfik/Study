def solution(N):
    if type(N) not in[int] or N<=0:
        raise ValueError('Input bad number')
    binar = list(bin(N).split('b').pop(1))
    while True:
        if binar[0] == '0':
            binar.pop(0)
        if binar[-1] == '0':
            binar.pop(-1)
        if binar[0] == '1' and binar[-1] == '1':
            break
    repeat = 0
    srepeat = 0
    for number in binar:
        if number == '0':
            srepeat+=1
        if number == '1':
            if srepeat>repeat:
                repeat=srepeat
            srepeat=0

    return repeat
