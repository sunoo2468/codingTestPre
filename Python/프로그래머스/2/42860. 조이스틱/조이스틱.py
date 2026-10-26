def solution(name):
    # 1. 알파벳 변경 횟수
    vertical = 0

    for char in name:
        up = ord(char) - ord('A')
        down = 26 - up
        vertical += min(up, down)

    # 2. A가 아닌 위치만 표시
    targets = [1 if char != 'A' else 0 for char in name]

    n = len(name)

    # 3. 오른쪽으로만 이동하는 경우
    horizontal = n - 1

    # 4. 방향을 바꾸는 모든 위치 확인
    for i in range(n):
        next_idx = i + 1

        # 연속된 A 구간 건너뛰기
        while next_idx < n and targets[next_idx] == 0:
            next_idx += 1

        # 오른쪽으로 갔다가 왼쪽으로 돌아오기
        right_first = 2 * i + (n - next_idx)

        # 왼쪽으로 갔다가 오른쪽으로 돌아오기
        left_first = i + 2 * (n - next_idx)

        horizontal = min(
            horizontal,
            right_first,
            left_first
        )

    return vertical + horizontal