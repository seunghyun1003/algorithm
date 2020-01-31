import numpy as np

def solution(answers):
    answer = []
    patterns = np.array([[1,2,3,4,5,1,2,3,4,5], [2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]])
    scores = [0]*len(patterns)
    
    for i, a in enumerate(answers):
        for j, p in enumerate(patterns):
            if a == p[i % len(p)]:
                scores[j] += 1
                
    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i+1)
        else:
            pass
    return answer
