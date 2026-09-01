def solution(numbers, target):
    answer = 0
    def dfs(index, total):

        # 모든 숫자를 사용했다면
        if index == len(numbers):
            if(total==target): 
                return 1
            return 0

        # 현재 숫자를 + 하는 경우
        plus = dfs(index + 1, total + numbers[index])

        # 현재 숫자를 - 하는 경우
        minus = dfs(index + 1, total - numbers[index])

        # 두 경로에서 찾은 정답 개수를 합쳐서 위로 전달
        return plus + minus
        
    answer = dfs(0,0)
    
    return answer