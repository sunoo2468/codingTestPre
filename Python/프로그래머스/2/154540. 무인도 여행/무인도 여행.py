def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    visited = [[False] * cols for _ in range(rows)]
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(rows):
        for y in range(cols):

            if maps[x][y] == 'X' or visited[x][y]:
                continue

            stack = [(x, y)]
            visited[x][y] = True
            total = 0

            while stack:
                cx, cy = stack.pop()
                total += int(maps[cx][cy])

                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]

                    if 0 <= nx < rows and 0 <= ny < cols:
                        if maps[nx][ny] != 'X' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))

            answer.append(total)

    return sorted(answer) if answer else [-1]