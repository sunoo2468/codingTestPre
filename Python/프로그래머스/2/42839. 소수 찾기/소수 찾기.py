def solution(numbers):
    candidates = set()
    visited = [False] * len(numbers)

    def is_prime(n):
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    def dfs(current):
        if current:
            num = int(current)

            if is_prime(num):
                candidates.add(num)

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True       # 1. 숫자 선택
                dfs(current + numbers[i])  # 2. 다음 숫자 탐색
                visited[i] = False      # 3. 선택 취소

    dfs("")
    return len(candidates)