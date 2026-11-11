def solution(grid):
    rows = len(grid)
    cols = len(grid[0])

    # 상, 우, 하, 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [
        [[False] * 4 for _ in range(cols)]
        for _ in range(rows)
    ]

    answer = []

    for x in range(rows):
        for y in range(cols):
            for d in range(4):

                if visited[x][y][d]:
                    continue

                cx, cy, cd = x, y, d
                length = 0

                while not visited[cx][cy][cd]:
                    visited[cx][cy][cd] = True
                    length += 1

                    if grid[cx][cy] == 'L':
                        cd = (cd + 3) % 4

                    elif grid[cx][cy] == 'R':
                        cd = (cd + 1) % 4

                    cx = (cx + dx[cd]) % rows
                    cy = (cy + dy[cd]) % cols

                answer.append(length)

    return sorted(answer)