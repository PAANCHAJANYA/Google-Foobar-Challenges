def solution(l, t):
    if t<=0 or t>250:
        return [-1, -1]
    if len(l)==0 or len(l)>100:
        return [-1, -1]
    for itr in range(len(l)):
        if l[itr]<1 or l[itr]>100:
            return [-1, -1]
    for itr in range(len(l)):
        if l[itr]==t:
            return [itr, itr]
    if sum(l) < t:
        return [-1, -1]
    elif sum(l) == t:
        return [0, len(l)-1]
    else:
        result_list = []
        for i in range(len(l) + 1):
            for j in range(i + 1, len(l) + 1):
                result_list.append(l[i:j])
        for lst in result_list:
            if(t==sum(lst)):
                return [l.index(lst[0]), l.index(lst[-1])]
        return [-1, -1]
        
print(solution([4,3,10,2,8,9], 12))

