def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]
    oil_by_column = [0] * m

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(n):
        for y in range(m):
            if land[x][y] == 0 or visited[x][y]:
                continue

            stack = [(x, y)]
            visited[x][y] = True

            size = 0
            columns = set()

            while stack:
                cx, cy = stack.pop()

                size += 1
                columns.add(cy)

                for dx, dy in directions:
                    nx = cx + dx
                    ny = cy + dy

                    if not (0 <= nx < n and 0 <= ny < m):
                        continue

                    if land[nx][ny] == 0 or visited[nx][ny]:
                        continue

                    visited[nx][ny] = True
                    stack.append((nx, ny))

            for col in columns:
                oil_by_column[col] += size

    return max(oil_by_column)