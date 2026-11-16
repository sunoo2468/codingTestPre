def solution(info, edges):
    n = len(info)
    graph = [[] for _ in range(n)]

    for parent, child in edges:
        graph[parent].append(child)

    answer = 0

    def dfs(sheep, wolf, available):
        nonlocal answer
        answer = max(answer, sheep)

        for node in available:
            next_sheep = sheep + (info[node] == 0)
            next_wolf = wolf + (info[node] == 1)

            if next_wolf >= next_sheep:
                continue

            next_available = available.copy()
            next_available.remove(node)
            next_available.extend(graph[node])

            dfs(next_sheep, next_wolf, next_available)

    dfs(1, 0, graph[0][:])

    return answer