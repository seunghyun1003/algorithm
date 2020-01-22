def solution(s,c):

    s.sort()
    c.sort()

    for par, com in zip(s, c) :
        if par != com :
            return par   

    return s[-1]       
