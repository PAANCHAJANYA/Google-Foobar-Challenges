def solution(src, dest):
    lst = [-17,-15,-10,-6,6,10,15,17]
    limit = 99999
    moves = 1
    possibilities = []
    newpossibilities = []
    for ele in lst:
        if (src%8)==0:
            if ele in [-17,-10,6,15]:
                continue
        if (src%8)==0 and (src//8)==0:
            if ele in [-6]:
                continue
        if (src%8)==0 and (src//8)<2:
            if ele in [-15]:
                continue
        if (src%8)==0 and (src//8)>5:
            if ele in [17]:
                continue
        if (src%8)==0 and (src//8)==7:
            if ele in [10]:
                continue
        if (src%8)==1:
            if ele in [-10,6]:
                continue
        if (src%8)==1 and (src//8)==0:
            if ele in [-6]:
                continue
        if (src%8)==1 and (src//8)<2:
            if ele in [-17,-15]:
                continue
        if (src%8)==1 and (src//8)>5:
            if ele in [15,17]:
                continue
        if (src%8)==1 and (src//8)==7:
            if ele in [10]:
                continue
        if (src%8 in [2,3,4,5]) and (src//8)==0:
            if ele in [-10,-6]:
                continue
        if (src%8 in [2,3,4,5]) and (src//8)<2:
            if ele in [-17,-15]:
                continue
        if (src%8 in [2,3,4,5]) and (src//8)>5:
            if ele in [15,17]:
                continue
        if (src%8 in [2,3,4,5]) and (src//8)==7:
            if ele in [6,10]:
                continue
        if (src%8)==6:
            if ele in [-6,10]:
                continue
        if (src%8)==6 and (src//8)==0:
            if ele in [-10]:
                continue
        if (src%8)==6 and (src//8)<2:
            if ele in [-17,-15]:
                continue
        if (src%8)==6 and (src//8)>5:
            if ele in [15,17]:
                continue
        if (src%8)==6 and (src//8)==7:
            if ele in [6]:
                continue
        if (src%8)==7:
            if ele in [-15,-6,10,17]:
                continue
        if (src%8)==7 and (src//8)==0:
            if ele in [-10]:
                continue
        if (src%8)==7 and (src//8)<2:
            if ele in [-17]:
                continue
        if (src%8)==7 and (src//8)>5:
            if ele in [15]:
                continue
        if (src%8)==7 and (src//8)==7:
            if ele in [6]:
                continue
        if ele+src >=0 and ele+src <=63:
            newpossibilities.append(ele+src)
    if dest in newpossibilities:
        return moves
    while moves < limit:
        moves = moves + 1
        possibilities = newpossibilities
        newpossibilities = []
        for ele2 in possibilities:
            for ele in lst:
                if (ele2%8)==0:
                    if ele in [-17,-10,6,15]:
                        continue
                if (ele2%8)==0 and (ele2//8)==0:
                    if ele in [-6]:
                        continue
                if (ele2%8)==0 and (ele2//8)<2:
                    if ele in [-15]:
                        continue
                if (ele2%8)==0 and (ele2//8)>5:
                    if ele in [17]:
                        continue
                if (ele2%8)==0 and (ele2//8)==7:
                    if ele in [10]:
                        continue
                if (ele2%8)==1:
                    if ele in [-10,6]:
                        continue
                if (ele2%8)==1 and (ele2//8)==0:
                    if ele in [-6]:
                        continue
                if (ele2%8)==1 and (ele2//8)<2:
                    if ele in [-17,-15]:
                        continue
                if (ele2%8)==1 and (ele2//8)>5:
                    if ele in [15,17]:
                        continue
                if (ele2%8)==1 and (ele2//8)==7:
                    if ele in [10]:
                        continue
                if (ele2%8) in [2,3,4,5] and (ele2//8)==0:
                    if ele in [-10,-6]:
                        continue
                if (ele2%8) in [2,3,4,5] and (ele2//8)<2:
                    if ele in [-17,-15]:
                        continue
                if (ele2%8) in [2,3,4,5] and (ele2//8)>5:
                    if ele in [15,17]:
                        continue
                if (ele2%8) in [2,3,4,5] and (ele2//8)==7:
                    if ele in [6,10]:
                        continue
                if (ele2%8)==6:
                    if ele in [-6,10]:
                        continue
                if (ele2%8)==6 and (ele2//8)==0:
                    if ele in [-10]:
                        continue
                if (ele2%8)==6 and (ele2//8)<2:
                    if ele in [-17,-15]:
                        continue
                if (ele2%8)==6 and (ele2//8)>5:
                    if ele in [15,17]:
                        continue
                if (ele2%8)==6 and (ele2//8)==7:
                    if ele in [6]:
                        continue
                if (ele2%8)==7:
                    if ele in [-15,-6,10,17]:
                        continue
                if (ele2%8)==7 and (ele2//8)==0:
                    if ele in [-10]:
                        continue
                if (ele2%8)==7 and (ele2//8)<2:
                    if ele in [-17]:
                        continue
                if (ele2%8)==7 and (ele2//8)>5:
                    if ele in [15]:
                        continue
                if (ele2%8)==7 and (ele2//8)==7:
                    if ele in [6]:
                        continue
                if ele+ele2>=0 and ele+ele2<=63:
                    newpossibilities.append(ele+ele2)
        if dest in newpossibilities:
            return moves
print(solution(0,63))
