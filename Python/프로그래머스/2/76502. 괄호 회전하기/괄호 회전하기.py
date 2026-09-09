from collections import deque
def solution(s):
    answer = 0
    
    s_dict = {
        "{" : "}",
        "(" : ")", 
        "[" : "]"
    }
    
    queue = deque(s)
    
    for i in range(len(s)):
        stack = []
        
        for k in range(len(s)):
            current = queue[k]
            
            if current in s_dict:
                stack.append(current)
            else :
                if not stack:
                    # print("스택이 비어있음, 전 값 확인 불가")
                    stack.append("1")
                    break
                if(s_dict[stack[-1]] == current):
                    stack.pop()
                else:
                    stack.append("1")
                    break
                
        if len(stack) == 0:
            answer += 1
        
        queue.rotate(-1)
        
    return answer