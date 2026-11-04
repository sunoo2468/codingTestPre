def solution(cards):
    n = len(cards)
    visited = [False] * n
    groups = []

    for i in range(n):
        if visited[i]:
            continue

        current = i
        count = 0

        while not visited[current]:
            visited[current] = True
            count += 1

            current = cards[current] - 1

        groups.append(count)

    groups.sort(reverse=True)

    if len(groups) < 2:
        return 0

    return groups[0] * groups[1]