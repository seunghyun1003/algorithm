def solution(phone_book):
    answer = True
    sorted_phone_book = sorted(phone_book)
    for a in range(len(phone_book)-1):
        if sorted_phone_book[a] in sorted_phone_book[a+1] :
            return False
        else:
            return True
    return answer
