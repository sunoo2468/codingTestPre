def solution(tickets):
    tickets.sort()

    visited = [False] * len(tickets)
    path = ["ICN"]

    def dfs(current):
        # 모든 항공권을 사용했다면 성공
        if len(path) == len(tickets) + 1:
            return True

        for i in range(len(tickets)):
            start, end = tickets[i]

            # 현재 공항에서 출발하고 아직 사용하지 않은 항공권
            if not visited[i] and start == current:
                visited[i] = True
                path.append(end)

                # 다음 공항에서 계속 탐색
                if dfs(end):
                    return True

                # 실패한 선택을 취소 (백트래킹)
                path.pop()
                visited[i] = False

        return False

    dfs("ICN")
    return path