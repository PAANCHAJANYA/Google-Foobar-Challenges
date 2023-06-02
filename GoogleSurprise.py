def solution(s):
    string = ""
    for itr in range(len(s)):
        if(string != ""):
            lens = len(s)
            lenstring = len(string)
            if(string * int(lens/lenstring) == s):
                return int(lens/lenstring)
        string = string + s[itr]
    return 1



print(solution("abcc"))
