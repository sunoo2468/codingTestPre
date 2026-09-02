def solution(triangle):
    dp = []

    # triangle과 같은 구조의 dp 생성
    for row in triangle:
        dp.append([0] * len(row))

    # 시작점
    dp[0][0] = triangle[0][0]

    # 두 번째 줄부터 계산
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):

            # 맨 왼쪽
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]

            # 맨 오른쪽
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]

            # 가운데
            else:
                dp[i][j] = max(
                    dp[i - 1][j - 1],
                    dp[i - 1][j]
                ) + triangle[i][j]

    return max(dp[-1])