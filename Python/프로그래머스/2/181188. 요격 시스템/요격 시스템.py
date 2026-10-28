def solution(targets):
    
    targets.sort(key=lambda x: x[1])
    last_end = targets[0][1]
    answer = 1
    
    for start, end in targets[1:]:
        if start >= last_end:
            last_end = end
            answer += 1
            
    return answer