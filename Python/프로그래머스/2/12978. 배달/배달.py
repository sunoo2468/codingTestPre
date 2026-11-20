import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    distance = [float('inf')] * (N + 1)
    distance[1] = 0

    heap = [(0, 1)]

    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for next_node, cost in graph[now]:
            new_dist = dist + cost

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return sum(1 for d in distance[1:] if d <= K)