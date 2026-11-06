def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue

        answer += 1
        stack = [i]
        visited[i] = True

        while stack:
            current = stack.pop()

            for next_node in range(n):
                if computers[current][next_node] == 1:
                    if not visited[next_node]:
                        visited[next_node] = True
                        stack.append(next_node)

    return answer