def solution(k, tangerine):
    answer = 0
    count = {}

    for size in tangerine:
        if size in count:
            count[size] += 1
        else:
            count[size] = 1
            
    counts = sorted(count.values(), reverse=True)
    
    for c in counts:
        k -= c
        answer += 1
        
        if k <= 0:
            break
            
    return answer