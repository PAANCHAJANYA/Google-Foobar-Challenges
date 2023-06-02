def solution(start, length):
    res = 0
    itr = start
    skip = 1
    while itr <= start+(length*(length-1)):
        if itr > 2000000000:
            break
        if ((itr - 1)%4 == 0):
            x = itr - 1
        elif ((itr - 1)%4 == 1):
            x = 1
        elif ((itr - 1)%4 == 2):
            x = itr
        elif ((itr - 1)%4 == 3):
            x = 0
        if ((itr + length - skip)%4 == 0):
            y = itr + length - skip
        elif ((itr + length - skip)%4 == 1):
            y = 1
        elif ((itr + length - skip)%4 == 2):
            y = itr + length - skip + 1
        elif ((itr + length - skip)%4 == 3):
            y = 0
        if itr == start+(length*(length-1)):
            res = res ^ start+(length*(length-1))
        else:
            res = res ^ x ^ y
        itr = itr + length
        skip = skip + 1
    return res
print(solution(17,4))
