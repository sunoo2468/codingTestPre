from collections import deque

def solution(maps):
    queue = deque()
    visited = {}
    
    visited[(0, 0)] = 1  # 시작점 방문 처리
    queue.append((0,0)) # 시작은 (0,0)
    
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵의 범위 내인지 확인
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
                
            if maps[nx][ny] == 1 and (nx, ny) not in visited:
                visited[(nx, ny)] = visited[(x, y)] + 1
                queue.append((nx,ny))
    
    # 목적지까지 도달 후 거리 계산
    target = len(maps) -1, len(maps[0])-1
    
    if target in visited:
        return visited[target]

    return -1
