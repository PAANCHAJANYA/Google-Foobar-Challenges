def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return (gcd(x, y)==1)
def solution(x, y):
    call = 0
    if int(x)==int(y):
        return "impossible"
    elif int(x)==1:
        return str(int(y)-1)
    elif int(y)==1:
        return str(int(x)-1)
    elif (int(x))%2==0 and (int(y))%2==0:
        return "impossible"
    elif (int(x))%3==0 and (int(y))%3==0:
        return "impossible"
    elif (int(x))%5==0 and (int(y))%5==0:
        return "impossible"
    elif (int(x))%7==0 and (int(y))%7==0:
        return "impossible"
    elif not is_coprime(int(x),int(y)):
        return "impossible"
    while (int(x))!=1 or (int(y))!=1:
        if int(y) == 1:
            return str(call+int(x)-1)
        else:
            call = call + int(int(x)/int(y))
            temp = int(x)%int(y)
            x = y
            y = str(temp)
    return str(call)

print(65000000000000000, 58041, solution(str(65000000000000000),str(58401)))
