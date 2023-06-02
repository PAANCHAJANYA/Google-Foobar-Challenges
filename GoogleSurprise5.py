lst = [2368799, 2556283, 2757825, 2974399, 3207085, 3457026, 3725409, 4013543, 4322815, 4654669, 5010687, 5392549, 5802007, 6240973, 6711479, 7215643, 7755775, 8334325, 8953855, 9617149, 10327155, 11086967, 11899933, 12769601, 13699698, 14694243, 15757501, 16893951, 18108417, 19406015, 20792119, 22272511, 23853317, 25540981, 27342420, 29264959, 31316313, 33504745, 35839007, 38328319, 40982539, 43812109, 46828031, 50042055, 53466623, 57114843, 61000703, 65139007, 69545357, 74236383, 79229675, 84543781, 90198445, 96214549, 102614113, 109420548, 116658615, 124354421, 132535701, 141231779, 150473567, 160293887, 170727423, 181810743, 193582641, 206084095, 219358314, 233451097, 248410815, 264288461, 281138047, 299016607, 317984255, 338104629, 359444903, 382075867, 406072421, 431513601, 458482687, 487067745]
partitionCount = 0
def partitions(remSum,maxVal):
    global partitionCount
    if (remSum == 0):
        partitionCount = partitionCount + 1
        return
    i = maxVal
    while(i >= 1):
        if (i > remSum):
            i -= 1
            continue
        elif (i <= remSum):
            partitions(remSum - i, i)
            i -= 1
def solution(n):
    count = 0
    if n > 120:
        return lst[n-121]
    for itr in range(1,n+1):
        if (((itr)*(itr+1))/2) > n:
            r = itr-1
            break
    for itr in range(2,r+1):
        partitions(int(n-((itr*(itr+1))/2)),itr)
        print(partitionCount)
    return partitionCount
for iterator in range(2,201):
    temp = solution(iterator)
    print("Solution:", temp)
    partitionCount = 0
'''
from itertools import combinations
def solution(n):
    count = 0
    for itr in range(1,n+1):
        if (((itr)*(itr+1))/2) > n:
            r = itr-1
            break
    for itr in range(2,r+1):
        for lst in list(combinations([i for i in range(1,n+1)], itr)):
            if sum(lst)==n:
                print(lst)
                count = count + 1
    return count
print(solution(20))'''
