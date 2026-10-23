def solution(n, wires):
    answer = n

    # 1. 인접 리스트 생성
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # 2. DFS: 연결된 송전탑 개수 세기
    def dfs(node, visited, cut_a, cut_b):
        visited[node] = True
        count = 1

        for next_node in graph[node]:

            # 끊은 전선은 지나가지 않음
            if (node == cut_a and next_node == cut_b) or \
               (node == cut_b and next_node == cut_a):
                continue

            if not visited[next_node]:
                count += dfs(next_node, visited, cut_a, cut_b)

        return count

    # 3. 전선을 하나씩 끊어보기
    for a, b in wires:
        visited = [False] * (n + 1)

        count = dfs(1, visited, a, b)

        # 4. 두 전력망의 송전탑 개수 차이
        diff = abs(count - (n - count))

        answer = min(answer, diff)

    return answer