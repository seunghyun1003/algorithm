from collections import Counter

def solution(participant, completion):
    answer_list = []
    
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    result = participant_count - completion_count
    
    for name in result:
        if result.values() != 0:
            answer_list.append(name)
            
    answer = ",".join(answer_list)
    return answer
            
    
