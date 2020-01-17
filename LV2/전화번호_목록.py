def solution(phone_book):
    answer = True

    pblen = sorted(phone_book, key=len)
    
    
    for i in len(pblen):
        for j in len(pblen):
            if pblen[i].startswith(pblen[j]):
                answer = false
            else: answer = true
    
    return answer
